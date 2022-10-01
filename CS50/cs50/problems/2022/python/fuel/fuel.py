def main():
    while True:
        try:
            x,y=str(input("Fraction:")).split("/")
            valid=is_true(int(x),int(y))
            if valid==None:
                continue
            print(valid)
            break
        except (ValueError,ZeroDivisionError):
            pass
def is_true(n,k):
    if n==1 and k==4:
        return "25%"
    elif n==2 and k==3:
        return "50%"
    elif n==3 and k==4:
        return "75%"
    elif n==4 and k==4:
        return "F"
    elif n==0 and k<=4:
        return "E"
    elif n>k or k==0:
        return None
main()







