import sys
f = open(sys.argv[1],"r+")
dict1 = {}
list1 = []
for line in f:
    list1.append(line.rstrip().split(":"))
for a in list1:
    dict1[a[0]]=a[1]
f.close()
list2=sys.argv[2].split(",")
for i in list2:
    try:
        print(f"Name: {i}, University: {dict1[i]}")
    except:
        print(f"No record of {i} was found!")

