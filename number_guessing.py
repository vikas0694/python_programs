print("welcome to the number guessing game")
x = input("guess the number:")
x = int(x)

if(x==5):
    print("you won the game")

else:
    if(x<5):
        print("too low")
    if(x>5):
        print("too high")
    print("you loose")