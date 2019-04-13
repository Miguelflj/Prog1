#UFMT CCOMP
#LISTA 1 MEDIA COM PESOS
#MIGUEL FREITAS

def main():
    entrada = raw_input()
    n1,n2,n3,n4 = entrada.split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    media = ((n1*2)+(n2*3)+(n3*4)+(n4))/10
    print "Media: %0.1f" % (media)
    if (media >= 7.0):
        print "Aluno aprovado."
    if (media >= 5.0 and media <= 6.9):
        print "Aluno em exame."
        ne = float(input())
        media = (ne + media) /2
        print "Nota do exame: %0.1f" % (ne)
        if (media >= 5.0):
            print "Aluno aprovado."
            print "Media final: %0.1f" % (media)
        else:
            print "Aluno reprovado."
            print "Media final: %0.1f" % (media)
    if (media < 5.0):
        print "Aluno reprovado."
            
main()