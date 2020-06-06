#https://projecteuler.net/archives
print('''


La suma de los cuadrados de los
primeros diez números naturales es,

12+22+. . .+102=385
El cuadrado de la suma de los
primeros diez números naturales es,

(1+2+. . . +10)2=552=3025
Por lo tanto, la diferencia entre la suma de los
cuadrados de los primeros diez números naturales
y el cuadrado de la suma es 3025a385x2640.

Encuentra la diferencia entre la suma de los cuadrados
de los primeros cien números naturales y el cuadrado de la suma.

''')





inicio = 1
final = 100


temp = 0
temp2 = 0
cuadra = 0


for i in range (inicio, final+1):
        temp = temp + i
        temp2 = temp2 + i**2
        if i == final :
                 
                cuadra = temp**2
                print( cuadra)
                print( temp2)

print( "valor total : ",abs(temp2-cuadra))

















