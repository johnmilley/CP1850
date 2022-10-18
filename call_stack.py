# function stack example
# adapted from https://automatetheboringstuff.com/2e/chapter3/

def a():
    print("a() starts")
    b()
    d()
    print("a() returns")

def b():
    print("b() starts")
    c()
    print("b() returns")

def c():
    print("c() starts")
    print("c() returns")

def d():
    print("d() starts") 
    print("d() returns")

a() # call function a