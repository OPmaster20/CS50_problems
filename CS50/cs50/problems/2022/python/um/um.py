import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    #test_case str=re.findall(r".+[u|U]m*",s)
    #test_case str=re.findall(r"\b[u|U]m*",s)
    str=re.findall(r"um(.+)?",s)
    return len(str)


if __name__ == "__main__":
    main()