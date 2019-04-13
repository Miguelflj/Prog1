


def main():
    
    i = 0
    soma = 0
    cont = 0
    while(i < 20):
        n = int(input("Digite um numero maior ou menor que zero\n"))
        i += 1
        if(n > 0):
            soma = n + soma
        if(n < 0):
            cont +=1
            
            
    print "A soma dos positivos eh: " + str(soma)
    print "A quantia dos negativos eh: " + str(cont)
    
    
main()