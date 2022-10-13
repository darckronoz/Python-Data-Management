#create a comprehension list with the vowels of the phrase "Tunja tiene mucha altitud"

phrase = "Tunja tiene mucha altitud"
vowels = ['a', 'e', 'i', 'o', 'u']
l = [x for x in phrase if x in vowels]

la = [x for x in phrase if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' ]

le = [x for x in phrase if ord(x) == 97 or ord(x) == 101 or ord(x) == 105 or ord(x) == 111 or ord(x) == 117]

print(l)
print(la)
print(le)
