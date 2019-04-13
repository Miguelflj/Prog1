
def main():
    entrada = raw_input()
    n1,n2,n3 = entrada.split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    
    maior = n1
    if (maior < n2):
        maior = n2
    if (maior < n3):
        maior = n3
    
    print "%d eh o maior" %(maior)

main()