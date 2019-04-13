




def main():
	i = 0
	y = int(input())
	while (i < y) :
		entrada = raw_input()
		she,raj = entrada.split()
		if( she == raj):

			print "Caso #" + str(i) + ": De novo!"

  		else:

  			if(she == "pedra"):

  				if(raj == "lagarto" | raj == "tesoura"):
  					print "Caso #" + str(i) + ": Bazinga!"
  				else:
  					print "Caso #" + str(i) + ": Raj trapaceou!"
 			elif(she == "papel"):

  				if(raj == "pedro" | raj == "Spock"):
  					print "Caso #" + str(i) + ": Bazinga!"
  				else:
  					print "Caso #" + str(i) + ": Raj trapaceou!"
 			elif(she == "tesoura"):

  				if(raj == "papel" | raj == "lagarto"):
  					print "Caso #" + str(i) + ": Bazinga!"
  				else:
  					print "Caso #" + str(i) + ": Raj trapaceou!"
 			elif(she == "lagarto"):

  				if(raj == "Spock" | raj == "papel"):
  					print "Caso #" + str(i) + ": Bazinga!"
  				else:
  					print "Caso #" + str(i) + ": Raj trapaceou!"
 			elif(she == "Spock"):

  				if(raj == "tesoura" | raj == "pedra"):
  					print "Caso #" + str(i) + ": Bazinga!"
  				else:
  					print "Caso #" + str(i) + ": Raj trapaceou!"
 main()