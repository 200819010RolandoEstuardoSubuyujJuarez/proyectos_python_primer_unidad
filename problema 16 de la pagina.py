#https://projecteuler.net/archives
print('''

2°15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2°1000?

''')


inicio = int(input("ingrese un numero >"))

temporal= 0
salida = 2**inicio
sa = list(str(salida))
print(sa)
#print(len(sa))
#print("nuevo")
for i in range(0, len(sa)):
        #print(sa[i])
        temporal = temporal + int(sa[i]) 

print(temporal)
        















