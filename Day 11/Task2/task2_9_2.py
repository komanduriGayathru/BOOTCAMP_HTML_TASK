# Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

lucky_number=7
while (True):
    answer=input("Do you want to continue guessing:")
    if (answer=="no"):
        break
    else:
        number=input("Guess the lucky number:")
        if (int(number)==lucky_number):
            break
