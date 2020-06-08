#9. Read the two parts of the question below: 
# Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 

lucky_number=7
while (True):
    x=input("Guess the lucky number:")
    if (int(x)==lucky_number):
        break
