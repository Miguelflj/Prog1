#UFMT CCOMP
#LISTA 2 CEDULAS
#MIGUEL FREITAS


def main():
    a = int(input())
    cd = a
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    while (cd >= 100):
        cd = cd - 100
        cont1 += 1
    while (cd >= 50):
        cd = cd - 50
        cont2 += 1
    while (cd >= 20):
        cd = cd - 20
        cont3 += 1
    while (cd >= 10):
        cd = cd - 10
        cont4 += 1
    while (cd >= 5):
        cd = cd -5
        cont5 += 1
    while (cd >= 2):
        cd = cd - 2
        cont6 += 1
    while (cd >= 1):
        cd = cd - 1
        cont7 += 1
    print (a)
    print (cont1), "nota(s) de R$ 100,00"
    print (cont2), "nota(s) de R$ 50,00"
    print (cont3), "nota(s) de R$ 20,00"
    print (cont4), "nota(s) de R$ 10,00"
    print (cont5), "nota(s) de R$ 5,00"
    print (cont6), "nota(s) de R$ 2,00"
    print (cont7), "nota(s) de R$ 1,00"

main()