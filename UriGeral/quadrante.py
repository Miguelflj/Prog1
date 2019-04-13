

def main():
    entrada = raw_input()
    x,y = entrada.split()
    x = int(x)
    y = int(y)
    while(x != 0 and y != 0):
        if(x > 0 and y > 0):
            print "primeiro"
        if(x < 0 and y > 0):
            print "segundo"
        if(x < 0 and y < 0):
            print "terceiro"
        if(x > 0 and y < 0):
            print "quarto"
        entrada = raw_input()
        x,y = entrada.split()
        x = int(x)
        y = int(y)
        
        
main()