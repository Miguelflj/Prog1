

def main():
    vet = []
    vetN = []
    j = 19
    for i in range(20):
        vet.append(int(input()))
    for i in range(19,-1,-1):
        vetN.append(vet[i])
    for i in range(20):
        print("N[" +str(i)+"]"+ " = "+ str(vetN[i]))







main()

