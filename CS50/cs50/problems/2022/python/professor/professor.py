import random
def main():
    k=get_level()
    score=0
    time_generate=10
    while True:
        if time_generate==0:
            print("Score:",score)
            break
        if generate_integer(k):
            score+=1
            time_generate-=1
        else:
            continue
def get_level():
    while True:
        try:
            lev=int(input("Level:"))
            if lev<0 or lev>1:
                continue
            return lev
        except:
            continue
def generate_integer(level):
    cor=0
    x=random.randint(1,10)
    y=random.randint(1,10)
    while True:
        print(x,'+',y,'=',end='')
        n=int(input(""))
        if n==x+y:
            return True
        else:
            cor+=1
            if cor==3:
                print(x,'+',y,'=',x+y)
                return True
            print("EEE")
            continue



if __name__ == "__main__":
    main()