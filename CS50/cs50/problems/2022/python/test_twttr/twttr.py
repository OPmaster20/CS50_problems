def main():
    x=str(input("Input:"))
    y=shorten(x)
    print('Output:',end='')
    print(y)
def shorten(word):
    omit=['A','E','I','O','U','a','e','i','o','u']
    for i in word:
        if i not in omit:
            word=word.strip(i)
    for i in word:
        if i not in omit:
            word=word.strip(i)
    return word
if __name__ == "__main__":
    main()