

mtz = []
for i in range(12):
    mtz.append([0.0]*12)
op = raw_input()

for i in range(12):
    for j in range(12):
        mtz[i][j] = float(input())


soma = 0.0
cont = 0.0

for i in range(12):
    for j in range(12):
        if( (i + j) >= 12 and (j < i ) ):
            soma = mtz[i][j] + soma
            cont += 1.0
            
if( op == "S"):
    soma = float(soma)
    print "%0.1f" %(soma)
elif(op == "M"):
    media = float(soma/cont)
    print "%0.1f" %(media)