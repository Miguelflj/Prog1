#UFMT Ccomp

#Ex.15 while

def main():
	lims=input("Digite o limite superior")
	limi=input("Digite o limite inferior")
	while (limi<lims):
		if (limi%6==0):
			print(limi)
		limi = limi + 1

main()