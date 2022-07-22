"""
Rectangle POO

Ecrire une classe Rectangle permettant de construire des rectangles
Ils se carracterisent par une longueur et une largeur largeur.

Un Rectangle doit posseder 2 methodes :
    - affichage(), permettant d'afficher les informations du rectangle.
    - Surface(), permettant de calculer la surface du rectangle.
    
"""
from classeRectangle import BoiteChaussure

from Fonction import inputfloatpositif


vLngr=inputfloatpositif("Entrer le longueur :")
vLrgr=inputfloatpositif("Entrer le largeur :")
vHtr=inputfloatpositif("Entrer l'hauteur")
uneBoite01=BoiteChaussure(vLngr,vLrgr,vHtr)
uneBoite01.affichage()
