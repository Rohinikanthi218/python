Q) Game
import random
n=random.randint(1,100)
count=5
while (True):
    x=int(input("enter the number:"))
    if x < n :
        print("Too low")
    elif x > n :
        print("Too high")
    else :    
        print("Congratulations! You got the correct number")
        break;
        count = count - 1
print("You lost!")        
