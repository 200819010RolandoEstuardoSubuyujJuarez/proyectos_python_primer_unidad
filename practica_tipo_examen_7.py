print('''
Al enumerar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, 
podemos ver que el sexto primo es 13.

¿Cuál es el número primo 10 001?
      
      ''')
final = 13

for i in range(0, final+1):
    for n in range(1, final +1):
        inpar = 2*i + 1                
        if n%inpar !=0: #
            print(inpar, i,n, inpar%n) 
            
            
            
            
            
            #if i%2 != 0:
                
                
                #if i%n == 0:
                    