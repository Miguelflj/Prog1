


def main():
    x = int(input())
    z = int(input())
    while x >= z:
        z = int(input())
    flag = True
    cont = 0
    somaX = 0
    while flag:
        somaX += x
        cont += 1
        if(somaX > z):
            flag = False
        x += 1
    print(cont)


main()