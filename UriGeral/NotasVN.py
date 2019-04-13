



def main():
    a = 0
    b = 1
    flag = True
    while flag:
        
        n1 = []
        i = 0
        while i <= 1:
            aux = float(input())
            if(aux >= 0 and aux <= 10.0):
                n1.append(aux)
            else:
                print "nota invalida"
                i -= 1
            i += 1
        media = ((n1[a] + n1[b])/2.0)
        print "media = %0.2f" %(media)
        print "novo calculo(1-sim 2-nao)"
        op = int(input())
        if(op == 1):
            flag = True
            a += 2
            b += 2
        if(op == 2):
            flag = False
        else:
            print "novo calculo(1-sim 2-nao)"
main()