#UFMT CCOMP
#LISTA 1 VALORES IMPARES CONSECUTIVOS
#MIGUEL FREITAS

def main():
    x = int(input())
    i = x
    y = x
    if ( x%2 != 0):
        y -=1
    while (i <= (y + 6)):
        if ( i%2 != 0):
            print (i)
            y +=1
            
        i += 1
        
main()