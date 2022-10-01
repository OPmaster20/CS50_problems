def main():
    hours,minutes=str(input("What time is it?:")).split(":")
    convert(int(hours),int(minutes))
def convert(x,y):
    if x==7 or x==8 and 0<y>=59:
        print("breakfast time!")
    elif x==12 or x==13 and 0<y>=59:
        print("lunch time!")
    elif x==18 or x==19 and 0<y>=59:
        print("dinner time!")
if __name__=='__main__':
    main()
