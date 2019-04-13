

def main():
    flag = True
    contVG = 0
    contVI = 0
    empate = 0
    cont = 0
    while flag:
        cont += 1
        entrada = raw_input()
        gi,gg = entrada.split()
        gg = int(gg)
        gi = int(gi)
        if(gi > gg):
            contVI += 1
        if(gg > gi):
            contVG += 1
        if(gg == gi):
            empate += 1
        print "Novo grenal (1-sim 2-nao)"
        op = int(input())
        if(op == 2):
            flag = False
    print str(cont) + " grenais"
    print "Inter:" + str(contVI)
    print "Gremio:" + str(contVG)
    print "Empates:" + str(empate)
    if(contVI > contVG):
        print "Inter venceu mais"
    if(contVG > contVI):
        print "Gremio venceu mais"
    if(contVG == contVI):
        print "Nao houve vencedor"

main()