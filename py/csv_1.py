import csv
with open("C:\\Users\\gs400\\Desktop\\sam.csv",'a') as f:
    re=csv.writer(f)
    re.writerow(['\n6','sam','mad'])
with open("C:\\Users\\gs400\\Desktop\\sam.csv") as s:
    a=csv.reader(s)
    for i in a:
        print(i)
