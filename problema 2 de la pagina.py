#https://projecteuler.net/archives
print('''


Cada nuevo término de la secuencia de Fibonacci se
genera agregando los dos términos anteriores.
A partir de 1 y 2, los primeros 10 términos serán:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Al considerar los términos de la secuencia de Fibonacci
cuyos valores no superan los cuatro millones,
encuentre la suma de los términos de valor uniforme.



''')




a = 10
n = 1
inicio = 1
siguiente = 0
temporal = 1
print('1')
while n <= a :
        n = n + 1
        
        siguiente = temporal + inicio
        print(siguiente)
        inicio = temporal
        temporal = siguiente
        
        
        
