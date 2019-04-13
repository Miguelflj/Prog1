from lista import encontraMaior
                    

def main():
    vet = []
    vetMaior = []
    flag = True
    i = 0
    while flag == True:
        vet.append(input())
        if(vet[i] != 0):
            i += 1
        else:
            
            flag = False
    for i in range(5):
        maior =  encontraMaior(vet)

        vetMaior.append(maior)
        
        vet.remove(maior)
        
    print "5 maiores fockius numeros (logo abaixo) =): \n" + str(vetMaior)
main()