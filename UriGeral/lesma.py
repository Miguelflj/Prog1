









flag = True
while(flag):
    try:
        qtd = int(input())
        i = 0
        vet = raw_input()
        vet = vet.split()
        while(i < qtd):
            vet[i] = int(vet[i])
            i += 1
        
        
        maior = vet[0]
        i = 0
        while(i < qtd):
            if(maior < vet[i]):
                maior = vet[i]
            i += 1
            
        if(maior < 10):
            print "1"
        elif(maior >= 20):
            print "3"
        else:
            print "2"

    except EOFError:
        flag = False