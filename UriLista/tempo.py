#UFMT CCOMP
#LISTA 1 CONVERSAO DE TEMPO
#MIGUEL FREITAS

def main():
    seg = int(input())
    cont1 = 0
    cont2 = 0
    cont3 = 0
    while (seg > 3600):
        seg = seg - 3600
        cont1 += 1
    while (seg > 60):
        seg = seg - 60
        cont2 += 1
    while ( seg >= 1):
        seg = seg - 1
        cont3 += 1
    print str(cont1)+":"+str(cont2)+":"+str(cont3)
    
main()