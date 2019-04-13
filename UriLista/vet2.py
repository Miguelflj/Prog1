#UFMT CCOMP
#LISTA 2 VETORES
#MIGUEL FREITAS

def main():
    x = [float(input())]
    i = 1
    y = x[0]
    
    while ( i <= 99):
        y = y/2
        x.append(y)
        i += 1
    i = 0
    while ( i <= 99):
         print "N[" +str(i) +"] = %0.4f" %(x[i])
         i += 1
main()