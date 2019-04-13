
#MIGUEL FREITAS UFMT CCOMP

def main():


	dic = ["D"]
	qtd_t = int( input() )
	mtz = []
	for i in range(4):
		mtz.append([0]*4)

	for i in range(qtd_t):
		flagNONE = 0
		flagDown = 0
		flagUp = 0
		flagRight = 0
		flagLeft = 0

		for j in range(4):
			entrada = str(input())
			in0,in1,in2,in3 = entrada.split()

			mtz[j][0] = int(in0)
			mtz[j][1] = int(in1)
			mtz[j][2] = int(in2)
			mtz[j][3] = int(in3)

		#verifica se o jogo já esta terminado		
		for i in range(4):
			for j in range(4):
				if( mtz[i][j] == 2048):
					flagNONE = 1

		#Down
		for i in range(3):
			for j in range(4):
				if(   ( ( mtz[i][j] != 0 ) and  ( mtz[i+1][j] == 0 ) ) or ( mtz[i][j] == mtz[i+1][j] ) and mtz[i][j] != 0 ):
					flagDown = 1
		#Up
		for i in range(1,4):
			for j in range(4):
				if(  ( ( mtz[i][j] != 0 ) and ( mtz[i-1][j] == 0 ) ) or ( mtz[i][j] == mtz[i-1][j]  ) and mtz[i][j] != 0 ):
					flagUp = 1
		#Right
		for i in range(4):
			for j in range(3):
				if( ( (mtz[i][j] != 0) and (mtz[i][j+1] == 0) ) or ( mtz[i][j] == mtz[i][j+1] ) and mtz[i][j] != 0 )  :
					flagRight = 1

		#Left			
		for i in range(4):
			for j in range(1,4):
				if( ( ( mtz[i][j] != 0)  and ( mtz[i][j-1] == 0 ) ) or ( mtz[i][j] == mtz[i][j-1]) and mtz[i][j] != 0 ):
					flagLeft = 1

		if( flagNONE):
			print("NONE")
		elif(flagDown != 1 and flagLeft != 1 and flagRight != 1 and flagUp != 1):
			print("NONE")
		else:
			marc = 1
			if(flagDown):
				print("DOWN",end="")
				marc = 0
			if(flagLeft):
				if(marc):
					print("LEFT",end="")
				else:
					print(" LEFT",end="")
				marc = 0
			if(flagRight):
				
				if(marc):
					print("RIGHT",end="")
				else:
					print(" RIGHT",end="")
				marc = 0
			if(flagUp):
				if(marc):
					print("UP",end="")
				else:
					print(" UP",end="")
					
			print("")
			


main()