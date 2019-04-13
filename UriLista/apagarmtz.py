#UFMT CCOMP
#MATRIZ SOMA OU MEDIA DA DIAGONAL PRINCIPAL

def main():
    soma = 0
    mtz = [] #DECLARA VETOR
    for i in range(4): #CRIA MATRIZ
        mtz.append([0]*4)
    op = raw_input() #LE A OPERACAO
    
    for i in range(4):
        for j in range(4):
                mtz[i][j] = float(input())
                
    for i in range(4):
        for j in range(4):
            if (i < j):
                soma = mtz[i][j] + soma
    if(op == "S"):
        print "%0.1f" %(soma)
    elif(op == "M"):
        #media = (soma/4.0)
        print "%0.1f" %(media)
        
main()        