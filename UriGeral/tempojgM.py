def main():

    entrada = raw_input()
    Hi,Mi,Hf,Mf = entrada.split()
    Hi = int(Hi)
    Mi = int(Mi)
    Hf = int(Hf)
    Mf = int(Mf)
    contH = 0
    if(Hf <= Hi):
        Hf += 24
    tempoM = ((Hf - Hi) * 60)
    tempoM = tempoM + (Mf - Mi)
    while(tempoM >= 60):
            tempoM -= 60
            contH += 1
    print "O JOGO DUROU " + str(contH) + " HORA(S) E " + str(tempoM) + " MINUTO(S)"

main()