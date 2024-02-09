import random

def guess_the_number():
    number = random.randint(1, 20)
    attempts = 0
    
    print("Hello Stranger, I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess."))
            attempts += 1
            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                print("Good job, KBTU! You guessed my number {} in {} guesses!".format(number, attempts))
                break
        except ValueError:
            print("Sorry, please write a whole number")