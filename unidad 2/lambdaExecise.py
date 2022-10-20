
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