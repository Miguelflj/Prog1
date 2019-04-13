def main():
    n = int(input())
    for h in range(n):
        soma = 0
        entrada = raw_input()
        x,y = entrada.split()
        x = int(x)
        y = int(y)
        if(x > y):
            aux = x
            x = y
            y = aux
        for i in range(x+1,y):
            if(i%2 != 0):
                soma = soma + i
        print (soma)
        
        
        
main()