def EncontraMaior(mtz,tamL,tamC):
    
    maior = mtz[0][0]
    for i in range(tamL):
        for j in range(tamC):
            if(maior < mtz[i][j]):
                maior = mtz[i][j]
    return maior