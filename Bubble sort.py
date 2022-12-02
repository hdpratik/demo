
n = int(input("Enter number of Element:"))
print("Enter Elements:")
arr=[]
for i in range(n):
    pratik=int(input())
    arr.append(pratik)
print("Before sorting elements is:")
for i in range(n):
    print(arr[i],end=",")
print()
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted Elements is:")
for j in range(n):
    print("%d" % arr[j],end=",")
