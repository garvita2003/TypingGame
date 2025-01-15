import random
import time
from colorama import Fore, Style #pip install colorama

# Prompts
prompts = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a versatile and powerful programming language",
    "Coding is a skill that can change your life",
    "Practice makes perfect",
    "All for one, and one for all.",
    "The only limit is your imagination.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "She sells seashells by the seashore.",
    "A journey of a thousand miles begins with a single step.",
    "Typing fast takes practice and precision.",
    "Always aim for accuracy before speed.",
    "The rain in Spain stays mainly in the plain.",
    "Every cloud has a silver lining.",
    "Better late than never, but never late is better.",
    "Jack and Jill went up the hill to fetch a pail of water.",
    "Success comes to those who work hard and stay consistent.",
    "An apple a day keeps the doctor away.",
    "All work and no play makes Jack a dull boy.",
    "The pen is mightier than the sword.",
    "A picture is worth a thousand words.",
    "Life is what happens when you're busy making other plans.",
    "Good things come to those who wait patiently."
]

def display_prompt(prompt):
    print("Type this: ", prompt, "")
    input("Press ENTER when you are ready!")

def calculate_typing_speed(prompt, start_time, end_time):
    words = len(prompt.split())
    elapsed_time = end_time - start_time
    speed = words / (elapsed_time / 60)
    return speed

def play_typing_game():
    prompt = random.choice(prompts)
    display_prompt(prompt)

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    if user_input == prompt:
        print(Fore.GREEN + "Congratulations! You typed it correctly.")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + "Sorry, there were errors in your typing:")
        for i in range(len(prompt)):
            if user_input[i:i+1] == prompt[i:i+1]:
                print(Fore.GREEN + user_input[i:i+1], end='')
            else:
                print(Fore.RED + user_input[i:i+1], end='')
        print(Style.RESET_ALL)

    typing_speed = calculate_typing_speed(prompt, start_time, end_time)
    print("Your typing speed: {:.2f} words/minute".format(typing_speed))

if __name__ == "__main__":
    while True:
        play_typing_game()
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break