#Realizar una funcion que reciba como parámetro la lista de los empleados. Mostrar la información
#de los empleados con el siguiente formato:
#formato 1: -> function formatListOne [x] Done
#empleado -- 1
#luis
#20
#55.6

#formato 2: -> function formatListTwo
#nombre empleado: Luis, Edad: 20, Peso: 55.6

#formato 3: -> function formatListThree
#Empleado_1:Luis, Edad: 20, Peso: 55.6

from re import S


class employees:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

employeesList = []
employeesList.append(employees('Lucia', 30, 65.8))
employeesList.append(employees('Pedro', 18, 60))
employeesList.append(employees('Luis', 20, 55.6))

# -> this uses pop so it empty the list xd *FIXEDnot.-.*
def formatListOne(auxlist):
    index = 1
    while(len(auxlist) > 0):
        employ = auxlist.pop()
        print('empleado --', index)
        print(employ.name)
        print(employ.age)
        print(employ.weight)
        index+=1

#formatListOne(employeesList)

def formatListTwo(xlist):
    for i in range(len(xlist)):
        print('nombre empleado:', xlist[i].name, ', Edad:', xlist[i].age, ', Peso:', xlist[i].weight)

formatListTwo(employeesList)

def formatListThree(xlist):
    index = 1
    while(index <= len(xlist)):
        print('Empleado_',index,':', xlist[index-1].name,', Edad:',xlist[index-1].age,', Peso:',xlist[index-1].weight)
        index+=1

formatListThree(employeesList)