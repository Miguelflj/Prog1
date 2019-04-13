

def main():
    n = int(input())
    for h in range(n):
        entrada = raw_input()
        x,y = entrada.split()
        x = float(x)
        y = float(y)
        if(y == 0):
            print "divisao impossivel"
        else:
            divi = x/y
            print "%0.1f" %(divi)
    
    
main()