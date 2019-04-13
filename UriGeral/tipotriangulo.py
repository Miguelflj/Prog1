

def main():
    entrada = raw_input()
    a,b,c = entrada.split()
    a = float(a)
    b = float(b)
    c = float(c)
    if(a >= (b + c)):
        print "NAO FORMA TRIANGULO"
    elif(a**2 ==   (b**2 + c**2)):
        print "TRIANGULO RETANGULO"
    elif(a > (b**2 + c**2)**0.5):
        print "TRIANGULO OBTUSANGULO"
    elif(a**2 < (b**2 + c**2)):
        print "TRIANGULO ACUTANGULO"
    if(a == b == c):
        print "TRIANGULO EQUILATERO"
    elif(a == b or a == c or b == c):
        print "TRIANGULO ISOSCELES"

main()
    