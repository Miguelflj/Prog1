


def main():
    vet = []
    qtd = int(input())
    i = 0
    cont = 0
    entrada = raw_input()
    vet = map(int,entrada.split())
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