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

class employees:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

employeesList = []
employeesList.append(employees('Lucia', 30, 65.8))
employeesList.append(employees('Pedro', 18, 60))
employeesList.append(employees('Luis', 20, 55.6))


def formatListOne(xlist):
    index = 1
    while(len(xlist) > 0):
        employ = xlist.pop()
        print('empleado --', index)
        print(employ.name)
        print(employ.age)
        print(employ.weight)
        index+=1

formatListOne(employeesList)

#def formatListTwo(xlist):


#def formatListThree(xlist):