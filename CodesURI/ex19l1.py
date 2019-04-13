




palavra = str(input())

t = len(palavra)
aux = t -1

for i in range(t):
    j = aux
    while(j < t):
        print(palavra[j],end = "")
        j = j + 1
    print()
    aux = aux - 1