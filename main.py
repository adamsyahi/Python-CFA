import random


genres = ['rock', 'pop', 'hip hop', 'jazz', 'country', 'classical', 'electronic']


def choose_genre():
    random_genre = random.choice(genres)
    return random_genre


def play_game():
    print("Welcome to adam Music Genre Guessing Game!")
    print("I'm thinking of a genre... can you guess it?")
    random_genre = choose_genre()
    attempts = 4
    
    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        
        if guess == random_genre:
            print("Congratulations! You guessed it right!")
            break
        else:
            attempts -= 1
            print("Wrong guess! You have", attempts, "more attempts left.")
    
    if attempts == 0:
        print("Game loss! The correct genre was", random_genre)
    

play_game()