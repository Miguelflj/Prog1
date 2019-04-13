#UFMT CCOMP
#LISTA 2 USO DE LACO
#MIGUEL FREITAS

def main():
    i = 0
    j = 1
    while (i <= 2):
        if (i%1.0) == 0:
            i = int(i)
            print "I=" + str(i),"J="+str(j)
        else:
             print "I="+str(i),"J="+str(j)
        j += 1
        if (j > (3 + i)):
            i = i + 0.2
            j = j - (j-i) + 1
    
main()