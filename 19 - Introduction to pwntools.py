from pwn import *
import pwnlib.util
import pwnlib.util.hashes

# Generate a cyclic pattern of 50 bytes.
# This pattern is a sequence of characters designed to be unique
# within the specified length. Each position in the pattern is different,
# which helps in identifying how far into the memory the overflowed data has reached.
cycle_pattern = cyclic(50)

# Print the generated cyclic pattern to the console.
# This output will look like a string of characters, where each set of characters is unique.
# Example output might look like: 'AAAABBBBCCCCDDDDEEEEFFFF...'
print(cycle_pattern)

# How this helps with debugging buffer overflows:
# 1. **Create the Overflow**:
#    Use this cyclic pattern as input to a program that has a buffer overflow vulnerability.
#    The pattern will overflow the buffer and overwrite adjacent memory locations.

# 2. **Analyze the Crash**:
#    When the program crashes (e.g., due to a return address being overwritten),
#    examine the memory or core dump to see where the overflowed data has ended up.

# 3. **Find the Overwritten Data**:
#    Look at the memory location that was overwritten (e.g., the return address on the stack).
#    You will see a portion of the cyclic pattern in this location.

# 4. **Determine the Offset**:
#    By comparing the overwritten data with the original cyclic pattern, you can identify
#    the exact position of the pattern that ended up in the memory location. 
#    For example, if the return address in memory is 'CCCC', and 'CCCC' starts at the 20th byte of the cyclic pattern,
#    then the offset to the return address is 20 bytes from the start of the buffer.

# Crafting a More Precise Exploit Payload:
# 1. **Identify the Offset**:
#    With the offset determined, you now know how far into the buffer the return address is.
#    This helps you precisely control the data in memory.

# 2. **Prepare Your Payload**:
#    Your exploit payload typically consists of:
#    - **Padding**: Fill the buffer up to the offset. This is done with 'NOP' operations or any filler data.
#    - **Return Address**: Replace the return address with the address of your shellcode or payload.
#    - **Shellcode**: This is the actual code you want to execute, such as a reverse shell.

# 3. **Example Payload Construction**:
#    Let's say the offset is 40 bytes. Your payload might look like this:
#    ```python
#    # Create the payload
#    padding = b'A' * 40  # Padding to reach the return address
#    return_address = p32(0xdeadbeef)  # Example address to overwrite with
#    shellcode = b'\x90' * 100 + b'\xcc' * 10  # NOP sled and shellcode

#    payload = padding + return_address + shellcode
#    ```
#    - `b'A' * 40` creates 40 bytes of padding.
#    - `p32(0xdeadbeef)` is an example function to convert the return address into a 4-byte format.
#    - `b'\x90' * 100` is a NOP sled (no operation instructions) to slide into the shellcode.
#    - `b'\xcc' * 10` represents the actual shellcode (in this example, a series of breakpoint instructions).

# 4. **Test the Exploit**:
# Use this payload to test your exploit against the vulnerable program. Adjust the payload based on the results
# and refine your approach as needed.

# By understanding the offset and crafting a precise payload, you gain control over the program's execution flow
#  and can exploit vulnerabilities more effectively.

# Additional Notes:
# - **NOP Sled**: In the payload example, `b'\x90' * 100` represents a NOP sled. The NOP sled is a sequence of no-operation instructions
#  that allows the CPU to "slide" into the actual shellcode. If the program's execution jumps into the NOP sled,
#  it will eventually reach the shellcode, making it easier for the exploit to succeed even if the exact jump location isn't precise.

# - **0xdeadbeef**: This is a placeholder address used for demonstration purposes. It is not an actual function
#  but a common example address in exploit development. You would replace this with the actual address where your shellcode or exploit payload is located.

print("----------------------------")

# Example usage of cyclic_find function
# This function helps you locate the position of a specific pattern within a cyclic pattern.

# Suppose you have a specific sequence (pattern) you want to find in the cyclic pattern.
# For example, the sequence 'laaa' is the pattern we're looking for within the cyclic pattern.

# The cyclic_find function returns the offset where the specified pattern starts within the cyclic sequence.
# This is useful in exploitation scenarios to pinpoint where a particular value or sequence is located
# within the cyclic pattern, which can help in determining offsets and crafting precise payloads.

# Generate a cyclic pattern of sufficient length.
# For demonstration, we use a pattern that is longer than the length of the sequence we are searching for.
# The length of the pattern should be large enough to ensure it covers the possible range where 'laaa' might appear.
cyclic_pattern = cyclic(50)

# Use cyclic_find to locate the position of the pattern 'laaa' within the cyclic pattern.
# The function will return the offset (position) where 'laaa' starts in the cyclic pattern.
offset = cyclic_find("laaa")

# Print the result.
# The output will be the position in the cyclic pattern where 'laaa' starts.
print(offset)

# Explanation:
# 1. **Generate Cyclic Pattern**:
#    A cyclic pattern is generated to cover a large range of unique sequences. This pattern repeats in a specific order, ensuring that each position is distinct.

# 2. **Find Pattern Offset**:
#    The `cyclic_find` function searches the cyclic pattern for the specified sequence ('laaa' in this case). 
#    It returns the starting index (offset) of the sequence within the cyclic pattern.

# 3. **Use in Exploits**:
#    Finding the offset of a specific sequence helps in identifying where it lies in memory after a buffer overflow. 
#    This can be used to precisely control the execution flow or locate the overwritten return address.

# Note: 
# Ensure that the cyclic pattern length is long enough to contain the sequence you are searching for. 
# If the pattern is too short, it might not contain the sequence, leading to incorrect or no results.


# Print the shellcode that spawns a shell
# The shellcraft.sh() function generates an assembly code snippet that, when executed,
# spawns a shell (`/bin/sh`) using the `execve` system call.

print("----------------------------")

print(shellcraft.sh())

# Explanation of the generated assembly code:

# The goal of this shellcode is to execute a shell (`/bin/sh`) using the execve system call.

# 1. **Understanding execve**:
#    - `execve` is a system call used to execute a program. It replaces the current process with a new process.
#    - It takes three arguments:
#      1. `path` - The path to the executable (e.g., '/bin/sh').
#      2. `argv` - An array of arguments to pass to the executable. The first element is typically the name of the executable itself.
#      3. `envp` - An array of environment variables. Passing 0 means no environment variables are passed.

# Assembly code breakdown:
# /* execve(path='/bin///sh', argv=['sh'], envp=0) */

# 2. **Push the string '/bin/sh' onto the stack**
#    - This is the path of the executable we want to run.
#    - The string '/bin/sh' is pushed onto the stack in a reversed order to be used later by execve.
#    The following assembly instructions achieve this:
#    push 0x68                # Pushes the byte 0x68 (ASCII for 'h') onto the stack.
#    push 0x732f2f2f          # Pushes the bytes '///s' onto the stack (ASCII for 's' and '/').
#    push 0x6e69622f          # Pushes the bytes '/bin' onto the stack (ASCII for 'b', 'i', 'n', and '/').

# 3. **Set up the argv array**
#    - This is an array of arguments for execve, where we need to pass a pointer to the string '/bin/sh'.
#    - We create this array and make sure it is null-terminated.

#    The following assembly instructions set up the argument array:
#    push 0x1010101           # Pushes 0x1010101, which will be XORed to form 'sh\x00\x00'.
#    xor dword ptr [esp], 0x1016972  # XORs the value at [esp] with 0x1016972 to produce 'sh\x00'.
#    xor ecx, ecx             # Clear ecx register (set it to 0). Registers are used to hold and manipulate data.
#    push ecx                 # Push null byte to terminate the string 'sh\x00'.
#    push 4                   # Push the length of the argument array (4 bytes) onto the stack.
#    pop ecx                  # Pop the length into ecx register.
#    add ecx, esp             # Adjust ecx to point to the address of the argument 'sh\x00'.
#    push ecx                 # Push the address of the argument array onto the stack.

# 4. **Prepare the execve system call**
#    - Set up the registers for the execve system call:
#      - `ebx` will hold the path to the executable.
#      - `ecx` will hold the pointer to the argument array.
#      - `edx` will hold the environment pointer (null in this case).

#    The following assembly instructions set up the system call parameters:
#    mov ecx, esp             # Move the stack pointer to ecx (argv pointer). This sets up the argument pointer.
#    xor edx, edx             # Clear edx register (envp pointer is null). Setting edx to 0, as no environment variables are passed.

# 5. **Invoke the execve system call**
#    - The syscall number for execve is 0xb.
#    - We need to set up eax with the syscall number and then execute the interrupt.

#    The following assembly instructions invoke the execve system call:
#    push SYS_execve           # Push the syscall number for execve (0xb) onto the stack.
#    pop eax                  # Pop the syscall number into the eax register.
#    int 0x80                 # Trigger the interrupt to make the syscall.

# Summary:
# This shellcode sets up and invokes the execve system call to run '/bin/sh'. 
# It first pushes the path '/bin/sh' and the argument array onto the stack, 
# then prepares the registers and finally makes the system call to execute the shell.

# Additional Information:
# - **Registers**: Registers are small storage locations in the CPU used to hold and manipulate data. Common registers include `eax`, `ebx`, `ecx`, and `edx`.
# - **ecx**: The name "ecx" stands for "Extended Count Register". It is often used as a counter or pointer in operations.
# - **edx**: The name "edx" stands for "Extended Data Register". It is used for various purposes, including as a data register or in extended arithmetic operations.
# - **xor Operation**: The XOR operation is used to modify the data in memory. It helps in constructing or adjusting specific values without directly storing them. For example, XORing can be used to manipulate values to get a desired result (like creating 'sh\x00').

# This shellcode is crafted to work in environments where you need to spawn a shell and is a common example in exploit development.

print("----------------------------")

# This line combines multiple operations into one:
print(hexdump(asm(shellcraft.sh())))

# Explanation:

# 1. **shellcraft.sh()**:
#    - This generates assembly code for spawning a shell (as explained previously).
#    - It outputs assembly instructions that will invoke the `execve` system call to run `/bin/sh`.

# 2. **asm()**:
#    - The `asm()` function compiles the assembly code (generated by `shellcraft.sh()`) into machine code (bytecode).
#    - Assembly language is human-readable, but the CPU can only understand machine code, so `asm()` translates the assembly into the binary instructions that the CPU can execute.
#    - In essence, `asm()` turns the shellcode from assembly format to its raw hexadecimal form, which the computer understands and runs.

# 3. **hexdump()**:
#    - The `hexdump()` function takes raw bytes (in this case, the machine code generated by `asm()`) and displays it in a human-readable hexadecimal format.
#    - Hexdump is a common way to represent binary data, showing both the hexadecimal values and the corresponding ASCII characters for each byte.
#    - This allows us to see the machine code in a structured format, which is useful for debugging, analyzing, or injecting it into a vulnerable program.

# 4. **print()**:
#    - Finally, the `print()` function outputs the result of `hexdump(asm(shellcraft.sh()))` to the console.
#    - This will display the hexadecimal representation of the compiled shellcode and its corresponding ASCII values.

# Summary of the whole line:
# - This line generates shellcode for spawning a shell (`shellcraft.sh()`),
#   compiles that shellcode into machine code (`asm()`),
#   and then outputs a hex dump of the machine code (`hexdump()`) to make it easier to inspect or use in an exploit.

print("----------------------------")

# This line is using the p32() function to pack an integer (0x13371337) into a 32-bit little-endian format.
print(p32(0x13371337))

# Explanation:

# 1. **0x13371337**:
#    - This is a hexadecimal number (base 16) commonly used as a "magic number" in exploit development.
#    - Hexadecimal numbers are often used in low-level programming because they map easily to binary, and 0x13371337 is a recognizable, easy-to-spot pattern.

# 2. **p32()**:
#    - The `p32()` function is used to **pack** a 32-bit integer into a byte string, formatted in **little-endian** order.
#    - Little-endian means the least significant byte (LSB) comes first. This is the default byte order on x86 architectures.
#    - Packing is essential when dealing with binary exploitation because you often need to convert human-readable integers into raw bytes that a computer can process.
#    - For example, in buffer overflows or when crafting an exploit, you might need to pack addresses or values into the correct byte format before injecting them into memory.

# 3. **Why pack the integer?**
#    - In exploit development, you may need to inject specific values, such as memory addresses or return values, into a vulnerable program.
#    - These values must be in the correct byte order and size (32-bit or 64-bit depending on the system) for the program to interpret them correctly.
#    - By using `p32()`, you're ensuring that the integer `0x13371337` is represented as a sequence of 4 bytes, compatible with the target system's architecture.

# 4. **Little-endian example**:
#    - For the integer `0x13371337`, the bytes are packed as:
#      - `0x37` (LSB)
#      - `0x13`
#      - `0x37`
#      - `0x13` (MSB)
#    - When packed with `p32()`, it results in the byte string: `b'7\x13\x37\x13'`.

# 5. **print()**:
#    - The `print()` function will output the packed byte representation of `0x13371337`.
#    - It will look something like: `b

print("----------------------------")

# This line performs a sequence of operations involving packing and unpacking a 32-bit integer.
print(hex(u32(p32(0x13371337))))

# Explanation:

# 1. **p32(0x13371337)**:
#    - The `p32()` function packs the integer `0x13371337` into a 32-bit little-endian byte string (as explained earlier).
#    - This converts the integer `0x13371337` (hexadecimal) into a 4-byte sequence: `b'7\x13\x37\x13'`.
#    - The result is a byte string that represents the original integer in little-endian format.

# 2. **u32()**:
#    - The `u32()` function **unpacks** a 32-bit byte string back into an integer.
#    - In this case, it takes the 4-byte sequence from `p32(0x13371337)` (`b'7\x13\x37\x13'`) and converts it back into a 32-bit integer.
#    - Since we packed it in little-endian format, `u32()` will reverse the process and restore the original integer, which is `0x13371337`.

# 3. **hex()**:
#    - The `hex()` function converts the integer returned by `u32()` into a hexadecimal string for easier readability.
#    - Since we originally packed a hexadecimal number (`0x13371337`), this function helps format the output in the same way.

# 4. **print()**:
#    - The `print()` function outputs the final result as a hexadecimal string.
#    - In this case, the printed result will be the original number `0x13371337`, showing that the process of packing and unpacking preserved the value.

# Summary of the whole line:
# - `p32(0x13371337)` packs the integer `0x13371337` into a 4-byte little-endian string.
# - `u32()` then unpacks the byte string back into the original integer.
# - `hex()` formats the integer as a hexadecimal string.
# - The printed output confirms that the original integer is unchanged: `0x13371337`.

# Example output:
# 0x13371337

print("----------------------------")

# This script creates a process that interacts with the system shell and sends commands to it.
p = process("/bin/sh")  # 1. Create a new process running '/bin/sh'.
#    - `process("/bin/sh")` starts a new process running the system's shell (`/bin/sh`).
#    - This allows us to interact with the shell programmatically, as if we were typing commands directly into a terminal.

p.sendline("echo hello;")  # 2. Send the command 'echo hello' to the shell.
#    - `p.sendline()` sends a string to the process followed by a newline (`\n`).
#    - In this case, it's sending the command `echo hello;` which will instruct the shell to print the string "hello" to standard output.
#    - The `;` at the end of the command is optional but often used to signal the end of a command in shells.

p.interactive()  # 3. Switch to interactive mode to take control of the shell.
#    - `p.interactive()` hands control over to the user, allowing them to interact with the shell directly.
#    - This means that after sending the initial command, the user can continue typing and interacting with the shell as if it were a regular terminal session.

# Summary:
# - This script opens a shell process, sends a command to print "hello", and then allows the user to take over the shell interactively.
# - It's useful in exploit development when you want to automate interaction with a shell and then switch to manual control.

print("----------------------------")

# This script connects to a remote service and interacts with it.
# Spin up netcat, nc -nvlp 1234  
r = remote("127.0.0.1", 1234)  # 1. Connect to a remote service at IP 127.0.0.1 on port 1234.
#    - `remote("127.0.0.1", 1234)` creates a connection to a remote server.
#    - Here, "127.0.0.1" is the loopback address (localhost), meaning the connection is made to a service running on the same machine.
#    - Port 1234 is the network port where the remote service is listening.

r.sendline("hello!")  # 2. Send the string 'hello!' to the remote service.
#    - `r.sendline()` sends the provided string followed by a newline character (`\n`) to the remote server.
#    - In this case, it sends the message "hello!" to the service, similar to how a command or message would be sent to a server or application.

r.interactive()  # 3. Switch to interactive mode to interact with the remote service.
#    - `r.interactive()` allows the user to interact directly with the remote service through the open connection.
#    - After sending the initial message, this hands over control to the user so they can continue interacting with the service manually (just like typing in a terminal).

r.close()  # 4. Close the connection to the remote service.
#    - `r.close()` closes the connection to the remote server.
#    - It's a good practice to close connections after you're done using them to free up resources.

# Summary:
# - This script establishes a connection to a service running on the same machine (localhost) on port 1234.
# - It sends a message ("hello!") to the service, then switches to interactive mode to allow manual interaction.
# - Finally, it closes the connection to the remote service.

print("----------------------------")

# Load the ELF (Executable and Linkable Format) binary for '/bin/bash'.
l = ELF('/bin/bash')

# What is ELF?
#    - ELF (Executable and Linkable Format) is a common file format for executables, object code, shared libraries, and core dumps in Unix-based systems.
#    - It contains several sections, such as the code, data, symbol tables, and relocation information, making it a versatile format.
#    - In security research or exploitation, understanding the ELF format allows us to access critical information such as function addresses, Global Offset Table (GOT) entries, and the program's entry point.

# 1. Print the base address of the ELF binary.
print(hex(l.address))  
#    - `l.address` provides the base address of the loaded ELF binary in memory.
#    - The base address is where the binary starts in the process's virtual address space.
#    - For statically linked binaries, the base address is fixed. However, for dynamically linked binaries, this base address may change due to ASLR (Address Space Layout Randomization).
#    - This base address is important when calculating the actual address of various functions and data within the ELF file during runtime.

# 2. Print the entry point address of the ELF binary.
print(hex(l.entry))  
#    - `l.entry` gives the entry point address of the ELF binary.
#    - The entry point is the address where execution starts when the binary is run by the operating system.
#    - This is generally the first instruction of the program or where the setup code begins before handing control to `main()`.
#    - Knowing the entry point is useful in reverse engineering and exploitation because it can help identify where control starts and where to focus analysis.

# 3. Print the Global Offset Table (GOT) entry for the `write` function.
print(hex(l.got['write']))  
#    - The Global Offset Table (GOT) is a mechanism used by dynamically linked executables to resolve and store addresses of external functions (like those in shared libraries).
#    - `l.got['write']` retrieves the address in the GOT that stores the address of the `write` function.
#    - When a dynamically linked binary first needs to call an external function (like `write` from the C library), it uses the GOT to find out where that function lives in memory.
#    - In exploitation, an attacker may attempt to overwrite GOT entries to hijack control flow and redirect execution to malicious code or a different function (this is known as a GOT overwrite attack).
#    - The ability to read GOT entries is essential for understanding how a program interacts with external libraries at runtime.

# Summary:
# - `ELF('/bin/bash')` loads the ELF binary for '/bin/bash' and provides access to its metadata and addresses.
# - The base address (`l.address`) is where the binary is loaded into memory, useful for calculating the absolute address of functions and variables.
# - The entry point (`l.entry`) is where the program starts executing, making it a critical address in analyzing program flow.
# - The GOT entry for `write` (`l.got['write']`) is the address where the program will look up the actual memory address of the `write` function at runtime.
# - This information is invaluable for reverse engineering and exploit development, as it helps map out how a binary works and where potential weaknesses may lie.

print("----------------------------")

# The ELF object is created for the '/bin/bash' binary.
l = ELF('/bin/bash')

# Search for the string '/bin/sh\x00' in the ELF binary and print its memory addresses.
#    - `l.search(b'/bin/sh\x00')` searches for the byte sequence '/bin/sh\x00' (null-terminated string) in the ELF binary.
#    - '/bin/sh' is typically used in shellcode to spawn a shell, and the null terminator (`\x00`) is required by C-style strings.
#    - The search function returns an iterable of addresses where the byte sequence is found in the binary.
#    - These addresses are essential when crafting exploits that need to reference or use '/bin/sh' for shell access.
for address in l.search(b'/bin/sh\x00'):
    print(hex(address))  # Print the address of '/bin/sh' in hexadecimal format.

# Explanation:
#    - This code is useful for exploit developers trying to locate '/bin/sh' within the binary.
#    - In many shellcode exploits, `/bin/sh` is used to spawn a shell, allowing the attacker to execute commands.

# Search for the 'jmp esp' instruction in the binary and print the first result.
#    - `asm('jmp esp')` assembles the x86 instruction 'jmp esp' into machine code using pwntools' `asm()` function.
#    - 'jmp esp' is often used in exploits to hijack control flow. Specifically, it jumps to the stack pointer (`esp`) and starts executing the code there.
#    - This is helpful in situations like buffer overflows, where the attacker wants to execute their payload (shellcode) that is located on the stack.
#    - `l.search()` looks for this instruction in the ELF binary and returns its memory address.
#    - `next()` fetches the first occurrence of the 'jmp esp' instruction in the ELF, which is the address that an attacker can use to control execution flow.
print(next(l.search(asm('jmp esp'))))  # Print the first occurrence

print("----------------------------")

# Load the ELF binary (in this case, '/bin/bash').
l = ELF('/bin/bash')

# Create a ROP object for the loaded ELF binary.
#    - ROP stands for Return-Oriented Programming.
#    - ROP is a common exploitation technique that uses small chunks of code (called "gadgets") that already exist in the binary to execute arbitrary logic.
#    - The `ROP()` constructor analyzes the ELF binary and identifies useful gadgets (small sequences of instructions that end with a return).
#    - These gadgets are then used to chain together an exploit without injecting new code, instead reusing existing code to perform malicious actions.
r = ROP(l)

# Print the address of the `rbx` register gadget found in the ROP chain.
#    - ROP gadgets often manipulate specific registers.
#    - `r.rbx` gives the address of the first gadget that moves a value into the `rbx` register.
#    - The `rbx` register in x86_64 architecture is a general-purpose register often used to store base addresses or intermediate values.
#    - In ROP chains, specific registers need to be loaded with values or pointers to build up the exploit.
print(r.rbx)  
#    - This prints the address of the gadget that can manipulate the `rbx` register.
#    - This gadget can be used as part of a chain in an exploit, where you need to control the value in `rbx` for a particular purpose (such as loading an address or preparing for a system call).

print("----------------------------")

# XOR the characters "A" and "B"
#    - XOR is a bitwise operation where bits are compared. If the bits are the same, the result is 0, and if they are different, the result is 1.
#    - "A" in ASCII is represented as 0x41 (binary: 01000001).
#    - "B" in ASCII is represented as 0x42 (binary: 01000010).
#    - XORing 0x41 and 0x42 results in 0x03 (binary: 00000011).
#    - The result will be the byte corresponding to the XORed value.
result1 = xor("A", "B")
print(result1)  # This will print '\x03' because the XOR of "A" and "B" gives the byte value 0x03.

# Now, XOR the result of the previous XOR operation with "A"
#    - The result of the first XOR operation was '\x03'.
#    - XORing '\x03' (binary: 00000011) with "A" (0x41, binary: 01000001):
#      00000011 XOR 01000001 = 01000010, which is the ASCII value for "B".
#    - Essentially, XORing a character with another, then XORing it again with the first character, gives back the second one.
result2 = xor(result1, "A")
print(result2)  # This will print 'B' because XORing the result with "A" recovers the original "B".

print("----------------------------")

# Encode a byte string to Base64
#    - Base64 encoding represents binary data in an ASCII string format using 64 printable characters.
#    - This is useful for encoding binary data (like files or byte strings) into a text format for transmission or storage.
#    - The `b64e()` function from the `pwn` library performs this encoding.
encoded = b64e(b"test")
print(encoded)  # This will print b'dGVzdA==', which is the Base64 encoding of the byte string b'test'.

# Decode a Base64 encoded byte string
#    - The `b64d()` function from the `pwn` library decodes a Base64 encoded byte string back to its original binary form.
#    - The encoded string b"dGVzdA==" represents the ASCII string "test" in Base64 encoding.
decoded = b64d(b"dGVzdA==")
print(decoded)  # This will print b'test', which is the original byte string decoded from the Base64 encoded input.

print("----------------------------")

from pwnlib.util.hashes import md5sumhex, sha1sumhex

# Compute the MD5 checksum of a byte string
#    - The `md5sumhex` function calculates the MD5 hash of the input byte string and returns it as a hexadecimal string.
#    - MD5 is a widely used hash function that produces a 128-bit hash value, typically represented as a 32-character hexadecimal number.
#    - The input here is b"hello", which is a byte string containing the text "hello".
#    - The function will output the MD5 checksum of this byte string.
md5_checksum = md5sumhex(b"hello")
print(md5_checksum)  # This will print the hexadecimal representation of the MD5 hash of "hello".

# Compute the SHA-1 checksum of a byte string
#    - The `sha1sumhex` function calculates the SHA-1 hash of the input byte string and returns it as a hexadecimal string.
#    - SHA-1 produces a 160-bit hash value, typically represented as a 40-character hexadecimal number.
#    - The input here is b"hello", which is the same byte string used for the MD5 checksum.
#    - The function will output the SHA-1 checksum of this byte string.
sha1_checksum = sha1sumhex(b"hello")
print(sha1_checksum)  # This will print the hexadecimal representation of the SHA-1 hash of "hello".

print("----------------------------")

bits_for_a = bits(b'a')
print(bits_for_a)
print(unbits(bits_for_a))