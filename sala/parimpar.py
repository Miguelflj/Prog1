


def main():
    vet1 = [] 
    vet2 = []
    i = 0
    while( i < 5):
        x = int(input("Entre com valores inteiros e positivos: "))
        print "\n"
        if (x%2 == 0):
            vet1.append(x)
        else:
            vet2.append(x)
        i += 1
        
    print "vetor de numeros pares\n" + str(vet1)
    print "\n"
    print "vetor de numeros impares\n" + str(vet2)

main()