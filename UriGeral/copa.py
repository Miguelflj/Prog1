






flag = True
while(flag):
    try:
        entrada = int(input())

        if(entrada == 0):
                print ("vai ter copa!")
        else:
                print ("vai ter duas!")

    except EOFError:
        flag = False

