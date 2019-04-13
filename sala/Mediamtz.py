def MediaMtz(mtz,tamL,tamC):
    soma = 0 
    div = tamL * tamC
    for i in range(tamL):
        for j in range(tamC):
            soma = mtz[i][j] + soma
        media = float(soma /div)
    return media