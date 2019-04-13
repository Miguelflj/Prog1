

def main():
    soma = 0
    cont = 0
    
    for i in range(6):
        n = input()
        if(n > 0):
            soma = n + soma
            cont += 1
    media = (soma/cont)
    print str(cont) + " valores positivos"
    print "%0.1f" %(media)

main()