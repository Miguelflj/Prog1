


def main():
    flag = True
    x = int(input())
    if(x == 0):
        flag = False
    while flag:
        soma = 0
        i = 0
        if(x%2 != 0):
            x += 1
        while i <= 4:
            soma += x
            x += 2
            i += 1
        print(soma)
        x = int(input())
        if(x == 0):
            flag = False
        
main()