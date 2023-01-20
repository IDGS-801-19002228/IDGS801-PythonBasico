
cadena="Universidad Tecnologica de Leon"

print(cadena)
print(cadena.lower())
print(cadena.upper())
print(cadena.title())
print(cadena.find("de")) #Para buscar la palabra 
print(cadena.count("a")) #saber cuantas letras "a" aparecen

textoFinal=cadena.replace("a","4") #Reemplaza la letra "a" por el numero "4"
print(textoFinal)
cadenaNueva=cadena.split(" ") #Separa las palabras
print(cadenaNueva)