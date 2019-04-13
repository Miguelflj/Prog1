

def main():
    
    n = int(input())
    for h in range(n):
        
        
        
        fraseOrd = str()
        vetTam = []
        
        frase = raw_input()
        
        vetP = frase.split()
        
        controle = len(vetP)
        
        for i in range(controle):
            vetTam.append(len(vetP[i]))
        cont = len(vetP)
        
        vetTam = sorted(vetTam,reverse=True)
        for i in range(controle):
            for j in range(cont):
                if(vetTam[i] == len(vetP[j])):
                    
                    if(i == controle-1):
                        fraseOrd = fraseOrd + vetP[j]
                        vetP[j] = str()
                    else:
                        fraseOrd = fraseOrd + vetP[j] + " "
                        vetP[j] = str()
                        
        print (fraseOrd)
        

main()