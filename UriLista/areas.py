#UFMT CCOMP
#CALCULAR AREA DAS FIGURAS GEOMETRICAS
#MIGUEL FREITAS

def main():
    #leitura utilizando raw_input e ele devolve uma string
    entrada = raw_input()
    #Usei o .split() para quebrar a string separando pelo espaço/armazei os pedaços em 3 variaveis
    A,B,C = entrada.split()
    #coverteu as variaveis que estavam em string em float(flutuante)
    A = float(A)
    B = float(B)
    C = float(C)
    tring = (A*C)/2.0
    arec = 3.14159*(C*C)
    areat = ((A+B)*C)/2.0
    areaq = (B*B)
    arear = (A*B)
    print "TRIANGULO: %0.3f"%(tring)
    print "CIRCULO: %0.3f"%(arec)
    print "TRAPEZIO: %0.3f"%(areat)
    print "QUADRADO: %0.3f"%(areaq)
    print "RETANGULO: %0.3f"%(arear)
main()