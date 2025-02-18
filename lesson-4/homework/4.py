import random
play_again = True
while play_again:
    number_to_guess = random.randint(1, 100)
    attempts = 10
    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("You guessed it right!")
            break   
        attempts -= 1
    if attempts == 0:
        print("You lost. Want to play again?")
    play_again_input = input("Do you want to play again? (Y/YES/y/yes/ok): ").strip().lower()
    if play_again_input in ['y', 'yes', 'ok']:
        play_again = True
    else:
        play_again = False
        print("Thanks for playing!")
