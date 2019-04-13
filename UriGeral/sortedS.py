
def main():
    
    vet = raw_input()
    vet = vet.split()
    
    for i in range(3):
        vet[i] = int(vet[i])
    vetC = sorted(vet)
    for i in range(3):
        print(vetC[i])
        if(i == 2):
            print "\n",
    for i in range(3):
        print(vet[i])
main()