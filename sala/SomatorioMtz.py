def SomaMtz(mtz,tamL,tamC):
    soma = 0
    for i in range(tamL):
        for j in range(tamC):
            soma = mtz[i][j] + soma
    return soma