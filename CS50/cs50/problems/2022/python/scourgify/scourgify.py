import sys
import csv
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
try:
    with open(sys.argv[1],'r') as file:
        w=csv.DictReader(file)
        name=[]
        house=[]
        first=[]
        last=[]

        for row in w:
            #print(row['name'])
            name.append(row['name'])
            house.append(row['house'])
        for p in sorted(name):
            last,first=p.split(',')
            last.append(last)
            first.append(first)
        for i in first:
            print(i)
            #print(f)
    #with open(sys.argv[2],'a') as files:
     #   c=csv.DictWriter(files,fieldname='first','last','house')
      #  for m in c:
       #     c.writerow({'first':first,'last':last,'house':house})





except:
    sys.exit("Could not read invalid_file.csv")