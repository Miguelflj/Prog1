def main():
    vet = []
    for i in range(5):
        vet.append(int(input()))
    maior = vet[0]
    for i in range(5):
        if(maior < vet[i]):
            maior = vet[i]
            p = i
    print (maior)
    print (p+1)
main()