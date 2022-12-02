n=int(input("Enter number of values:"))
list1=[]
for i in range (0,n):
    a=int(input("Enteger:"))
    list1.append(a)
print("Circulating the elements of list",list1)
no_of_circulate=int(input("Enter Number of circulating  terms:"))
for i in range(0,no_of_circulate):
    a=list1.pop(0)
    list1.append(a)
    print(list1)