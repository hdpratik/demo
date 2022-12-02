def binary_search(list1,key):
    low = 0
    high = n - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list1[mid] < key:
            low = mid + 1
        elif list1[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1
n= int(input("Enter Number of elements:"))
list1=[]
for i in range(n):
    num=int(input("Enter Number:"))
    list1.append(num)
key=int(input("Enter Searching Element:"))
res=binary_search(list1,key)
if res != -1:
    print("Element is present at index",res)
else:
    print("Element is not present in list1")
print("Print All Present elements:",list1)