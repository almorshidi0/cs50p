import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

octets = []

def validate(ip):
    regex = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    matches = re.search(regex, ip)
    if matches:
        octets = matches.groups()
    else:
        return False
    for octet in octets:
        octet_value = int(octet)
        if octet_value not in range(0, 256):
            return False
    return True

if __name__ == "__main__":
    main()
