import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #a,b,c,d=ip.split('.')
    #ips=int(a)+'.'+int(b)+'.'+int(c)+'.'+int(d)
    if re.search(r"^([0-2])([0-5])?([0-5])?\.([0-2])?([0-5])?([0-5])?\.([0-2])?([0-5])?([0-5])?\.([0-2])?([0-5])?([0-5])?$",ip):
        return True
    else:
        return False
if __name__ == "__main__":
    main()