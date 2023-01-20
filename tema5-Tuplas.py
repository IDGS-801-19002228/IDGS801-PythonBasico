
#Es una lista estatica, no permite cambios
tupla=(1,2,3)
print(tupla)
print(type(tupla))

tupla2=(7,"Roberto",True,23.8,16+7j)
print(tupla2)

print(tupla2[1]) #Extra el elemento que se requiera ingresando la posicion.

print(tupla2[4])
print(tupla2[-1]) #Extrae el elemento pero de manera inversa mostrando el ultimo elemento de la tupla
print(tupla2[0:3]) #Extrae un rango de elementos
print(tupla2[3:]) #Otra manera de extraer los elementos

a,b,c=tupla #Asigna los elementos a las letras

print(a)
print(c)

tuplaN=tupla+tupla2
print(tuplaN)
print(tupla.count(2)) #Te dice que cantidades hay de ese elemento, es decir cuantas veces aparece.

tupla[2]=23