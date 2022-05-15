# For loop
print ("my name is")
for i in range(5): 
   print("George 5 times (" +str(i) + ")")

# While loop
print ("my name is")
i = 0
while i < 5:
   print("George 5 times (" +str(i) + ")")
   i = i + 1

# The range function can be used to set the start and end intergers 
for i in range(12, 16):
   print (i)

# It can also be used to increase the amout of steps inbetween iterations
for i in range(0, 10, 2):
   print (i)

# You can also use negative numbers 
for i in range(5, -3, -1):
   print (i)

# Importing modules 
import random 
for i in range(5):
   print (random.randint(1,10))

# You can also use "from import", alowwing you to import ceritan moduals from a library 


# Ending a program early

# import sys 

# while True:
#    print('Type exit to exit.')
#    response = input()  # map user input to response variable 
#    if response == 'exit':
#       sys.exit()
#    print("you types in " + response + " .")


# Guess the number 
import random


secretNumber = random.randint(1,20) # create a car with the secret numeber
print("I am thinking of a number between 1 and 20")

## Ask the player to guess 6 times 
for guessesTaken in range(1, 7): # this foor loop adds a 
   print("take a guess")
   guess = int(input())

   if guess < secretNumber:
      print("Your guess is too low")
      print("you have " + str(str() - str(guessesTaken)) + " left")
   if guess > secretNumber:
      print("Your guess is too high")
      print("you have " + str(str(range) - str(guessesTaken)) + " left")
   else: 
      break  # this triggers when the guess is correct

if guess == secretNumber: 
   print("you have guessed the correct number in" + str(guessesTaken) + "guesses")
else: 
   print("You ran out of guesses, the number i was thinking of was " + str(secretNumber))