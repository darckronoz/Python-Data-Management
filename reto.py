import json
with open('Unidad1_Reto.json', 'r') as file:
    data = json.load(file)

print()
#create student and subjects dict
student = dict.fromkeys(data[0])
subject = dict.fromkeys(data[0].get('asignaturas')[0])

#nota promedio por asignatura ----------->

#create aux dictionaries and list to do the query
subjects = set()
auxSubjectList = []

#fill set with subjects and list with subjects and scores
for d in data:
    for s in d.get('asignaturas'):
        x = ['','']
        x[0] = s.get('nombre')
        x[1] = s.get('nota')
        subjects.add(s.get('nombre'))
        auxSubjectList.append(x)

#create dictionary of the query
subjectScore = dict()

#gets the mean of a number list
def prom(lists):
    prom = 0
    for i in lists:
        prom+=i
    return prom/len(lists)

#adds to the dictionary the subjects with it's respective score mean.
for s in subjects:
    aux = []
    subjectScore.setdefault(s)
    for a in auxSubjectList:
        if a[0] == s:
            aux.append(a[1])
    subjectScore[s] = prom(aux)

#print nota promedio por asignatura:
print('nota promedio por asignatura')
print(subjectScore)

#nota promedio por estudiante de las asignaturas cursadas(no retiradas) - ordenar por apellido.

noRetiredSubject = []

#fill set with subjects and list with subjects and scores
for d in data:
    aux = ['',[]]
    aux[0] = d.get('apellidos').get('primer_apellido')
    for s in d.get('asignaturas'):
        if s.get('retirada') == 'No':
            aux[1].append(s.get('nota'))
    aux[1] = prom(aux[1])
    noRetiredSubject.append(aux)

#sort by lastname
noRetiredSubject.sort()

#convert to dictionary key(lastname), value(mean score)
finalQuery = dict()
for i in noRetiredSubject:
    finalQuery[i[0]] = i[1]


#final query: promedio notas por estudiante de asignaturas cursadas ordenado por apellidos.
print('promedio de notas por estudiante de asignaturas cursadas ordenado por apellidos.')
print(finalQuery)