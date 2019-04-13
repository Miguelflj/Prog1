# UFMT - Prog1
# Prof. Ivairton
#
# Exercicio para manipulacao de arquivos,
# funcoes e matrizes
#

## Funcao que calcula e retornar o somatorio dos valores da mtz ##
def somatorioMtz(mtz, nl, nc):
    s = 0
    for i in range(nl):
        for j in range(nc):
            s = s + mtz[i][j]
    return s


## Funcao que calcula a soma dos valores por linha, constroi um vetor e retorna-o ##
def somaLinha(mtz, nl, nc):
    vetSoma = []
    for i in range(nl):
        s = 0
        for j in range(nc):
            s = s + mtz[i][j]
        vetSoma.append(s)
    return vetSoma


## Funcao que calcula a soma dos valores por coluna, constroi um vetor e retorna-o ##
def somaColuna(mtz, nl, nc):
    vetSoma = []
    for j in range(nc):
        s = 0
        for i in range(nl):
            s = s + mtz[i][j]
        vetSoma.append(s)
    return vetSoma


## Funcao que encontra o menor valor presente na mtz ##
def menor(mtz, nl, nc):
    val = mtz[0][0]
    for i in range(nl):
        for j in range(nc):
            if val > mtz[i][j]:
                val = mtz[i][j]
    return val


## Funcao que encontra o maior valor presente na mtz ##
def maior(mtz, nl, nc):
    val = mtz[0][0]
    for i in range(nl):
        for j in range(nc):
            if val < mtz[i][j]:
                val = mtz[i][j]
    return val


### Funcao principal do programa ###
def main():
    arquivo = open("entrada.txt", "r")
    # Considere testar as funcoes
    # read()
    # readline()
    # readlines()

    # Faz a leitura da primeira linha em separado
    strLinha = arquivo.readline()

    # A funcao split quebra a linha em um vetor, contendo os valores (separados por espacos)
    valores = strLinha.split()

    nLinhas = int(valores[0]) #armazena num linhas
    nColunas = int(valores[1]) #armazena num colunas

    #incializa a matriz com zeros
    mtz = []
    for i in range(nLinhas):
        mtz.append([0] * nColunas)

    # aqui sera usado uma iteracao diretamente no arquivo
    # eh importante saber que a posicao de leitura no arquivo nao se altera (continua da onde estavamos)
    contLinhas = 0 #contador da posicao da linha
    for strLinha in arquivo:
        valores = strLinha.split()
        #partindo do principio que o arquivo estah corretamente estruturado, podemos determinar o laco pelo numero de colunas, ou o tamanho do vetor
        for contColunas in range(nColunas):
            mtz[contLinhas][contColunas] = int(valores[contColunas])
        contLinhas += 1

    arquivo.close()

    #Chama a funcao que calcula o somatorio de valores da matriz
    somatorio = somatorioMtz(mtz, nLinhas, nColunas)

    #Chama a funcao que calcula a soma dos valores por linhas
    somaPorLinha = somaLinha(mtz, nLinhas, nColunas)

    #Chama funcao que calcuala a soma por coluna
    somaPorColuna = somaColuna(mtz, nLinhas, nColunas)

    #Chama funcao que encontra o menor valor na mtz
    menorValor = menor(mtz, nLinhas, nColunas)

    #Chama funcao que encontra o maior valor na mtz
    maiorValor = maior(mtz, nLinhas, nColunas)

    arquivo = open("saida.txt", "w")
    string = ( "Matriz com tamanho: " + str(nLinhas) + " x " + str(nColunas) + "\n")
    arquivo.write(string)
    arquivo.write("Matriz:")
    arquivo.write(str(mtz))
    arquivo.write("\n")
    arquivo.write("Somatorio: " + str(somatorio) + "\n")
    arquivo.write("Soma da linhas: " + str(somaPorLinha) + "\n")
    arquivo.write("Soma das colunas: " + str(somaPorColuna) + "\n")
    arquivo.write("Maior valor: " + str(maiorValor) + " e Menor valor: " + str(menorValor) + "\n")
    arquivo.close()

main()