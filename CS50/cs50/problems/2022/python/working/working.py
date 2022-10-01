import re
import sys


def main():
    print(convert(input("Hours: ")))

#9 AM to 5 PM
#9:00 AM to 5:00 PM
#10 PM to 8 AM
def convert(s):
        if re.search(r"^([0-9])([0-9])?[ ]([A-Z][A-Z])[ ]to[ ]([0-9])([0-9])?[ ]([A-Z][A-Z])$",s):
            match=re.search(r"^([0-9])([0-9])?[ ]([A-Z][A-Z])[ ]to[ ]([0-9])([0-9])?[ ]([A-Z][A-Z])$",s)
                #print(match.group(2))
            if match.group(3)=='AM' and match.group(6)=='PM' and match.group(2)==None:
                return f"{int(match.group(1)):02}:{0:02} to {int(match.group(4))+12:02}:{0:02}"
            elif match.group(3)=='PM' and match.group(6)=='AM' and match.group(2)==None:
                return f"{int(match.group(1))+12:02}:{0:02} to {int(match.group(4)):02}:{0:02}"
            else:
                return f"{int(match.group(1))+12+10-1}:{0:02} to {int(match.group(4)):02}:{0:02}"

        if re.search(r"^([0-9])([0-9])?[:]([0-5][0-9])[ ]([A-Z][A-Z])[ ]to[ ]([0-9])([0-9])?[:]([0-5][0-9])[ ]([A-Z][A-Z])$",s):
            other=re.search(r"^([0-9])([0-9])?[:]([0-5][0-9])[ ]([A-Z][A-Z])[ ]to[ ]([0-9])([0-9])?[:]([0-5][0-9])[ ]([A-Z][A-Z])$",s)
                #print(other.group(1))
            if other.group(4)=='AM' and other.group(8)=='PM' and other.group(2)==None:
                    return f"{int(other.group(1)):02}:{int(other.group(3)):02} to {int(other.group(5))+12:02}:{int(other.group(7)):02}"
            elif other.group(4)=='PM' and other.group(8)=='AM' and other.group(2)==None:
                    return f"{int(other.group(1))+12:02}:{int(other.group(3)):02} to {int(other.group(5)):02}:{int(other.group(7)):02}"
            else:
                return f"{int(other.group(1))+12+10-1:02}:{int(other.group(3)):02} to {int(other.group(5)):02}:{int(other.group(7)):02}"



if __name__ == "__main__":
    main()