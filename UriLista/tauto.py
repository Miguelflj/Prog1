
def main():
    flag = True
    frase = raw_input()
    while flag:
        tauto = True
        frase = frase.upper()
        frase = frase.split()
        tam = len(frase)
        comb = frase[0][0]
        for i in range(1,tam):
            if(comb != frase[i][0]):
                tauto = False
        if(tauto == True):
            print 'Y'
        else:
            print 'N'
        frase = raw_input()
        if(frase == '*'):
            flag = False


main()
