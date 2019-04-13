


def main():
    classe = raw_input()
    grupo = raw_input()
    familia = raw_input()
    if(classe == "vertebrado"):
        if(grupo == "ave"):
            if(familia == "carnivoro"):
                print "aguia"
            if(familia == "onivoro"):
                print "pomba"
        if(grupo == "mamifero"):
            if(familia == "onivoro"):
                print "homem"
            if(familia == "herbivoro"):
                print "vaca"
    if(classe == "invertebrado"):
        if(grupo == "inseto"):
            if(familia == "hematofago"):
                print "pulga"
            if(familia == "herbivoro"):
                print "lagarta"
        if(grupo == "anelideo"):
            if(familia == "hematofago"):
                print "sanguessuga"
            if(familia == "onivoro"):
                print "minhoca"
                
main()