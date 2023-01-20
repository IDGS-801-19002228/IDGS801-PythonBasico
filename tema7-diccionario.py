#Nos permite almacenar datos atraves de un key valor

miDiccionario={"Matricula":19002228,"Nombre":"Fernando","Edad":22}

print(type(miDiccionario))
print(miDiccionario)

miDiccionario["Nombre"]="Panfilo" #Cambia el valor por el nuevo valor indicado.
print(miDiccionario)

print(miDiccionario["Edad"]) #Solo imprime el dato requerido.
print(miDiccionario.values()) #Devuelve los valores
print(miDiccionario.keys())
