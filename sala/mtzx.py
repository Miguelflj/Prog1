def main():
    mtz = []
    for i in range(5):
        mtz.append([0]*5)
    for i in range(5):
        for j in range(5):
            if(i==j):
                mtz[i][j] = 1
    #i = 4
    #j = 4
    #while (i >= 0):
        #while (j >= 0):
            #if(i==j):
                mtz[0][4] = 1
                mtz[1][3]= 1
                mtz[2][2] = 1
                mtz[3][1] = 1
                mtz[4][0] = 1
                
            #j -= 1
        #i -= 1
                
    for i in range(5):
        print (mtz[i])

main()