def main():
    n = int(input())
    for h in range(n):
        cont = 0
        fraseOrd = str()
        vetTam = []
        frase = raw_input()
        for i in frase:
            if( i != " "):
                vetTam.append(len(i))
                cont += 1
        vetTam = sorted(vetTam)
        #for i in range(cont-1,-1,-1):
        i = 0
        for j in frase:
            print(j)
            if(j == " "):
                fraseOrd = fraseOrd + j
            elif(vetTam[i] == len(j)):
                    fraseOrd = fraseOrd + j
                    i += 1
        print (fraseOrd)

main()