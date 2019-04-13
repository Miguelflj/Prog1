


def main():
   
    n = int(input())
    for h in range(n):
        combin = str()
        entrada = raw_input()
        palavra1,palavra2 = entrada.split()
        
        controle = len(palavra1 + palavra2)
        
        controle1 = len(palavra1)
        controle2 = len(palavra2)
        if(controle1 < controle2):
            m = controle2
        else:
            m = controle1
        for a in range(m):
            if(a < controle1):
                combin = combin + palavra1[a]
            if(a  < controle2):
                combin = combin + palavra2[a]
        print combin
    
main()