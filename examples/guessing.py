import random

number = random.randint(1, 101)
guess = None
print "I'm thinking of a number between 1 and 100. Guess what it is!"
while guess != number:
    guess = int(raw_input("Guess a number: "))
    if guess < number:
        print "Too small"
    elif guess > number:
        print "Too large"
    else:
        print "You've guessed it! The number is %d" % number
