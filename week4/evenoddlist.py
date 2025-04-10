def createlist(l,n):
    l=[]
    for i in range(n):
        temp=int(input("enter value:"))
        l.append(temp)
    return l


def esum(l):
    esum=0
    for i in range(len(l)):
        if(i%2==0):
            esum+=l[i]
    return esum
    
    
def osum(l):
    osum=0
    for i in range(len(l)):
        if(i%2!=0):
            osum+=l[i]
    return osum
    
        
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

es1=esum(l1)
print(es1)
es2=esum(l2)
print(es2)
es3=esum(l3)
print(es3)

os1=osum(l1)
print(os1)
os2=osum(l2)
print(os2)
os3=osum(l3)
print(os3)
