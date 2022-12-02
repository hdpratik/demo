n=int(input("enter any number="))
s=0
c=0
while(n>0):
    s=n%10
    c=c+1
    n=n//10

print("total numbers of digit=",c)