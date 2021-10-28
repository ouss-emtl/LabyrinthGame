from copy import deepcopy
import numpy as np

def deplacement_haut(grille, position) :
    """
    :param grille:
    :param position:
    :return: position acutalisée
    LA FONCTION NE MODIFIE PAS LES ARGUMENTS GRILLE ET POSITION
    """
    i,j = position
    if i == 0 :
        return position
    elif grille[i-1][j] == 0 :
        return position
    else :
        return i-1, j
def deplacement_bas(grille, position) :
    """
    :param grille:
    :param position:
    :return: position acutalisée
    LA FONCTION NE MODIFIE PAS LES ARGUMENTS GRILLE ET POSITION
    """
    n=len(grille)
    i,j = position
    if i == n-1 :
        return position
    elif grille[i+1][j] == 0 :
        return position
    else :
        return i+1, j
def deplacement_gauche(grille, position) :
    """
    :param grille:
    :param position:
    :return: position acutalisée
    LA FONCTION NE MODIFIE PAS LES ARGUMENTS GRILLE ET POSITION
    """
    n=len(grille)
    i,j = position
    if j == 0 :
        return position
    elif grille[i][j-1] == 0 :
        return position
    else :
        return i, j-1
def deplacement_droite(grille, position) :
    """
    :param grille:
    :param position:
    :return: position acutalisée
    LA FONCTION NE MODIFIE PAS LES ARGUMENTS GRILLE ET POSITION
    """
    n=len(grille)
    i,j = position
    if j == n-1 :
        return position
    elif grille[i][j+1] == 0 :
        return position
    else :
        return i, j+1


def deplacement(grille, direction, position ) :
    '''

    :param grille: liste de liste carrée contenant des 0 ou des 1
    :param direction: string dans ['haut', 'bas', 'droite' , 'gauche']
    :param position: couple i,j tels que grille[i][j] soit la position du personnage
    :return: la position du joueur actualisée.
    '''
    i,j=position

    if direction =='bas' :
        return deplacement_bas(grille, position)
    if direction =='haut' :
        return deplacement_haut(grille, position)
    if direction =='droite' :
        return deplacement_droite(grille, position)
    if direction =='gauche' :
        return deplacement_gauche(grille, position)
    return (i,j)

def actualisation_grille_eclairage(grille_eclairage, position, portee_eclairage):
    """
    Renvoie la grille éclairage mise à jour
    1 si éclairé
    0 sinon
    :param grille_eclairage:
    :param position:
    :param portee_eclairage:
    :return: grille_eclairage
    """
    n = len(grille_eclairage)
    nouvelle_grille_eclairage = deepcopy(grille_eclairage)
    x, y = position
    for i in range(x-portee_eclairage, x+portee_eclairage+1):
        for j in range(y-portee_eclairage, y+portee_eclairage+1):
            if i>=0 and i<n and j>=0 and j<n:
                nouvelle_grille_eclairage[i][j] = 1
    return nouvelle_grille_eclairage



def affichage_console(vue) :
    print(np.array(vue))

def commande_joueur() :
    a=input()
    assert a in ['z','q','s','d']
    if a == 'z' :
        return 'haut'
    elif a=='q' :
        return 'gauche'
    elif a=='s' :
        return 'bas'
    elif a=='d' :
        return 'droite'

def partie_terminee(grille, position) :
    i,j=position
    return grille[i][j]==2

def sur_une_tnt(grille, position):
    x,y = position
    return grille[x][y] == 4

def creer_vue(grille, grille_eclairage, position, portee_affichage):
    def vue_unique(vue_grille, vue_grille_eclairage):
       """
       Condense les deux vues pour avoir un mvp plus lisible
       -1 : hors de la grille
       0: mur et/ou zone non éclairée
       1: vide éclairé
       :param vue_grille:
       :param vue_grille_affichage:
       :return:
       """
       n = len(vue_grille)
       vue = deepcopy(vue_grille)
       for i in range(n):
           for j in range(n):
               if (vue_grille[i][j] != 0) and vue_grille_eclairage[i][j] == 0:
                   vue[i][j] = 0

       return vue


    def creer_deux_vues(grille, grille_eclairage, position, portee_affichage):
        """
        Une vue est un couple de matrice (vue_grille, vue_grille_eclairage)
        Génère la vue, les matrices carrées sont de taille (2*portee_affichage+1)
        :param grille:
        :param grille_eclairage:
        :param position:
        :param portee_affichage:
        :return: (vue_grille, vue_grille_eclairage)
        """
        vue_grille = [[0 for i in range(2*portee_affichage+1)] for j in range(2*portee_affichage+1)]
        vue_grille_eclairage = [[0 for i in range(2*portee_affichage+1)] for j in range(2*portee_affichage+1)]
        x, y = position
        n = len(grille)
        for i in range(x-portee_affichage, x+portee_affichage+1):
            for j in range(y-portee_affichage, y+portee_affichage+1):
                if i>=0 and i<n and j>=0 and j<n:
                    vue_grille[i-(x-portee_affichage)][j-(y-portee_affichage)] = grille[i][j]
                    vue_grille_eclairage[i-(x-portee_affichage)][j-(y-portee_affichage)] = grille_eclairage[i][j]
                else:
                    vue_grille[i-(x-portee_affichage)][j-(y-portee_affichage)] = -1
                    vue_grille_eclairage[i-(x-portee_affichage)][j-(y-portee_affichage)] = -1
        return (vue_grille, vue_grille_eclairage)

    a, b = creer_deux_vues(grille, grille_eclairage, position, portee_affichage)
    return vue_unique(a,b)

def jouer_mvp() :
    """
    Permet simplement de jouer avec un affichage matrice
    """
    portee_eclairage = 3
    portee_affichage = 6
    position_initiale = [7,7]

    #grille : 0=mur / 1=vide / 2=sortie
    grille_eclairage = [[0 for i in range(16)] for j in range(16)]
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    position = position_initiale
    grille_eclairage = actualisation_grille_eclairage(grille_eclairage, position, portee_eclairage)
    vue = creer_vue(grille, grille_eclairage, position, portee_affichage)
    affichage_console(vue)
    while not partie_terminee(grille, position) :
        direction = commande_joueur()
        vue, grille_eclairage, position = infos_apres_deplacement(grille, grille_eclairage, position, direction, portee_eclairage, portee_affichage)
        affichage_console(vue)
    print("C'est gagné")

def infos_apres_deplacement(grille, grille_eclairage, position, direction, portee_eclairage, portee_affichage):
    """
    Donne toutes les infos utiles à l'affichage après un déplacement
    """
    nouvelle_position = deplacement(grille, direction, position)
    grille_eclairage = actualisation_grille_eclairage(grille_eclairage, nouvelle_position, portee_eclairage)
    vue = creer_vue(grille, grille_eclairage, nouvelle_position, portee_affichage)
    return vue, grille_eclairage, nouvelle_position

def position_initiale(grille):
    n = len(grille)
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 5:
                return (i,j)
