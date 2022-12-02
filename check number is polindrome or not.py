n=int(input("enter any number="))
s=0
r=0
t=n
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
if t==s:
    print("number",s,"is polindrome")
else:
    print("number",s,"is Not polindrome")