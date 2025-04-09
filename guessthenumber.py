# GUESS THE NUMBER GAME
import random
import time
lucky_num = random.randint(1,100)
print(60*"-")
print("GUESS THE NUMBER??".center(60," "))
print(60*"-")
print()
print("Guess a number from 1 to 100.")
print("You have 5 lives to guess the correct number.")
print("THE GAME STARTS IN :")
for i in range (3,0,-1):
    print(i)
    time.sleep(1)
# lives = 5
for i in range (4,-1,-1) :
    user_num = int(input("Enter a number :"))
    if user_num not in range(1,101):
        print("Invalid number, Enter a valid number!!")
        continue
    
    if (user_num == lucky_num) :
        print("CONGRATULATIONS!!!!")
        print("YOU WIN :) ")
        print("You have guessed the correct number")
        break
    elif (user_num < lucky_num) :
        print("Your number is less than the Lucky number")
    else :
        print("Your number is greater than the Lucky number")
    remaining_lives = i
    if remaining_lives > 0 :
        print(f"Remaining Lives : {remaining_lives}")
    else :
        print("YOUR CHANCES ARE OVER.")
        print("YOU LOSE :( ")
        print(f"The Lucky Number was : {lucky_num}")