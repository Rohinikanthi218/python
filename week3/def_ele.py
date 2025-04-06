def largest(elements):
    ele=0
    for i in elements:
        ele=max(ele,i)
    return ele
    
def smallest(elements,largeNUM):
    ele=largeNUM
    for i in elements:
        ele=min(ele,i)
    return ele
    
def printelements(elements):
    for i in elements:
        print(i,end=" ")
        
        
elements=[]
limit=int(input("Enter the limit: "))
for i in range(limit):
    ele=int(input("Enter: "))
    elements.append(ele)
    
largeNUM=largest(elements)
smallNum=smallest(elements,largeNUM)
printelements(elements)
print("largest= ",largeNUM)
print("smallest= ",smallNum)
