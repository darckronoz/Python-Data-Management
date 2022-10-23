
estudiantes = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
#filter all the students that begins with a vowel
print(list(filter(lambda x: x[0].lower() in 'aeiou', estudiantes)))

#another example of filter:
#cheking if a number from a list is even 
thelistxd = [1, 3, 7, 9, 1, 13, 15, 12, 65, 54, 39, 102, 339, 221, 50, 70, 84, 12 ,45 ,78 ,98 ,65 ,32]
checkeven = lambda x: x if x%2 == 0 else None

print(list(filter(checkeven, thelistxd)))