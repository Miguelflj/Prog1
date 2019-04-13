def Fibonacci(n,x,y):
    if(n  == 0):
        return 0
    if(n > 1):
        return y + Fibonacci(n -1,y , x + y)
    else:
        return 1
        
def main():
    n = int(input('Posicao: '))
    fibo = Fibonacci(n,1,0)
    print (fibo)
main()