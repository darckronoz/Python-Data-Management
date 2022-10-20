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

#dictionary from mylist, with each element and the index
myList = ['a', 'as', 'bat', 'car', 'dove', 'python']
indexs = [myList.index(x) for x in myList]
dictlist={k:v for k, v in zip(myList, indexs)}
print(dictlist)

#create a comprehension list with the vowels of the phrase "Tunja tiene mucha altitud"

phrase = "Tunja tiene mucha altitud"
vowels = ['a', 'e', 'i', 'o', 'u']
l = [x for x in phrase if x in vowels]

la = [x for x in phrase if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' ]

le = [x for x in phrase if ord(x) == 97 or ord(x) == 101 or ord(x) == 105 or ord(x) == 111 or ord(x) == 117]

print(l)
print(la)
print(le)
