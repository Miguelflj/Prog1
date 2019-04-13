#UFMT CCOMP
#DISTANCIA ENTRE PONTOS lista 2
#MIGUEL FREITAS

import math
 
def main():
    entrada1 = raw_input()
    x1,y1 = entrada1.split()
    entrada2 = raw_input()
    x2,y2 = entrada2.split()
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    dist = math.sqrt((((x1-x2)**2) + ((y1-y2)**2)))
    print("%.4f"%dist)
                        
main()