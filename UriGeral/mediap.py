

def main():
    n = int(input())
    for a in range(n):
        entrada = raw_input()
        n1,n2,n3 = entrada.split()

        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
            
        mediaP = ((2*n1) + (3*n2) + (5*n3))/10.0
        print "%0.1f" %(mediaP)




main()