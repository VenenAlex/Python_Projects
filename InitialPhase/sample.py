import random
name = input("Enter your name : ")
print(f"Hello {name}, Have a nice day!!")
print(f"The length of your name is : {len(name)}")
random_num = random.randint(1,10)
guess = input("Guess a number between 1 - 10 : ")
if (guess==random_num):
    print(f"You guessed the correct number!!")
else:
    print(f"Wrong!!, The correct number was {random_num}")