

def main():

	qtd = int(input())
	i = 0
	aux = 0

	while (i < qtd):
		soma = 0
		entrada = raw_input()
		x,y = entrada.split()
		x = int(x)
		y = int(y)

		if( (x%2) == 0):
			x += 1

		j = 0
		while(j < y):

			soma = soma + x
			x = x + 2
			j += 1
		print soma
		i += 1

main()