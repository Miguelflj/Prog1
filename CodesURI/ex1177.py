




def main():

	comp = int(input())
	i = 0
	j = 0
	while (i < 1000):
		if(j < comp):
			print "N[" + str(i)+"] =",j
		else:
			j = 0	
			print "N[" + str(i)+"] =",j

		j += 1
		i += 1

main()