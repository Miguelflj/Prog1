




entrada = raw_input()
t1,t2,t3 = entrada.split()
t1 = int(t1)
t2 = int(t2)
t3 = int(t3)

if( t1 == t2):
    if(t2 < t3):
        print ":)"
    else:
        print ":("
elif( t1 > t2):
    if(t2 <= t3):
        print ":)"
    elif( t2 > t3):
        dif1 = (t1 - t2)
        dif2 = (t2 - t3)
        if(dif1 > dif2):
            print ":)"
        else:
            print ":("
else:
    if(t2 > t3):
        print ":("
    else:
        dif1 = (t2 - t1)
        dif2 = (t3 - t2)
        if(dif1 > dif2):
            print ":("
        else:
            print ":)"