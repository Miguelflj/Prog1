#UFMT CCOMP
#MATRIZ SOMA OU MEDIA ABAIXO DA DIAGONAL SEC

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
            if ((i + j) >= 12):
                soma = mtz[i][j] + soma
    if(op == "S"):
        print "%0.1f" %(soma)
    elif(op == "M"):
        media = (soma/66.0)
        print "%0.1f" %(media)
        
main()  