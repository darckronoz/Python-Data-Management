import json
with open('Unidad1_Reto.json', 'r') as file:
    data = json.load(file)


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




