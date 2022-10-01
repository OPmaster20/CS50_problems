x=str(input("Input:"))
omit=['A','E','I','O','U','a','e','i','o','u']
print('Output:',end='')
for i in x:
    if i not in omit:
        print(i,end='')
print('\n')