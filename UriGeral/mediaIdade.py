


def main():
    soma = 0
    flag = True
    cont = 0.0
    idade = int(input())
    if(idade < 0):
            flag = False
            
    while flag:
        
        cont += 1
        soma = idade + soma
        idade = int(input())
        if(idade < 0):
            flag = False
    
    mediaIdade =(soma/cont)

    print "%0.2f" %(mediaIdade)
    
main()