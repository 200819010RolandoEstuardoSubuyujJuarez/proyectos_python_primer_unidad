print('''
Considere todas las combinaciones de enteros de a b 
para 2 ≤ a ≤ 5 y 2 ≤ b ≤ 5:

    2 2 = 4, 2 3 = 8, 2 4 = 16, 2 5 = 32
    3 2 = 9, 3 3 = 27, 3 4 = 81, 3 5 = 243
    4 2 = 16, 4 3 = 64, 4 4 = 256, 4 5 = 1024
    5 2 = 25, 5 3 = 125, 5 4 = 625, 5 5 = 3125

Si luego se colocan en orden numérico, con cualquier 
repetición eliminada, obtenemos la siguiente secuencia 
de 15 términos distintos:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

¿Cuántos términos distintos hay en la secuencia generada 
por a b para 2 ≤ a ≤ 100 y 2 ≤ b ≤ 100?

      ''')

in1 = int(input("ingrese a1 : "))
in2 = int(input("ingrese a2 : "))
in3 = int(input("ingrese b1 : "))
in4 = int(input("ingrese b2 : "))

print('''
      
      
            
      
      ''')

lista_a = []
lista_b = []
lista_cua=[]
valor = 0

for i in range(in1, in2+1):
    lista_a.append(i)
    

for i in range(in3, in4+1):
    lista_b.append(i)
    
    
#lista_a.extend(lista_b) 
#print(lista_a)   
r = lista_a[:]

for i in r:
    for n in r:
        
        valor = i**n
        lista_cua.append(valor)
        
lista_cua.sort()
print(lista_cua)


t1 = lista_cua[0]
t2 = 0
te = lista_cua[:]
del te[1:]

for i in range(1, len(lista_cua)):
    t2 = lista_cua[i]
    #print(t1, t2)
    if (t1 == t2):
        print(t1, t2)
        print("son iguales se saca: ", lista_cua[i])
    else:  
        te.append(t2)  
        t1 = t2
        
print(te)    
    
    







