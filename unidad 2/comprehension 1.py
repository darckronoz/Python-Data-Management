#Lists, Dictionaries and Set Comprehensions

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#simple list1 comprehension.
a = [x for x in list1]

print(a)

b = [x*2 for x in list1]

print(b)

c = [x for x in list1 if x < 4]

print(c)

d = [x for x in list1 if x >= 4 if x%2 == 0]

print(d)