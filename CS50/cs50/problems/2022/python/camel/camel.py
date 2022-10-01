x=str(input("camelCase:"))
for i in range(len(x)):
    if x[i]=='N' and len(x)>5:
        print("_",end='')
    if x[i]=='N' or x[i]=='F' and len(x)>15:
        print("_",end='')
    print(x[i],end='')

print('\n')