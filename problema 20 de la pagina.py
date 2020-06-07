print('''"
n ! significa n × ( n - 1) × ... × 3 × 2 × 1

Por ejemplo, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
y la suma de los dígitos en el número 10! es 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

¡Encuentra la suma de los dígitos en el número 100!

"''' )


ingreso = int(input("Ingrese un numero: "))

temp = 1
lista = []
suma = 0
for i in range ( 1, ingreso+1):
    temp = temp*i
    
    
    if i == ingreso:
        lista = list(str(temp))
        print(lista)
        for x in range(0, len(lista)):
            suma = suma + int(lista[x])

print(suma)









