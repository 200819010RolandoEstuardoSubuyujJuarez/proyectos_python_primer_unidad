#https://projecteuler.net/archives
print('''

The following iterative sequence is defined for
the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13,
we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

''')


inicio = int(input("ingrese un numero >"))

modulo = 0
valor = True
sig = 0
lista = [inicio]
while valor :
        modulo = inicio%2 #si el modulo es 0 es par si es 1 es impar

        if inicio == 1:
                valor = False        
        elif modulo == 1:
                sig = int(3*inicio+1)
                #print(sig)
                inicio = sig
                lista.append(sig)
        else:
                sig = int(inicio/2)
                #print(sig)
                inicio = sig
                lista.append(sig)
        
print(lista, ": ", len(lista) )




















