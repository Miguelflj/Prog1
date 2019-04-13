


def main():
	i = 0
	n = int(input())

	while(i < n):
		j = 1
		soma = 0
		teste = int(input())
		while( j < teste):
			if( (teste%j) == 0):
				soma = soma + j
			j += 1

		if(teste == soma):
			print str(teste) + " eh perfeito"
		else:
			print str(teste) + " nao eh perfeito"

		i += 1
	


main()