
def main():
    entrada = raw_input()
    a,b = entrada.split()
    a = int(a)
    b = int(b)
    if (a > b):
        aux = b
        b = a
        a = aux
    if(b%a == 0):
        print "Sao Multiplos"
    else:
        print "Nao sao Multiplos"
        
        
main()