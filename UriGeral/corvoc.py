







soma = 0
j = 0

while(j < 3):
    pot = 2
    nBin = raw_input()
    tam = len(nBin)
    if(tam == 3):
        for i in range(3):
            if( nBin[i] == "*"):
                soma += 2 ** pot
            pot -= 1
    else:
        j += 1
        print soma
        soma = 0