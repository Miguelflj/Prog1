#UFMT- Ccomp
# Exerc. com If, elif e else

def main():
	n=input("Digite um valor:")
	if ((n % 10) == 0):
		print("Eh divisivel por 10")
	elif((n % 5) == 0):
		print("Eh divisivel por 5")
	elif((n % 2) == 0):
		print("Eh divisivel por 2")
	else:
		print("Nao eh divisivel por 10,5 e 2 ")

main()