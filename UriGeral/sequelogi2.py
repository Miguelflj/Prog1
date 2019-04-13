

def main():
    entrada = raw_input()
    x,y = entrada.split()
    x = int(x)
    y = int(y)
    aux = 1
    a = 1
    for i in range(a,y+1):
        for j in range(aux,x+aux):
            print (j),
        print "\n",
        aux += x
        if(j == y):
            a = y +5
main()