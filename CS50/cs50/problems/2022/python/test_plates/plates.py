def main():
    plates=str(input("Plate: "))
    result=is_valid(plates)
    print(result)
def is_valid(n):
    numbers=['1','2','3','4','5','6','7','8','9']
    space=[',','.','/',' ','%','#','*','+','=','!','@','$','^','&','?','_']
    z=len(n)
    if len(n)>6 or len(n)<2:
        return "invalid"
    count=0
    for i in range(len(n)):
        if 'A'<=n[i]<='Z' or n[i] in numbers or n[z-1] =='0':
            count+=1
        elif n[i] in numbers and n[z-1] not in numbers or n[0]=='0':
            return "Invalid"
        elif n[i] in space or n[i]=='0':
            count-=1
    if count==len(n):
        return "Valid"
    else:
        print(count)
        return "Invalid"
if __name__=='__main__':
    main()