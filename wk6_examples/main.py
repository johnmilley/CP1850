
# main() Example
# How we should set up our programs to run as modules and scripts/programs
# More info: https://realpython.com/python-main-function/


import random

def random_zen():
    """
    Randomly slects one of the lines from the zen of python
    """
    # To see the full Zen of Python, write 'import this' in a Python interpreter.
    zen = [
        "Beautiful is better than ugly.",
        "Explicit is better than implicit."
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts.",
        "Special cases aren't special enough to break the rules.",
        "Although practicality beats purity.",
        "Errors should never pass silently.",
        "Unless explicitly silenced.",
        "In the face of ambiguity, refuse the temptation to guess.",
        "There should be one-- and preferably only one --obvious way to do it. \
            Although that way may not be obvious at first unless you're Dutch.",
        "Now is better than never.",
        "Although never is often better than right now.",
        "If the implementation is hard to explain, it's a bad idea.",
        "If the implementation is easy to explain, it may be a good idea.",
        "Namespaces are one honking great idea -- let's do more of those!"
    ]
    print(zen[random.randint(0, len(zen) - 1)]) # generates random num: 0 -> 1 less than the length of the list

def main():
    # this is where the program starts
    random_zen()

# The conditional below is True if you are running this program from 
# VSCode/terminal/etc. If file is imported into another python program, 
# then it's False. Therefore, if we import this file, main() will not be run.
if __name__ == "__main__": 
    main()

# Uncomment the line below to see the value of __name__ when run
# What is the value when imported?

# print(__name__)