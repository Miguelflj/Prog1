







qtd = int(input())
for i in range(qtd):
    entrada = raw_input()
    n1,op1,n2,op2 = entrada.split()
    valor = raw_input()
    v1,v2 = valor.split()
    v1 = int(v1)
    v2 = int(v2)

    soma = v1 + v2
    if(soma % 2 == 0 ):
        if(op1 == "PAR"):
            print(n1)
        else:
            print(n2)
    else:
        if(op1 == "IMPAR"):
            print(n1)
        else:
            print(n2)