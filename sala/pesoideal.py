



def main():
    
    sexo =  raw_input("Digite o sexo/homem/mulher: ")
    alt = float(input("Digite sua altura: "))
    if(sexo == "homem"):
        ideal = (72.7 * alt) - 58
        print "Seu peso ideal eh: %0.2fKG" %(ideal)
    elif(sexo == "mulher"):
        ideal = (62.1 * alt) - 44.7
        print "Seu peso ideal eh: %0.2fKG" %(ideal)
    else:
        print "Sexo informado nao identificado"
        
    
    
    

main()