#UFMT CCOMP
#MATRIZ SOMA OU MEDIA DA AREA SUPERIOR

def main():
    soma = 0
    mtz = [] #DECLARA VETOR
    for i in range(12): #CRIA MATRIZ
        mtz.append([0]*12)
    op = raw_input() #LE A OPERACAO
    
    for i in range(12):
        for j in range(12):
                mtz[i][j] = float(input())
                
    for i in range(12):
        for j in range(12):
            if (i < j):
                 if ((i + j) <= 10):
                    soma = mtz[i][j] + soma
    if(op == "S"):
        print "%0.1f" %(soma)
    elif(op == "M"):
        media = (soma/30.0)
        print "%0.1f" %(media)
        
main()  