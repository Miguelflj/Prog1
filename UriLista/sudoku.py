

TamL = 9
TamC = 9
TamV = 9
def veLinha(mtz):
	vet = []
	for i in range(TamV):
		vet.append(0);

	for i in range(TamL):
		#zera vetor
		for k in range(TamV):
			vet[k] = 0

		for j in range(TamC):
			pos = mtz[i][j] - 1
			vet[pos] = 1
		#ve vetor 
		for l in range(TamV):
			if(vet[l] == 0):			
				return -1
	return 1


def veColuna(mtz):
	vet = []
	for i in range(TamV):
		vet.append(0);

	for i in range(TamL):
		#zera vetor
		for k in range(TamV):
			vet[k] = 0

		for j in range(TamC):
			pos = mtz[j][i] - 1
			vet[pos] = 1

		#ve vetor 
		for l in range(TamV):
			if(vet[l] == 0):
				return -1
	return 1

def VeQD(mtz,poslIn,poscIn,poslFin,poscFin):
	vet = []
	for i in range(TamV):
		vet.append(0);

	for k in range(TamV):
		vet[k] = 0

	for i in range(poslIn,poslFin):
		for j in range(poscIn,poscFin):
			pos = mtz[i][j] - 1
			vet[pos] = 1
	for l in range(TamV):
		if(vet[l] == 0):
			return -1
	return 1

def main():
	inst = int( input() )
	for h in range(inst):
		flag = 1
		#aloca mtz
		sdk = []
		for i in range(TamL):
			sdk.append([0]*9)
		#arq = open("entradaSDK.txt","r")
		#inputsdk = arq.readlines()
		#lê 144 valores

		for i in range(TamL):
			vet = []
			#vet = list(map(int,inputsdk[i].split()))
			entrada = str(input())
			vet = list( map(int,entrada.split() ) )
			for j in range(TamC):
				sdk[i][j] = vet[j]

		flag = veLinha(sdk)
		if(flag == 1):
			flag = veColuna(sdk)
		poslIn = 0
		poscIn = 0
		poslFin = 3
		poscFin = 3
		if(flag == 1):
			while(poslFin <= 9):

				flag = VeQD(sdk,poslIn,poscIn,poslFin,poscFin)
				if(poscFin != 9):
					poscIn = poscFin
					poscFin += 3
				else:
					poslIn = poslFin
					poslFin += 3

		print("Instancia",h+1)

		if(flag == 1):
			print("SIM")
		else:
			print("NAO")
		print("")

main()


