print('''

Una permutación es una disposición ordenada de objetos. 
Por ejemplo, 3124 es una posible permutación de los dígitos 
1, 2, 3 y 4. Si todas las permutaciones se enumeran numérica 
o alfabéticamente, lo llamamos orden lexicográfico. 
Las permutaciones lexicográficas de 0, 1 y 2 son:

012 021 102 120 201 210

¿Cuál es la permutación lexicográfica millonésima de 
los dígitos 0, 1, 2, 3, 4, 5, 6, 7, 8 y 9?
''')

ingreso = 523#int(input("ingrese un numero : "))
lista = list(str(ingreso))
largo = len(lista)
ordenada = list(sorted(lista))
temp = 1
salida = []
print(largo, lista, ordenada)

for i in range ( 1, largo+1):   #se obtienen todas las combinaciones
    temp = temp*i
print(temp)

for i in range(0, temp):
    #print(i)
    for n in range(0, largo):
        #print(i,n)
        print(i, ordenada[n])
    
    #print(salida)
        
        
    









