def credit(balance,Balance):
    Balance=Balance+balance
    print(Balance)
    return Balance
    
def debit(balance,Balance):
    Balance=Balance-balance
    print(Balance)
    return Balance
    
def check_balance(Balance):
    print("current balance",Balance)
    
    
    
    
    
Balance=0
Balance=credit(1500,Balance)
Balance=debit(1400,Balance)
Balance=check_balance(Balance)
