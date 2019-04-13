#UFMT CCOMP
#TIRAR MEDIA, MAIOR E MENOR
#MIGUEL FREITAS

def main():
    vet = []
    i = 0
    while (i < 10):
        vet.append(input())
        i += 1
    
    menor = vet[0]
    maior = vet[0]
    soma = 0
    i = 0
    while (i < 10):
        if(menor > vet[i]):
            menor = vet[i]
        if (maior < vet[i]):
            maior = vet[i]
        soma = vet[i] + soma
        i += 1
    media = soma/10
    print "Maior numero: " + str(maior)
    print "Menor numero: " + str(menor)
    print "Media numero: " + str(media)
    
    


main()