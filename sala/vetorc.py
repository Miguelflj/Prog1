#UFMT CCOMP
#IMPRIMINDO VETOR AO CONTRARIO

#def main():
    #vet = []
    #i = 0
    #while (i < 10):
        #vet.append(input())
        #i += 1
    #print "\n"
    #i = -1
    #while(i >= -10):
        #print (vet[i])
        #i -=1
#main()

#UTILIZANDO LAÇO FOR

def main():
    vet = []
    i = 0
    while (i < 10):
        vet.append(input())
        i += 1
    print "\n"
    i = -1
    for i in range(-1,-11,-1):
        print (vet[i])
       
main()