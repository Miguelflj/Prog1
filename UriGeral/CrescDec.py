
def main():
    entrada = raw_input()
    x,y = entrada.split()
    x = int(x)
    y = int(y)
    while(x != y):
        if(x < y):
            print "Crescente"
        if(x > y):
            print "Decrescente"
        entrada = raw_input()
        x,y = entrada.split()
        x = int(x)
        y = int(y)
main()