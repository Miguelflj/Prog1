



def main():
    entrada = raw_input()
    a,b,c = entrada.split()
    a = float(a)
    b = float(b)
    c = float(c)

    difbc = b - c
    difac = a - c
    difab = a - b
    
    sombc = b + c
    somac = a + c
    somab = a + b

    if(difbc < 0):
        difbc = (difbc * -1)
    if(difac < 0):
        difac = (difac * -1)
    if(difab < 0):
        difab = (difab * -1)
    
    flag = True
    if(not(difbc < a < sombc)):
        flag = False
    if(not(difac < b < somac)):
        flag = False
    if(not(difab < c < somab)):
        flag = False
    
    if(flag == True):
        peri = a + b + c
        print "Perimetro = %0.1f" %peri
    else:
        area = ((( a + b )* c )/ 2)
        print "Area = %0.1f" %area
    
    

main()