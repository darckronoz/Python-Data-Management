#lambda functions

#example multiply by 2 a number (lambda function)
from calendar import prmonth
from curses import keyname
from optparse import Values


def mult2(n): return n*2 #example normal function in one line
mult2l = lambda num : num*2 #example lambda function
print(mult2(4))
print(mult2l(4))

#function as a parameter.

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    #storing the function in a variable
    greeting = func(f"Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)

#lambda as a parameter

ints = [4, 0, 1, 5, 6, 45, 23, 12, 34, 56, 78, 90, 9, 7, 5, 23, 13, 35, 67, 84]

def apply_to_list(listx, function):
    return [function(x) for x in listx]

print(apply_to_list(ints, lambda x: "even" if x%2 == 0 else "odd"))

#EXERCISE
#to do: aporte revisar taller ultima parte

#Lambda with arguments

sampleO = lambda *args: sum(args) #with one it recieves a list of variables as arguments.
print(sampleO(1, 4, 5, 6, 7))

sampleDicts = lambda x, **args: print("si:", args.get(x)) #with two it recieves iterables.
#you can use different types of arguments in one function
sampleDicts('one', one='eluno', tre='sitres', dos='eldos')

#decorators :0 this enable a function to implement the behavior of another function like so:

def some_decorator(fuwu):
    def wraps(*args):
        print(f"Calling function '{fuwu.__name__}'")
        return fuwu(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")

decorated_function('argumentos de la segunda función')

# Defining a decorator

def trace(f):

    def wrap(*args, **kwargs):

        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")

        return f(*args, **kwargs)


    return wrap


# Applying decorator to a function

@trace

def add_two(x):

    return x + 2


# Calling the decorated function

add_two(3)


# Applying decorator to a lambda

print((trace(lambda x: x ** 2))(3))