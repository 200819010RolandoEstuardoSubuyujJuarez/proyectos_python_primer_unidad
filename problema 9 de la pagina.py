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
        modulo = inicio%2

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



        
##        i = i + 1
##        
## 
##
##
##
##
##        for i in range(1, valor+1):
##
##                modulo = i%2
##                if( i == inicio):
##                        print(i,modulo)
##                        if modulo == 1:
##                                print("es impar")
##                                valor = 3*i+1
##                                print(valor)
##                        else:
##                                print("es par")
##                                valor = i/2
##                                print(valor)
##                        
##
                














##temp = 0
##lista = [2]
##suma = 0
##
##for i in range(3, inicio+1):
##        for n in range(2, i):
##                temp = i%n
##                if temp != 0:
##                        continue
##                        
##                else:
##                        break
##        else:
##                print(i)
##                suma = suma + i
##                lista.append(i)
##                
##
##print (lista, "el valor de la suma es: ", suma+2)
##










