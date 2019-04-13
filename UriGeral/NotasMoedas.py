
def main():
    
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        cont5 = 0
        cont6 = 0
                
            
        contm = 0
        contm1 = 0
        contm2 = 0
        contm3 = 0
        contm4 = 0
        contm5 = 0
        
        cd = float(input())
            
        
        while (cd >= 100.00):
            cd = cd - 100.00
            cont1 += 1
        while (cd >= 50.00):
            cd = cd - 50.00
            cont2 += 1
        while (cd >= 20.00):
            cd = cd - 20.00
            cont3 += 1
        while (cd >= 10.00):
            cd = cd - 10.00
            cont4 += 1
        while (cd >= 5.00):
            cd = cd -5.00
            cont5 += 1
        while (cd >= 2.00):
            cd = cd - 2.00
            cont6 += 1
        
        
        while (cd >= 1.00):
            cd = cd - 1.00
            contm += 1
        while(cd >= 0.50):
            cd = cd - 0.50
            contm1 += 1
        while(cd >= 0.25):
            cd = cd - 0.25
            contm2 += 1
        while(cd >= 0.10):
            cd = cd - 0.10
            contm3 += 1
        while(cd >= 0.05):
            cd = cd - 0.05
            contm4 += 1
        while(cd >= 0.001):
            cd = cd - 0.01
            contm5 += 1
                
        
        print "NOTAS:"
        print (cont1), "nota(s) de R$ 100.00"
        print (cont2), "nota(s) de R$ 50.00"
        print (cont3), "nota(s) de R$ 20.00"
        print (cont4), "nota(s) de R$ 10.00"
        print (cont5), "nota(s) de R$ 5.00"
        print (cont6), "nota(s) de R$ 2.00"
        


        print "MOEDAS:"
        print (contm), "moeda(s) de R$ 1.00"
        print (contm1),"moeda(s) de R$ 0.50"
        print (contm2),"moeda(s) de R$ 0.25"
        print (contm3),"moeda(s) de R$ 0.10"
        print (contm4),"moeda(s) de R$ 0.05"
        print (contm5),"moeda(s) de R$ 0.01"
       
    

main() 