



def main():
	i = 0
	par = [None] * 5
	contp = 0
	conti = 0
	impar = [None]* 5
	aux = 0
	while(i < 15):
		n = int(input())
		if(n%2 == 0):
			par[contp] = n
			contp += 1
		else:
			impar[conti] = n
			conti += 1


		if(contp == 5):
			while(aux < contp):
				print "par[" + str(aux)+ "] =",par[aux]
				aux += 1
			contp = 0
		aux = 0

		if(conti == 5):
			while(aux < conti):
				print "impar[" + str(aux)+ "] =",impar[aux]
				aux += 1
			conti = 0

		i += 1
	i = 0
	while(i < conti):
		print "impar[" + str(i)+ "] =",impar[i]
		i += 1
	i = 0
	while(i < contp):
		print "par[" + str(i)+ "] =",par[i]
		i += 1


main()