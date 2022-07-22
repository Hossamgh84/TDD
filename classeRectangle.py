class BoiteChaussure():
    _longueur:float
    _largeur:float
    _hauteur:float

    def __init__(self,longueur:float,largeur:float,hauteur:float):
        self.set_longueur(longueur)
        self.set_largeur(largeur)
        self.set_hauteur(hauteur)

    # getters
    def get_longueur(self):
        return self._longueur
    def get_largeur(self):
        return self._largeur
    def get_hauteur(self):
        return self._hauteur

    # setters
    def set_longueur(self,longueur):
        if longueur<=0:
            print("longueur invalide") 
        else:
            self._longueur=longueur

    def set_largeur(self,largeur):
        if largeur<=0:
            print("largeur invalide") 
        else:
            self._largeur=largeur

    def set_hauteur(self,hauteur):
        if hauteur<=0:
            print("hauteur invalide") 
        else:
            self._hauteur=hauteur

    # methodes

    def calculVolume(self):
        return self.get_hauteur()*self.get_largeur()*self.get_hauteur()
    def calculSurface(self):
        return self.get_hauteur()*self.get_largeur()

    def affichage(self):
        print("Cette boite a une longueur : {:} cm\nune largeur : {:} cm\net une hauteur de : {:}".format(self.get_longueur(),self.get_largeur(),self.get_hauteur()))
        print("sa surface est : {:0.2f} cm^2\net son volume est : {:0.2f} cm^3".format(self.calculSurface(),self.calculVolume()))
