def printelements(elements):
    for i in elements:
        print(i,end=" ")
limit=int(input("Enter limit: "))
for i in range(limit):
        ele=int(input("Enter elements: "))
        elements.append(ele)
printelements(elements)
