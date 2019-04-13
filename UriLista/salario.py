#UFMT CCOMP
#LISTA 1 SALARIO
#MIGUEL FREITAS

def main():
    n = raw_input()
    sf = float(input())
    vm = float(input())
    comi = (vm*15)/100
    s = sf + comi
    print "TOTAL = R$ %0.2f" % s
    
main()