#UFMT - Ccomp

#Testes com IF ( Prog1)
#importa biblioteca com funcoes matematicas

import math

def main():
	n=input("Digite um numero:")
	if (n > 0):
		raiz = math.sqrt(n)
		print(raiz)
	elif (n < 0):
		expo = n * n
		#expo = n**2
		print(expo)
	else:
		print("Numero nulo")
main()