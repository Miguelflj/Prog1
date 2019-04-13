#UFMT CCOMP
#CALCULA TEMPO DE EVENTO 
#MIGUEL FREITAS




def main():
    #LEITURA DE FIM
    entrada = raw_input()
    d,diaI = entrada.split() # VARIAVEL (d) usada para descarte de texto
    diaI = int(diaI)
    entrada1 = raw_input()
    horaI,minuI,segI = entrada1.split(" : ")
    
    horaI = int(horaI)
    minuI = int(minuI)
    segI = int(segI)
    #LEITURA DE FIM
    entrada2 = raw_input()
    d,diaF = entrada2.split() # VARIAVEL (d) usada para descarte de texto
    diaF = int(diaF)
    entrada3 = raw_input()
    horaF,minuF,segF = entrada3.split(":")
    
    horaF = int(horaF)
    minuF = int(minuF)
    segF = int(segF)
    
    
    #TRANSFORMANDO TUDO EM SEGUNDO
    inicioEve = (segI + (minuI*60) + (horaI*60*60) + (diaI*60*60*24))
    fimEve =  (segF + (minuF*60) + (horaF*60*60) + (diaF*60*60*24))
    tempo = (fimEve - inicioEve) # fazendo a diferenca( nao se deve colocar cecidilia, da erro no Uri) do fim pelo inicio
    
    EventoD = tempo//86400
    
    print (str(EventoD) + " dia(s)")
    
    tempo = tempo%86400
    
    EventoH = tempo/3600
    
    print (str(EventoH) + " hora(s)")
    
    tempo=tempo%3600
    
    EventoM = tempo/60
    
    print (str(EventoM)+ " minuto(s)")
    
    EventoS = tempo%60
    
    print (str(EventoS) + " segundo(s)")

main()