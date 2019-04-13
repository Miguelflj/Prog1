

def main():
    fat = 1
    n = int(input())
    while(n >= 1):
        fat = n * fat
        n -= 1
    print (fat)
    x = fat + 5
    print "O valor de x é: " + str(x)
main()