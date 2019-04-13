


def main():
    entrada = raw_input()
    cp,np,vuP = entrada.split()
    vuP = float(vuP)
    np = int(np)
    
    entrada1 = raw_input()
    cp2,np2,vuP1 = entrada1.split()
    vuP1 = float(vuP1)
    np2 = int(np2)
    
    soma = ((np*vuP) + (np2*vuP1))
    
    print "VALOR A PAGAR: R$ %0.2f" %(soma)
main()