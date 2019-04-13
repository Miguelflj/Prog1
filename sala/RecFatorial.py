def CalculaFatorial(n):
    if(n == 1):
        return 1
    else:
        return(n * CalculaFatorial(n - 1))
        

def main():
    n = int(input())
    
    fat = CalculaFatorial(n)
    print (fat)
    x = fat + 5
    print "O valor de x é: " + str(x)
main()