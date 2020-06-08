#11. In the previous question, insert “break” after the “Good guess!” print statement.
# “break” will terminate the while loop so that users do not have to continue guessing
# after they found the number. If the user does not guess the number at all,
# print “Sorry but that was not very successful”.

lucky_number=7
counter=0
while(counter<5):
    number=input("Guess the lucky number:")
    if (int(number)==lucky_number):
        print ("Good Guess!")
        break
    elif (int(number)!=lucky_number):
        if (counter<4):
            print("Try again!")
        else:
            print ("Sorry but that was not very successful")
    counter+=1