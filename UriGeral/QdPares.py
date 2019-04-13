
def main():
    N = int(input())
    for i in range(1,N+1):
        if (i%2 == 0):
            resul = (i*i)
            print str(i)+"^2 = " + str(resul)
    
    
main()