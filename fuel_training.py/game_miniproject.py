
import random
number=random.randint(1,10)
score =0
while True:
    guess=int(input("enter the number between 1 to 10: "))
    print(score)

    if guess == number:
        print("you are win")
        score += 1
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
    



