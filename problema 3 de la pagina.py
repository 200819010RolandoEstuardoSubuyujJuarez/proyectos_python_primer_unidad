#https://projecteuler.net/archives
#http://es.onlinemschool.com/math/assistance/number_theory/multiplier/
print('''


Los factores primos de 13195 son 5, 7, 13 y 29.

¿Cuál es el factor primo más grande del número 600851475143 ?

''')

a = 600851475143
x = 600851475143
n = 1
resultado = 0
temp = 0

while n <= a :
        n = n + 1
        resultado = x%n
        if resultado == 0:
                temp = x/n
                print (n)
                x = temp
                 

                

        
        
        
