#https://projecteuler.net/archives
print('''
Encontrar los primeros N numeros perfectos
Como sugerencia, puede implementar una funcion que encuentre
los divisores propios de un numero, y devuelva una lista con estos
N es un numero que ingresa el usuario
http://es.wikipedia.org/wiki/N%C3%BAmero_perfecto
''')

final = int(input("> "))
lista= []

for i in range(1, final):
        if final%i == 0 :
                lista.append(i)
                
print(lista)        














