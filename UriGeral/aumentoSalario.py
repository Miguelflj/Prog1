

def main():
    
    s = float(input())
    
    if(s >= 0 and s <= 400.00):
        perc = 15
    if( s >= 400.01 and s <= 800.00):
        perc = 12
    if(s >= 800.01 and s <= 1200.00):
        perc = 10
    if (s >= 1200.01 and s <= 2000.00):
        perc = 7
    if (s > 2000.00):
        perc = 4
    
    reaj = ((s * perc) / 100.00)
    s = reaj + s
    print "Novo salario: %0.2f" %(s)
    print "Reajuste ganho: %0.2f" %(reaj)
    print "Em percentual: " + str(perc) + " %"
    
main()