
def main():
    vet = []
    qtd = int(input())
    i = 0
    cont = 0
    while (i < qtd):
        vet.append(int(raw_input()))
        i += 1
    menor = vet[0]
    i = 0
    while (i < qtd):
        if (menor > vet[i]):
            menor = vet [i]
            cont = i
        i += 1
    print "Menor valor: " + str(menor)
    print "Posicao: " + str(cont)

main()