from Mediamtz import MediaMtz

def main():
    tamL = input()
    tamC = input()
    mtz = []
    k = 1
    for i in range(tamL):
        mtz.append([0]*tamC)
        
    for i in range(tamL):
        for j in range(tamC):
            mtz[i][j] = k
            k = k + 1
    print mtz
    media = MediaMtz(mtz,tamL,tamC)
    
    print media
main()