numbers=['1','2','3','4','5','6','7','8','9']
space=[',','.','/',' ','%','#','*','+','=','!','@','$','^','&','?','_']
def main():
    plates=str(input("Plate: "))
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")
def is_valid(n):
    z=len(n)
    if len(n)>6 or len(n)<2:
        return False
    count=0
    for i in range(len(n)):
        if 'A'<=n[i]<='Z' or n[i] in numbers or n[z-1] =='0':
            count+=1
        elif n[i] in numbers and n[z-1] not in numbers or n[0]=='0':
            return False
        elif n[i] in space or n[i]=='0':
            count-=1
    if count==len(n):
        return True
    else:
        print(count)
        return False

main()