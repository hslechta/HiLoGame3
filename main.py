from random import randint


def choose_number():
    target = randint(1, 100)
    return target


def print_intro():
    print("Welcome to this hi-lo game!")
    print("The secret number is between 1-100 inclusive.")
    print("You get 10 guesses.")
    print()


def play(target):
    total_guesses = 0
    print("The computer is ready... Are you? (y/n)")
    response = input()
    while response != 'y':
        if response == 'n':
            print("Enter y when ready to begin.")
            response = input()
        else:
            print("Invalid response. Are you ready? (y/n)")
            response = input()
    if response == 'y':
        print("Guess an integer between 1 and 100.")
        guess = input()
        guess = int(guess)
        total_guesses += 1
        while guess != target and total_guesses < 10:
            if guess % 1 != 0:
                print("Integers only. Please guess again.")
                guess = input()
                guess = int(guess)
            elif guess < 1 or guess > 100:
                print("The secret number is between 1 and 100. Please guess again.")
                guess = input()
                guess = int(guess)
            elif guess > target:
                print("Too high. Try again.")
                print("You have " + str(10 - total_guesses) + " guesses left.")
                guess = input()
                guess = int(guess)
                total_guesses += 1
            elif guess < target:
                print("Too low. Try again.")
                print("You have " + str(10 - total_guesses) + " guesses left.")
                guess = input()
                guess = int(guess)
                total_guesses += 1
        if total_guesses == 10:
            print("You ran out of guesses. Too bad!")
        else:
            print("Congratulations! You guessed the secret number!")


def check_play_again():
    print("Would you like to play again? (y/n)")
    response = input()
    while response != 'y':
        if response == 'n':
            print("Thank you for playing! Goodbye!")
            return False
        else:
            print("Invalid response. Are you ready? (y/n)")
            response = input()
    print("Great! The computer will pick a new number between 1-100.")
    print()
    return True


def main():
    run_variable = True
    print_intro()
    while run_variable:
        target = choose_number()
        play(target)
        run_variable = check_play_again()


if __name__ == "__main__":
    main()
