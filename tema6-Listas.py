
nombres=["Juan","Mario","Laura"]
numeros=[1,2,3,4,5]

datos=[1,2.5,"Mario",True]

nombres[0]="Roberto"

#Forma de recorrer la lista(tupla)
print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario") #Insertar un nuevo elemento
print(nombres)
nombres.insert(2,"Maria") #Agrega el elemento en la posicion indicada reemplazando el que ya estaba.
print(nombres)

nombres.extend(["Chencha",2,23,5]) #Une dos listas.
print(nombres)
nombres.remove("Chencha") #Elimina el elemento indicado en este caso una cadena
print(nombres)
nombres.pop() #Elimina el ultimo elemento.
print(nombres)

n=["Juan"]
n2=n*5 #Multiplica o duplica por "N" cantidad el elemento o los elementos de la lista
print(n2)
print(nombres)

del nombres[0] #Elimina el primer elemento de la lista.
print(nombres)