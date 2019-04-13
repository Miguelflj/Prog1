







entrada = raw_input()

a,b = entrada.split()

a = int(a)
b = int(b)

if( b > 0 ):
    q = a // b
    r = a % b
    print str(q) + " " + str(r)
else:
    b = -1*b
    q = a // b
    r = a % b
    print str(-q) + " " + str(r)
