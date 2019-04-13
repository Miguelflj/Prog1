

def main():
    posi = 0
    nega = 0
    par = 0
    impar = 0
    for i in range(5):
        n = int(input())
        if (n > 0):
            posi += 1
        if(n < 0):
            nega += 1
        if(n%2 == 0):
            par += 1
        if (n%2 != 0):
            impar += 1
            
    print str(par) + " valor(es) par(es)"
    print str(impar) + " valor(es) impar(es)"
    print str(posi) + " valor(es) positivo(s)"
    print str(nega) + " valor(es) negativo(s)"
    
    
main()