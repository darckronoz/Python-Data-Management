#Lists, Dictionaries and Set Comprehensions

from operator import indexOf


list1 = [1, 2, 3, 4]
list1_rev = [4, 3, 2, 1]

#with nested loop

g = [(x, y) for x in list1 for y in list1_rev]

print(g)

#generate a comprehension list of numbers from 0 to 50 primes and not multiples of 5
l = [x for x in range(50)]

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    y = int(n**0.5)
    x = 5
    while x <= y:
        if n%x == 0: return False
        if n%(x+2) == 0: return False
        x+=6
    return True

thelist = [x for x in l if x%5 != 0 if isPrime(x) == True]

print(thelist)

#Dictionaries Comprehension

dict1 = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5 }

double_dct1 = {k:v*2 for (k,v) in  dict1.items()} #each value 2 times
print(double_dct1)

#comprehension matrix

m = [[x for x in range(4)] for y in range(4)]
print(m)

#comprehension set

words = ['portero', 'curul', 'jelou', 'dracula', 'hallowen', 'aaaaaaaa']
long_words = set(len(x) for x in words)
print(long_words)

#dictionary from mylist, with each element and the index
myList = ['a', 'as', 'bat', 'car', 'dove', 'python']
indexs = [myList.index(x) for x in myList]
dictlist={k:v for k, v in zip(myList, indexs)}
print(dictlist)

#tuples comprehension
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)

myDblList=[[x for x in tup] for tup in some_tuples]
print(myDblList)






