

def main():
    numB = []
    numD = int(input())
    flag = True
    i = 0
    while flag == True:

        numB.append(numD%2)
        print numB[i]
        numD = numD / 2
        print numD
        i += 1
        if(1 > numD):
            numB.append(0)
            flag = False
            

                
    numB = sorted(numB)
    
    print "numero binario" + str(numB)
    
main()