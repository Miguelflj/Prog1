#EXE. 3 SALA
#MIGUEL FREITAS
def main():
    vetA = []
    arquivo = open("entradaA.txt","r")
    for i in arquivo:
        vetA.append(int(i))
    vetA = sorted(vetA)
    contA = len(vetA)
    arquivo.close()
    
    vetB = []
    arquivo = open("entradaB.txt","r")
    for i in arquivo:
        vetB.append(int(i))
    vetB = sorted(vetB)
    contB = len(vetB)
    arquivo.close()
    
    
    #descobre a interseccao
    vetInt = []
    for i in range(contA):
        for j in range(contB):
            if(vetA[i] == vetB[j]):
                vetInt.append(vetA[i])
                j = contB+1
    #uniao 
    vetUni = []
    
    contInt = len(vetInt)
    for i in range(contA):
        vetUni.append(vetA[i])
    for i in range(contB):
        vetUni.append(vetB[i])
    
    for i in range(contInt):
        vetUni.remove(vetInt[i])
                
    vetUni = sorted(vetUni)
    arquivo = open("saida.txt", "w")
    arquivo.write("entradaA: " + str(vetA))
    arquivo.write("\n")
    arquivo.write("entradaB: " + str(vetB))
    arquivo.write("\n")
    arquivo.write("Intesecao: " + str(vetInt))
    arquivo.write("\n")
    arquivo.write("Uniao: " + str(vetUni))
    arquivo.close()
main()
