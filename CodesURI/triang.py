



def main():
	
	vet = raw_input()
	vet = vet.split()
	
	for i in range(3):
		vet[i] = float(vet[i])
	vet = sorted(vet)
	A = vet[2]
	B = vet[1]
	C = vet[0]

	if( A < (B+C)):
		if( (A*A) == ( (B*B) + (C*C) ) ):
			print "TRIANGULO RETANGULO"
		elif( (A*A) > ( (B*B) + (C*C) ) ):
			print "TRIANGULO OBTUSANGULO"
		elif( (A*A) < ( (B*B) + (C*C) ) ):
			print "TRIANGULO ACUTANGULO"

		if( A == B == C):
			print "TRIANGULO EQUILATERO"
		elif ( A == B or B == C or A == C):
			print "TRIANGULO ISOSCELES"
	else:
		print "NAO FORMA TRAINGULO"

main()