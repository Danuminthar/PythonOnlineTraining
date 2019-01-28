def cmp(l1,l2):
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            return 0
    return 1
list=["arkar","minthar","danu","kyaw",1999,444]
print(list)

arkarDANU=["akk","dnmt",11,33]
print(arkarDANU)
"""
list[3]="arkarkyaw"
ddd=print(list)
akk=print(list[2])
print(akk)

print(list)
print(len(list))

if "arkar" in list:
    print("arkar is in list")
    print()
else:
    print("arkar is not in list")
    print()

for ele in list:
    print (ele,end=" " )
print()
for i in range(0,5):
    print(i,end="-")
    print(list[i])

print(list[-3])
print("\n")
print(list[1:])
list.append("myatkooo")
print(list)
print()"""

if cmp(list,list):
    print("same list")
else:
    print("different list")

print(cmp(list,arkarDANU))
print(arkarDANU)
print(list)
