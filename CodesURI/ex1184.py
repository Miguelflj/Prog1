



def main():
	mtz = []
	op = raw_input()
	cont = float(0)
	for i in range(12):
		mtz.append([0]*12)

	for i in range(12):
		for j in range(12):
			mtz[i][j] = float(input())

	soma = 0
	for i in range(12):
		for j in range(12):
			if ( (j >  i) ):
				#print mtz[i][j]
				soma = mtz[j][i] + soma
				cont = cont + 1

	if(op == "S"):
		print "%0.1f" %(soma)
	elif(op == "M" ):
		print "%0.1f" %(soma/cont)


main()