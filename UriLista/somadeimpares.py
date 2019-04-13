#UFMT CCOMP
#lista 2 soma de numeros impares consecutivos
#MIGUEL FREITAS

def main():
    X = int(input())
    Y = int(input())
    if (X < Y):
        aux = Y
        Y = X
        X = aux
    soma = 0
    X = X - 1
    while (X > Y):
        if(X %2!= 0):
            soma = soma + X
        X -= 1
    print (soma)
    
main()