#lambda functions

#example multiply by 2 a number (lambda function)
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
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)

#lambda as a parameter

ints = [4, 0, 1, 5, 6, 45, 23, 12, 34, 56, 78, 90, 9, 7, 5, 23, 13, 35, 67, 84]

def apply_to_list(listx, function):
    return [function(x) for x in listx]

print(apply_to_list(ints, lambda x: "even" if x%2 == 0 else "odd"))

#to do: aporte revisar taller ultima parte
