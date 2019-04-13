

def main():
    n = int(input())
    for i in range(1,n+1):
        k = i**2
        print str(i) +" "+ str(k) +" "+ str(k*i)
        print str(i) +" "+ str(k+1) +" "+ str(k*i+1)
main()