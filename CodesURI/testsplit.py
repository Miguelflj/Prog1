


def main():
	arquivo = open("aluno.txt","r")
	aluno = arquivo.readline()

	nome,n1,n2 = aluno.split()

	print(nome)
	print(n1)
	print(n2)

	
	aluno = arquivo.readline()
	nome,n1,n2 = aluno.split()

	print(nome)
	print(n1)
	print(n2)

main()