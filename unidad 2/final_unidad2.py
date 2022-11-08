from functools import reduce
#Taller unidad 2

#1. pedidos de libros

from asyncio.windows_events import NULL
from operator import index


pedidos1 = [ ["45", "Nacho Lee, Pedro Cardenas", 5, 32.50],  
            ["87", "Urbanidad de Carreño, Juan Carreño", 4, 60.20],  
            ["72", "Aprenda a jugar dados en dos días, Ana Parra", 4,22.80], 
            ["81", "En Vendedor de Sueños, Benito Hernandez", 4, 15.60]] 

#generar una lista de tuplas con el numero de pedio y total de precio
#cada tupla debe incrementarse en 15 pesos si el valor del pedido es inferior a 80 pesos

salida = list(map((lambda x: (x[0], x[1]+15) if x[1] < 80 else (x[0], x[1])), ((y[0], y[2]*y[3]) for y in pedidos1)))
print('lista de tuplas con numero de pedido y costo total aplicando la restriccion')
print(salida)

#2. pedidos 2

pedidos2 = [ [1, ("45", 3, 12.5),   ("27",15,20.5), ("74", 10, 38.5)],   
            [2, ("45", 10, 12.5),  ("74", 11, 38.5)],  
            [3, ("45", 2, 12.5),  ("27", 1, 20.5)],  
            [4, ("31", 6, 14.0),   ("30",9,27.0),  ("100", 15, 40.5)],  
            [5, ("31", 5, 14.0),   ("30",12,27.0), ("27", 4, 20.5)]] 

def getPrice(pedidosList):
    l = []
    for i in range(len(pedidosList)):
        price = 0
        index = 0
        x = []
        for j in range(len(pedidosList[i])): 
            if j > 0:
                price += pedidosList[i][j][1]*pedidosList[i][j][2]
            else:
                index = pedidosList[i][j]
        x.append(index)
        x.append(price)
        l.append(x)
    
    return l

prices = getPrice(pedidos2)
salida = list(map(lambda x: [x[0], x[1]+15] if x[1] < 80 else [x[0], x[1]], prices))
print('lista de listas con codigo de pedido y valor total de pedido')
print(salida)

#2. pedidos 2 con el uso de reduce.

pedidos2 = [ [1, ("45", 3, 12.5),   ("27",15,20.5), ("74", 10, 38.5)],   
            [2, ("45", 10, 12.5),  ("74", 11, 38.5)],  
            [3, ("45", 2, 12.5),  ("27", 1, 20.5)],  
            [4, ("31", 6, 14.0),   ("30",9,27.0),  ("100", 15, 40.5)],  
            [5, ("31", 5, 14.0),   ("30",12,27.0), ("27", 4, 20.5)]] 

indexs = [x for y in pedidos2 for x in y if type(x) == type(1)]
totales = [reduce(lambda i, j: i[2] + j[2] ,x) for x in pedidos2]
print(totales)