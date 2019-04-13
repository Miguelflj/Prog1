

def main():
    cont = 0
    entrada = raw_input()
    hi,hf = entrada.split()
    hi = int(hi)
    hf = int(hf)
    if(hf <= hi):
        hf += 24
    tempo = hf - hi
    print "O JOGO DUROU " + str(tempo) + " HORA(S)"
main()