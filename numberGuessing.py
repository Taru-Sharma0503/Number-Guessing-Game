import random
a=random.randint(1,100)
maxLimit=20
count=0
print("Welcome to the Number Guessing Game!")
for i in range(maxLimit):
    b=int(input("Enter your guess between 1 to 100: "))
    if(a>b):
        print("Your guess is low")
    elif(a<b):
        print("Your guess is high")
    else:
        print("Congratulations! You guessed it right.")
        count=1
        break
if count==0:
    print("Maximum Limit(20) reached. The number to guess was : ",a)