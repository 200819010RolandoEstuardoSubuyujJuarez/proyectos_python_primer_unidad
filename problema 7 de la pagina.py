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





total = [2]
final = 13
a = 0
for x in range(3,final + 1):
        for i in range(2, x):
                if x%i != 0:
                        continue
                else:
                        break
        else:
                #print(x)
                total.append(x)
print(len(total))












