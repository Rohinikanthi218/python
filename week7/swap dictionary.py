d={}
a={}
size=int(input("enter size:"))
for i in range(size):
    key=int(input("enter key:"))
    value=input("enter value:")
    d[key]=value
    a[value]=key
print(d)
print(a)
