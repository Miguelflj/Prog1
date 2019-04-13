
def main():
    x = int(input())
    i = 1
    while(i <= x):
        n = int(input())
        i += 1
        if(n > 0 and n%2 == 0):
            print "EVEN POSITIVE"
        if(n > 0 and n%2 != 0):
            print "ODD POSITIVE"
        if (n < 0 and n%2 == 0):
            print "EVEN NEGATIVE"
        if (n < 0 and n%2 != 0):
            print "ODD NEGATIVE"
        if ( n == 0 ):
            print "NULL"
            
main()