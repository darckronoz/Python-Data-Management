#definition of a dictionary

juan = {
    'nombre': 'lucho',
    'edad': 21,
    'modelo': 2022,
    'sexo': 'no',
    'color': 'negro'
}

#add element to a dictionary

juan ['conduccion'] = False

#print(juan)
#print(juan.keys()) #obtain all the keys
#print(juan.values()) #obtain all the values

#print(juan)
oscar = juan.copy()
juan.clear()
#print(oscar)
lucho = dict.fromkeys(oscar) # create a dictionary with the keys of other dictionary, values none by default
#print(lucho)
#print(oscar.items())
clave2 = oscar.setdefault('altura', '6xd')
#print(clave2)
#print(oscar)

#for k,v in oscar.items():
    #print(k,':',v)

#enumerate

my_list = ['apple', 'banana', 'grapes', 'pear']
#for c, value in enumerate(my_list, 1):
    #print(c, value)

#for i in my_list:
    #print(my_list.index(i)+1, i)

#zip -> iterator of collections, pairs the elements on each list

keysList = ['name', 'age', 'weight', 'sex']
values = ['giovanny', 22, 69, 'alot']
dicttest = {}

for k, v in zip(keysList, values):
    dicttest[k] = v

#print(dicttest)

##exercise: create a dictionary from a list, classifing the words that starts with the same letter.
# example apple, bar, bat, atom, book, cat -> a: apple atom, b: bat, bar, c: car.---------------->

words = ['hola', 'me', 'llamo', 'frailejon', 'ernesto', 'perez', 'halo 2', 'mollejas', 'lluvia', 'federico', 'equino', 'pesos']
#h, m, l, f, e, p

letters = set()

for i in words:
    letters.add(i[0])

#separate the words
auxWords = []
for i in letters:
    aux = []
    for w in words:
        if w[0] == i:
            aux.append(w)
    auxWords.append(aux)

salida = dict()

for k, v in zip(letters, auxWords):
    salida[k] = v

print(salida)

