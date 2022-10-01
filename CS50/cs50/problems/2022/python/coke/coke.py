y=50
coin_list=[25,10,15]
while True:
    print(f"Amount due:{y}")
    x=int(input("Insert Coin:"))

    if x not in coin_list:
        print(f"Amount due:{y}")
        break
    y-=x

    if y==0:
        print(f"Change owed:{y}")
        break
    if y<0:
        print(f"Change owed:{(x-y)-x}")
        break
