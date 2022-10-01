import csv
import sys
from tabulate import tabulate
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
sys.argv[1].lstrip()
length=len(sys.argv[1])
if sys.argv[1].startswith('v',length-1):
    try:
        with open(sys.argv[1],'r') as file:
            w=csv.DictReader(file)
            #headers=['Regular Pizza','Small','Large']
            headers=[]
            table=[]
            for j in w:
                print(j.keys())
                for i in j.keys():
                    print(i)
                    headers.append(i)
                break
            for n in w:
                table.append([n[headers[0]],n[headers[1]],n[headers[2]]])
            for m in table:
                print(m)
            print(tabulate(table, headers, tablefmt="grid"))
    except:
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")


