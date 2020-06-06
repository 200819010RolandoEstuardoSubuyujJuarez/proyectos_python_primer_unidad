#https://projecteuler.net/archives
print('''
Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.
''')




a = 9
n = 1
salida =0
while n <= a:
        
        modulo1 = n%3
        modulo2 = n%5
        
        if modulo1 == 0 and modulo2 == 0:
                print(n)
                salida = salida + n
        elif modulo1 == 0 or modulo2 == 0:
                print(n)
                salida = salida + n
        n = n +1
                
print("el valor total es: ", salida)        
