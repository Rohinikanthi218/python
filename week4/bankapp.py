def credit(Balance,transactions,amount):
    Balance=Balance+amount
    transactions.append(amount)
    return Balance,transactions
    
def debit(Balance,transactions,amount):
    if Balance<=amount:
        print("Insufficient")
    Balance=Balance-amount
    transactions.append(-amount)
    print(Balance)
    return Balance,transactions
    
def check_balance(Balance):
    print("current balance",Balance)
    
    
def show_transactions(transactions):
    print("transactions",transactions)
    
    

    
Balance=0
transactions=[]
while(True):
    print("credit")
    print("debit")
    print("show balance")
    print("last 5 transactions")
    choice=int(input("enter choice: "))
    if choice==1:
        amount=int(input("enter amount"))
        Balance,transactions=credit(Balance,transactions,amount)
    elif choice==2:
        amount=int(input("enter amount"))
        Balance,transactions=debit(Balance,transactions,amount)
    elif choice==3:
        check_balance(Balance)
    else:
        show_transactions(transactions)
