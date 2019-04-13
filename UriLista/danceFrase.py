



def main():
        frase = raw_input()
        cont = 1
        fraseDance = str()
        for letra in frase:
            if (letra == " "):
                fraseDance = fraseDance + letra
            if(letra.isdigit() == True):
                fraseDance = fraseDance + letra
            elif(cont%2 != 0):
                fraseDance = fraseDance + letra.upper()
                cont += 1
            elif(cont%2 == 0):
                fraseDance = fraseDance + letra.lower()
                cont += 1
        cont += 1
        if (letra == " "):
            fraseDance = fraseDance + letra
        if(letra.isdigit() == True):
            fraseDance = fraseDance + letra
        elif(cont%2 != 0):
            fraseDance = fraseDance + letra.upper()
            cont += 1
        elif(cont%2 == 0):
            fraseDance = fraseDance + letra.lower()
            cont += 1
                
        print (fraseDance)

main()