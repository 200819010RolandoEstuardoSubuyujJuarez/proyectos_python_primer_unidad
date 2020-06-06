#https://projecteuler.net/archives
print('''



La suma de los primos por debajo de 10 es 2 + 3 + 5 + 7 x 17.

Encuentra la suma de todos los primos por debajo de dos millones.

''')

inicio = int(input("ingrese un numero >"))
temp = 0
lista = [2]
suma = 0

for i in range(3, inicio+1):
        for n in range(2, i):
                temp = i%n
                if temp != 0:
                        continue
                        
                else:
                        break
        else:
                print(i)
                suma = suma + i
                lista.append(i)
                

print (lista, "el valor de la suma es: ", suma+2)











