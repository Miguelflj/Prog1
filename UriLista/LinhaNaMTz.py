#UFMT CCOMP
#MATRIZ SOMA OU MEDIA DE LINHA

def main():
    soma = 0
    mtz = [] #DECLARA VETOR
    for i in range(12): #CRIA MATRIZ
        mtz.append([0]*12)
        
        
    lin = int(input()) #LE A LINHA DA OPERACAO
    op = raw_input() #LE A OPERACAO
    
    for i in range(12):
        for j in range(12):
                mtz[i][j] = float(input())
                
    for j in range(12):
        soma = mtz[lin][j] + soma
    if(op == "S"):
        print "%0.1f" %(soma)
    elif(op == "M"):
        media = (soma/12.0)
        print "%0.1f" %(media)
        
main()        