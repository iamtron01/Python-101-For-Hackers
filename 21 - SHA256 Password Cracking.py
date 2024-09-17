from pwn import *
from pwnlib.util.hashes import sha256sum
import sys

FAIL = -1
SUCCESS = 0

def crack_sha256_hash(password, hash_to_crack):
    computed_hash = (sha256sum(
        password
        .encode('utf8'))
        .hex())
    return computed_hash == hash_to_crack

def open_passwords(passwords):
    with open(passwords, "r") as passwords:
        for password in passwords:
            password = password.strip()
            yield password

if __name__ == "__main__":
    try:
        hash_to_crack =  sys.argv[1].strip()
        passwords = sys.argv[2]

        for password in open_passwords(passwords):
            print("[*] Trying password: %s" % password)
            if crack_sha256_hash(password, hash_to_crack):
                print("[+] Password found: %s" % password)
                sys.exit(SUCCESS)
            else:
                print("[-] Password not found")

    except IndexError:
        print("[-] Usage: %s <hash to crack> <password file>" % sys.argv[0])
        print("[-] Example: %s  008c7... hashes.txt" % sys.argv[0]) 
        sys.exit(FAIL)
    except Exception as exception:
        print("[-] An exception occured %s" % exception)
        print("[-] The Hash Cracking attack was not successful.")
        sys.exit(FAIL)     

# 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
# /usr/share/wordlists/rockyou.txt