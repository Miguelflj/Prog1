

def main():
    n = int(input())
    fiboAnt = 0
    fiboAtual = 1
    print (0),
    for i in range(n-1):
       
        aux = fiboAtual
        print (fiboAtual),
        fiboAtual = fiboAtual + fiboAnt
        fiboAnt = aux
        


main()