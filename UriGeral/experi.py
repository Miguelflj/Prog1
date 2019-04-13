

def main():
    n = int(input())
    totalCobaia = 0
    coelho = 0
    rato = 0
    sapo = 0
    for a in range(n):
        entrada = raw_input()
        qtd,tipoCobaia = entrada.split()
        qtd = int(qtd)
        totalCobaia = qtd + totalCobaia
        if(tipoCobaia == "C"):
            coelho = qtd + coelho
        if(tipoCobaia == "R"):
            rato = qtd + rato
        if(tipoCobaia == "S"):
            sapo = qtd + sapo
    
    percC = (coelho*100.0)/totalCobaia
    percR = (rato*100.0)/totalCobaia
    percS = (sapo*100.0)/totalCobaia
    
    print "Total: " + str(totalCobaia) + " cobaias"
    print "Total de coelhos: " + str(coelho)
    print "Total de ratos: " + str(rato)
    print "Total de sapos: " + str(sapo)
    print "Percentual de coelhos: %0.2f " %(percC) + "%"
    print "Percentual de ratos: %0.2f " %(percR) + "%"
    print "Percentual de sapos: %0.2f " %(percS) + "%"
main()