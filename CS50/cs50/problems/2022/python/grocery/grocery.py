d={}
i=1
while True:
    try:
        item=input()
        if item not in d:
            d[item]=i
        else:
            d[item]=i+1
    except EOFError:
        d_sort=sorted(d.items(),key=lambda x:x[0])
        d_sort=dict(d_sort)
        for key in d_sort:
            print(d[key],key.upper())
        print('\n',end='')
        break