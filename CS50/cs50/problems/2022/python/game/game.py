import random
while True:
    try:
        n=int(input("Level:"))
        if n<0:
            continue
        else:
            break
    except:
        continue
while True:
    try:
        k=random.randint(1,n)
        v=int(input("Guess:"))
        if v<0:
            continue
        if v>k:
            print("Too large!")
        elif v<k:
            print("Too small1")
        elif v==k:
            print("Just right!")
            break
    except:
        continue