

def main():
    imposto = 0
    valor = float(input())
    
    if(valor <= 2000.00):
        print "Isento"
    else:
        valor = valor - 2000.00
    if(valor >= 2000.01 and valor <= 3000.00 ):
        imposto = (valor * 8)/100
        valor = valor - 3000.00
    if (valor >= 3000.01 and valor <= 4500.00):
        imposto =(imposto + ((valor*18)/100))
        
    if ( valor > 4500.00):
        imposto = (imposto + ((valor*28/100)))
                   
    print "R$ %0.2f" % (imposto)
        
    
main()