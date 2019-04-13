



def main():
    entrada = raw_input()
    a,b,c = entrada.split()
    a = float(a)
    b = float(b)
    c = float(c)
    delta = ((b*b)-(4.0*a*c))
    if(delta <= 0):
        print "Impossivel calcular"
    else:
        det = (delta**0.5)
        if(a == 0 or det == 0):
            print "Impossivel calcular"
        else:
    
            r1 = ((-b + det)/ (2.0*a))
            r2 = ((-b - det)/ (2.0*a))
            print "R1 = %0.5f" %(r1)
            print "R2 = %0.5f" %(r2)
    

main()