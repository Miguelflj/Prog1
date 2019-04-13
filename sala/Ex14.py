#UFMT Ccomp
#Ex.14 com While

def main():
	i=1
	resul=1
	b=input("Digite o valor")
	n=input("Digite a expo")
	if (b >= 2) and (n > 1):
		while (i <= n):
			resul = b * resul
			i = i + 1
		print(resul)
	else:
		print("digita certo fdp")
main()