






rep = int(input())

for i in range(rep):
    nn = raw_input()

    nome,forc = nn.split()
    
    if(nome == "Thor"):
        print "Y"
    else:
        print "N"