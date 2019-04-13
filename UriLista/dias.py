#UFMT CCOMP
#LISTA 1 DIAS EM ANO
#MIGUEL FREITAS

def main():
    d = int(input())
    cont1 = 0
    cont2 = 0
    cont3 = 0
    while (d >= 365):
        d = d - 365
        cont1 += 1
    while (d >= 30):
        d = d - 30
        cont2 += 1
    while (d >= 1):
        d = d - 1
        cont3 += 1
    
    print (cont1), "ano(s)"
    print (cont2), "mes(es)"
    print (cont3), "dia(s)"
main()