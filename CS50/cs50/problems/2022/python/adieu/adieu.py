import inflect
p = inflect.engine()
while True:
    try:
        x=str(input("Name:"))
    except EOFError:
        print('\n',end='')
        print("Adieu","adieu","to ",x,sep=',')
        break
