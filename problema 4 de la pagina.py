#https://projecteuler.net/archives
print('''


2520 es el número más pequeño que se puede
dividir por cada uno de los números del 1 al 10 sin ningún resto.

¿Cuál es el número positivo más pequeño que es
uniformemente divisible por todos los números del 1 al 20?



''')




a = 2520
n = 0
inicio = 1
siguiente = 0
temporal = 1

resultado = 0


while n <= a :
        n = n + 1

        resultado = a%n
        if resultado == 0:
                print(1)
                if(resultado == 0):
                        print(2)
                        if(resultado == 0):
                                print(3)         
                                if resultado == 0:
                                        print(4)
                                        if(resultado == 0):
                                                print(5)
                                                if(resultado == 0):
                                                        print(6)  
                                                        if resultado == 0:
                                                                print(7)
                                                                if(resultado == 0):
                                                                        print(8)
                                                                        if(resultado == 0):
                                                                                print(9)         
                                                                                if resultado == 0:
                                                                                        print(10)
                                                                                        print(n)
                                                                                        break
                                                     

























