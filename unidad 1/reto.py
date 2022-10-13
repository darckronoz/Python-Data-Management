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
print()
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
print()
#Una lista con los estudiantes y el correo institucional correspondiente 
    #Si tiene dos nombres: [Primera letra del primer nombre][primera letra del segundo nombre].[primer apellido][dos ultimos números del documento]
    #Juan Carlos Perez Rubiano 123 = jc.perez23@uptc.edu.co
    #Si tiene un nombres: [Primera letra del primer nombre][primera letra del primer apellido].[segundo apellido][dos ultimos números del documento]
    #Luis Ramirez Moreno 6879 = lr.moreno79@uptc.edu.co

#Obtain the data neded firstname lastname and id.

dataStudents = []
for d in data:
    aux = ['','','',''] #0 = firstname 1 = secondname 2=lastname 3=id
    aux[0] = d.get('nombres').get('primer_nombre')
    if len(d.get('nombres')) > 1:
        aux[1] = d.get('nombres').get('segundo_nombre')
        aux[2] = d.get('apellidos').get('primer_apellido')
        aux[3] = str(d.get('documento'))
    else:
        aux[1] = d.get('apellidos').get('primer_apellido')
        aux[2] = d.get('apellidos').get('segundo_apellido')
        aux[3] = str(d.get('documento'))
    dataStudents.append(aux)

#built the mail and store it on a list.
studentsMail = []
for s in dataStudents:
    aux = []
    aux.append(s[0] + ' ' + s[1] + ' ' +  s[2])
    aux.append(s[0][0].lower()+s[1][0].lower()+'.'+s[2].lower()+str(s[3])[-2:]+'@uptc.edu.co')
    studentsMail.append(aux)

#lista con los estudiantes y su correo institucional con las indicaciones dadas.
print('estudiantes con correo institucional.')
print(studentsMail)