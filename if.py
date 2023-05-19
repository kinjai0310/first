import random
num = random.randint(1,10)
guess_number=int(input("guess a number:"))
if guess_number==num:
    print("you are right at first time")
elif guess_number>=num:
    guess_number = int(input("guess a smaller number:"))
    if guess_number==num:
        print("you are right at second time")
    elif guess_number >= num:
        guess_number = int(input("guess a smaller number:"))
        if guess_number == num:
            print("you are right at third time")
        else:
            print (f"correct answer: {num}")
    elif guess_number <= num:
        guess_number = int(input("guess a larger number:"))
        if guess_number == num:
            print("you are right at third time")
        else:
            print (f"correct answer: {num}")
elif guess_number<=num:
    guess_number = int(input("guess a larger number:"))
    if guess_number==num:
        print("you are right at second time")
    elif guess_number >= num:
        guess_number = int(input("guess a smaller number:"))
        if guess_number == num:
            print("you are right at third time")
        else:
            print (f"correct answer: {num}")
    elif guess_number <= num:
        guess_number = int(input("guess a larger number:"))
        if guess_number == num:
            print("you are right at third time")
        else:
            print (f"correct answer: {num}")



