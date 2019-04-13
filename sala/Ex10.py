#UFMT- Ccomp

# Teste IF ( prog1)

#Chamada de biblioteca
import math

def main():
	n=input("Digite um valor:")
	resto = n % 3
	if (resto == 0):
		print("Eh multiplho de 3")
	else:
		print("Nao eh multiplo de 3")
main()