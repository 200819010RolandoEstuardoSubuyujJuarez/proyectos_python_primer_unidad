#https://projecteuler.net/archives
print('''
Encontrar los primeros N numeros amigos.
Debe preguntar al usuario el valor de N antes de iniciar.
http://es.wikipedia.org/wiki/N%C3%BAmeros_amigos
''')



temporal = 0
lista= []
final  = int(input("ingrese primer numero > "))
final2 = int(input("ingrese segundo numero > "))
        
for i in range(1, final):
        if final%i == 0 :
                temporal = temporal + i                
                lista.append(i)
                
if final2 == temporal:
        print("son amigos", final, temporal)
        print(lista)
        print("la suma de la lista es: ",temporal)
        activo = True       
else:
        print("no son amigos")
        activo = True
                
       














