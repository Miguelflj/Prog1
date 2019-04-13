

def main():
	s = float(1)
	j = float(3)
	i = float(2)
	while(j <= 39):
		s = s + (j/i)
		i = i * 2
		j += 2
	
	print "%0.2f" %(s)


main()