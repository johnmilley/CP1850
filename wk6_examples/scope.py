# global and local scope - example
# adapted from https://automatetheboringstuff.com/2e/chapter3/

eggs = "over easy" # global variable (seen by entire program)

def breakfast():
    eggs = "runny"  # local
    yesterdays_breakfast()
    print(f"{eggs} eggs")

def yesterdays_breakfast():
    eggs = "boiled" # local
    ham = "sliced"  # local
    print(f"{eggs} eggs and {ham} ham")

def default_breakfast():
    print(eggs) # global eggs (line 7). Note: using global variables inside functions is not encouraged

breakfast()
default_breakfast()