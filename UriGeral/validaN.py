
def main():
    n1 = []
    i = 0
    while i <= 1:
        aux = float(input())
        if(aux >= 0 and aux <= 10.0):
            n1.append(aux)
        else:
            print "nota invalida"
            i -= 1
        i += 1
    media = ((n1[0] + n1[1])/2.0)
    print "media = %0.2f" %(media)
main()