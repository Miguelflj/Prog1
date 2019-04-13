def main():
	
	frase = raw_input()
	
        frase_modificada = str()

	contador = 2


	for letra in frase:
		
		if (letra == ' ' or letra == '-'):
			frase_modificada= frase_modificada+letra

		elif (contador%2 == 0):
			frase_modificada= frase_modificada+letra.upper()
			contador += 1
		elif (contador%2 != 0):
			frase_modificada= frase_modificada+letra.lower()
			contador += 1
        a = len(frase_modificada)
                
        print a
	
	print(frase_modificada)


main()