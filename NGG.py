import random
print("Number Guessing Game")
z=True

def ngg(h,a,n):
    r=random.randint(1,h)
    for i in range(a):
        g=int(input("\nEnter your guess: "))
        if g==r:
            print("Congrats ",n,", you found the correct number in ",i+1,"attempt(s)")
            break
        elif i==a-1:
            print("\nOut of attempts : (\nChosen number is ",r)
        elif g>r:
            print("guessed number is higher than the chosen number")
        elif g<r:
            print("guessed number is lower than the chosen number")
            
print('''\n\tRules:
1.The objective of the game is to guess the secret number chosen by the host
2.The game has 3 different level
3.The game is meant to be fun and friendly''')
n=input("\nEnter your name: ")

while z==True:
    print("\nE for Easy(1-10)\nM for Medium(1-100)\nH for Hard(1-500)")
    l=str(input("Select level: "))
    
    if l=="H"or l=="h":
        print("\nLevel: Hard\nRange: 1-500\nAttempts: 15")
        ngg(500,15,n)
    elif l=="E"or l=="e":
        print("\nLevel: Easy\nRange: 1-10\nAttempts: 3")
        ngg(10,3,n)
    elif l=="M"or l=="m":
        print("\nLevel: Medium\nRange: 1-100\nAttempts: 10")
        ngg(100,10,n)

    o=input("\nDo you want to play again?\nYes = Y\nNo =N\n")
    
    if o=="Y"or o=="y":
        print("\nFuiyoh!!!")
        z=True
    elif o=="N"or o=="n":
        print("\nThanks for playing the game : )")
        z=False

