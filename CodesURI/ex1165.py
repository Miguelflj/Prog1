





def main():
	h = int(input())
	i = 0
	while ( i < h ):	
		n = int(input())
		j = 1
		cont  = 0
		while( j <= n):
			if( (n%j)  == 0):
				cont += 1
			j += 1
		if(cont == 2):
			print str(n) + " eh primo"
		else:
			print str(n) + " nao eh primo"
		i += 1




main()