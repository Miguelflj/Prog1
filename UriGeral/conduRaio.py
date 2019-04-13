



casos = int(input())

for i in range(casos):
    
    entrada = raw_input()
    
    a,b = entrada.split()
    
    a = int(a)
    b = int(b)
    a = a + a
    b = b + b

    mraio = ( (a + b)/ 2)
    
    print (mraio)
    
    i += 1