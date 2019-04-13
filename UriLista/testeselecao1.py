#UFMT CCOMP
#LISTA 2 TESTES COM IF
#MIGUEL FREITAS

def main():
    entrada = raw_input()
    A,B,C,D = entrada.split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    if((B > C)and(D > A)):
        if((C + D) > (A + B)):
            if((C and D > 0) and (A%2==0)):
                print "Valores aceitos"
            else:
                 print "Valores nao aceitos"
        else:
             print "Valores nao aceitos"
    else:
         print "Valores nao aceitos"
        
main()