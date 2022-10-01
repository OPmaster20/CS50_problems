import sys
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")

sys.argv[1].lstrip()
length=len(sys.argv[1])
if sys.argv[1].startswith('y',length-1):
    try:
        with open(sys.argv[1],'r') as file:
            count=0
            for line in file:
                count+=1
        print(count)
    except:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")


