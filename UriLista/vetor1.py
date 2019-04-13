#UFMT CCOMP
#VETOR E SUBSTITUICAO
#MIGUEL FREITAS

def main():
    vet = []
    i = 0
    while (i < 10):
        vet.append(int(input()))
        i = i + 1
    i = 0
    while (i < 10):
        if( (vet[i]) <= 0):
            (vet[i]) = 1
            
        print "X[" +str(i) +"] = " + str(vet[i])
        i = i + 1
main()