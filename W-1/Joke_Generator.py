import random
import time

# List of programming/Python jokes
jokes = [
    "Why do Python programmers wear glasses?\nBecause they can't C.",
    "Why did the programmer quit his job?\nBecause he didn't get arrays.",
    "How many programmers does it take to change a light bulb?\nNone. That's a hardware problem.",
    "What do you call a snake that works for the government?\nA civil serpent (written in Python).",
    "Why do Java developers wear glasses?\nBecause they don’t see sharp.",
    "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
    "Why was the Python function sad?\nBecause it didn't get any arguments.",
    "What do you get when you cross a Python and a C++ program?\nA snake that thinks in objects.",
    "Why did the developer go broke?\nBecause he used up all his cache.",
    "What’s a Python programmer’s favorite dance move?\nThe 'while' loop!"
]

def show_random_joke():
    joke = random.choice(jokes)
    print("🃏 Here's your Python-flavored joke of the day:\n")
    time.sleep(1)
    print(joke)
    print("\n😂 Hope that made you smile!")

if __name__ == "__main__":
    show_random_joke()