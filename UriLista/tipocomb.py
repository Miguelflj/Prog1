


def main():
    i = 0
    al = 0
    gas = 0
    dies = 0
    flag = True
    while flag:
        op = int(input())
        if(op == 1):
            al += 1
        elif( op == 2):
            gas += 1
        elif( op == 3):
            dies += 1
        elif(op == 4):
            flag = False
        
        
    print "MUITO OBRIGADO"
    print "Alcool:", (al)
    print "Gasolina:", (gas)
    print "Diesel:", (dies)
            
main()
            