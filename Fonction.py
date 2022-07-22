# fonction addition
def addition(nb1:int=0, nb2:int=0)->int:
    nb3=nb1+nb2
    return nb3 #Economiser un variable on peut enlever nb3 et ecris return (nb1+nb2)
                #Economiation est fait apres la fin de coder et pas avant

# fonction d'input de nombre
def input_int(message:str)->int:
    carac = input(message)
    try:
        nb = int(carac)
    except ValueError as Ve:
        print("entrer un ENTIER !")
        print(Ve)
        nb = input_int(message)
    return nb
# fonction d'input de nombre
def inputfloatpositif(message:str)->float:
    carac = input(message)
    try:
        nb = float(carac)
        if nb<0:
            print("Positif !!!")
            nb = inputfloatpositif(message)
    except ValueError as Ve:
        print("entrer un nombre !")
        print(Ve)
        nb = inputfloatpositif(message)
    return nb

def input_int_positif(msg:str)->int:
    nbPos = input_int(msg)
    if nbPos < 0:
        print("entrer un POSITIF !")
        nbPos = input_int_positif(msg)
    return nbPos

# print(input_int("Entrer un nombre"))
# print(input_int_positif("quel est votre age?"))
# print(input_int_positif("quel est votre pointure?"))

# nb1 = input_int("entrer nombre 1 : ")
# nb2 = input_int_positif("entrer nombre 2 : ")
# print(addition(nb1,nb2))

def sortingList(ListAtrier:list):
    # parametre l = 0 pour fin trier l = 1 continue trier
    l=0
    # premier passage pour verifier si deja à l'ordre ou il faut trier deux elements
    for i in range(len(ListAtrier)-1):
        if (ListAtrier[i]>ListAtrier[i+1]):
            ListAtrier[i], ListAtrier[i+1] = ListAtrier[i+1], ListAtrier[i]
            # l = 1 pour la recrusivité que c'est toujours besoin de trier
            l=1
    # si l = 1 continue à trier sinon la fonctin se termine
    if l:
        sortingList(ListAtrier)

        