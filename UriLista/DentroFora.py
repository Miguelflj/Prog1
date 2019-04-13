def main():
    n = int(input())
    for h in range(n):
        palavraOrg = str()
        palavra = raw_input()
        tam = len(palavra)
        tamM= tam/2
        for i in range(tamM-1,-1,-1):
            palavraOrg = palavraOrg + palavra[i]

        for i in range(tam-1,tamM-1,-1):
            palavraOrg = palavraOrg + palavra[i]
        
        print (palavraOrg)



main()