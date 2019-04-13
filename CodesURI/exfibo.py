



def main():
	fibo = [];
	fibo.append(0)
	fibo.append(1)
	fibo.append(1)
	qtd = int(input())
	i = 0
	j = 2
	x = 0
	while(x < qtd):
		pos = int(input())
		if( pos > j):
			while(j < pos):
				j = j+1
				fibo.append(fibo[j-1] + fibo[j-2])
				
			print "Fib("+ str(pos) +") =",fibo[pos]
		else:

			print "Fib("+ str(pos) + ") =",fibo[pos]
		x = x +1 

	
main()