


def main():
    flag = True
    x = int(input())
    if(x == 0):
        flag = False
    while flag:
        for i in range(1,x+1):
            if(i != x):
                print (i),
            else:
                print (i)
            
        x = int(input())
        if(x == 0):
            flag = False





main()