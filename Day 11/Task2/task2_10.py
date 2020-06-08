#Write a program that asks five times to guess the lucky number.
#The program asks for five guesses (no matter whether the correct number was guessed or not).
# If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.

lucky_number=7
counter=0
while(counter<5):
    number=input("Guess the lucky number:")
    if (int(number)==lucky_number):
        print ("Good Guess!")
    elif (int(number)!=lucky_number):
        print("Try again!")

    counter+=1
print ("Game Over!")