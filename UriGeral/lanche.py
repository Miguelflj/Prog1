

def main():
    
    entrada = raw_input()
    cod,qtd = entrada.split()
    cod = int(cod)
    qtd = int(qtd)
    if(cod == 1):
        valor = qtd * 4.00
    if(cod == 2):
        valor = qtd * 4.50
    if(cod == 3):
        valor = qtd * 5.00
    if(cod == 4):
        valor = qtd * 2.00
    if(cod == 5):
        valor = qtd * 1.50
        
    print "Total: R$ %0.2f" %(valor)
    

main()