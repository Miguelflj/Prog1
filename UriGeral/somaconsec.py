



def main():
    soma = 0
    entrada = raw_input()
    vet = entrada. split()
    a = int(vet[0])
    n = int(vet[1])
    i = 1
    while(n <= 0):
        i += 1
        n = int(vet[i])
    for i in range(n):
        soma += a
        a += 1
    print soma

main()