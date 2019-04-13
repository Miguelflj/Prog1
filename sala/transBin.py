


def main():
    vetB = []
    n = int(input())
    for i in range(n):
        print "digite 0 ou 1"
        vetB.append(input())
    print "numero binario\n" + str(vetB)
    expo = len(vetB) - 1
    numD = 0
    for i in range(n):
        numD = ((vetB[i]* 2 ** expo) + numD)
        expo = expo - 1 
    
    print "numero decimal: " + str(numD)
    numB = []
    for i in range(n):
        numB.append(numD%2)
        numD = numD / 2
        
            
            

                
    numB = sorted(numB)
    
    print "numero binario" + str(numB)
    
main()




