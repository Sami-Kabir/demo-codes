#Number Guessing Game 

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty_level():
    difficulty_level = input("pick a difficulty level between 'easy' and 'hard': " )
    if difficulty_level == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty_level == 'hard':
        return HARD_LEVEL_TURNS
        
    
def check_numbers(user_guess, answer, turns):
    if user_guess < answer:
        print("your guess is too low")
        return turns -1
    elif user_guess > answer:
        print("your guess is too high")
        return turns -1
    else:
        print("your guess is correct")
          
def game():   
  #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
 #   print(f"Pssst, the correct answer is {answer}") 

    turns = set_difficulty_level()
  #Repeat the guessing functionality if they get it wrong.
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
        user_guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_numbers(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != answer:
            print("Guess again.")
            
game()
          