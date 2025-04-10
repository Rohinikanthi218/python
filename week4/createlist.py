def createlist(l,n):
    for i in range(n):
        temp=int(input("enter value:"))
        l.append(temp)
    return l
        
l1=[]
l2=[]
l3=[]
n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
n3=int(input("Enter n3"))
l1=createlist(l1,n1)
print(l1)
l2=createlist(l2,n2)
print(l2)
l3=createlist(l3,n3)
print(l3)
