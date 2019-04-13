


def main():
    cont = 0
    cont1 = 0
    qtdn = int(input())
    for i in range(qtdn):
        n = int(input())
        if(n >= 10 and n <= 20 ):
            cont +=1
        else:
            cont1 += 1
    print str(cont) + " in"
    print str(cont1) + " out"
main()