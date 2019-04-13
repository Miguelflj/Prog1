def encontraMaior(lista):
            if(len(lista) > 0):
                    maior = lista[0]

                    for val in lista:

                            if(val > maior):
                                    maior = val

                    return maior
            else:
                        return -1