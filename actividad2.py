
import os

class OperasBas:

    #Constructor de clase
    def __init__(self):
        pass
    #Metodos de clase
    def suma(self,n1,n2):
        res=n1+n2
        return res
    def resta(self,n1,n2):
        res=n1-n2
        return res
    def multiplicacion(self,n1,n2):
        res=n1*n2
        return res
    def division(self,n1,n2):
        res=n1/n2
        return res



def main():
    obj=OperasBas()
    op=-1
    res=0

    while (op!=0):
        op = int(input('\n 1.- Suma\n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Salir \n Introduce un valor: '))
        if (op == 5):
            break
        
        
        n1 = int(input('\n Ingresa el numero 1: '))
        n2 = int(input('\n Ingresa el numero 2: '))
        if (op == 1):
            res = obj.suma(n1, n2)
        elif (op == 2):
            res = obj.resta(n1, n2)
        elif (op == 3):
            res = obj.multiplicacion(n1, n2)
        elif (op == 4):
            res = obj.division(n1, n2)
        print('\n El resultado es: {}'.format(res))


if __name__ == '__main__':
    main()