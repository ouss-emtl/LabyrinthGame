import numpy as np
import random
import numpy as np
##Randomisateur



def est_disponible(position,grille):
    """return une liste de booléens qui décrit si les cases [droite,gauche,haut,bas] sont disponibles pour rajouter un mur"""
    disponibilites=[]
    if grille[position[0]+1][position[1]] == 0:
        if grille[position[0]+2][position[1]] == 0 and grille[position[0]+1][position[1]+1] == 0 and grille[position[0]+1][position[1]-1] == 0:
            disponibilites.append("down")
    if grille[position[0]-1][position[1]] == 0:
        if grille[position[0]-2][position[1]] == 0 and grille[position[0]-1][position[1]+1] == 0 and grille[position[0]-1][position[1]-1] == 0:
            disponibilites.append("up")
    if grille[position[0]][position[1]+1] == 0:
        if grille[position[0]][position[1]+2] == 0 and grille[position[0]-1][position[1]+1] == 0 and grille[position[0]+1][position[1]+1] == 0:
            disponibilites.append("right")
    if grille[position[0]][position[1]-1] == 0:
        if grille[position[0]][position[1]-2] == 0 and grille[position[0]+1][position[1]-1] == 0 and grille[position[0]-1][position[1]-1] == 0:
            disponibilites.append("left")
    return disponibilites

def branche_aleatoire_init(size_lab):
    #initialisation grille
    arrivee_disponible=[]
    while arrivee_disponible == []:
        grille = [[0 for i in range(size_lab+2)] for j in range(size_lab+2)]
        grille[0]=[-1 for i in range(size_lab+2)]
        grille[size_lab+1]=[-1 for i in range(size_lab+2)]
        for j in range (1,size_lab+1):
            grille[j][0]=-1
            grille[j][size_lab+1] = -1
        curseur=[size_lab//2+1,size_lab//2+1]
        grille[size_lab//2+1][size_lab//2+1]=1
        #tracé du chemin aléatoire
        while len(est_disponible(curseur,grille)) != 0:
            disponibilites = est_disponible(curseur,grille)
            random_direction = disponibilites[random.randint(0 , len(disponibilites)-1)]
            if random_direction == "down":
                curseur[0] += 1
            if random_direction == "up":
                curseur[0] -= 1
            if random_direction == "right":
                curseur[1] += 1
            if random_direction == "left":
                curseur[1] -= 1
            grille[curseur[0]][curseur[1]] = 1
        #on ajoute l'arrivée à la fin de ce premier chemin
        if grille[curseur[0]+2][curseur[1]] == -1:
            arrivee_disponible.append((curseur[0]+1,curseur[1]))
        if grille[curseur[0]-2][curseur[1]] == -1:
            arrivee_disponible.append((curseur[0]-1,curseur[1]))
        if grille[curseur[0]][curseur[1]+2] == -1:
            arrivee_disponible.append((curseur[0],curseur[1]+1))
        if grille[curseur[0]][curseur[1]-2] == -1:
            arrivee_disponible.append((curseur[0],curseur[1]-1))
    arrivee=random.choice(arrivee_disponible)
    grille[arrivee[0]][arrivee[1]]=2
    return np.array(grille)
#print(branche_aleatoire_init(15))

def recupere_positions_vides(grille):
    """Renvoie une liste avec les couples de positions ou il y a un passage (vide)"""
    couples = []
    n = len(grille)
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 1:
                couples.append([i,j])
    return couples

def proportion_remplissage(grille):
    return len(recupere_positions_vides(grille))/(len(grille)**2)

#print(proportion_remplissage(grille))

def grille_totale(size_lab,proportion):
    grille=branche_aleatoire_init(size_lab)
    while proportion_remplissage(grille) <  proportion:
        curseur=random.choice(recupere_positions_vides(grille))
        while len(est_disponible(curseur,grille)) != 0:
            disponibilites = est_disponible(curseur,grille)
            random_direction = disponibilites[random.randint(0 , len(disponibilites)-1)]
            if random_direction == "down":
                curseur[0] += 1
            if random_direction == "up":
                curseur[0] -= 1
            if random_direction == "right":
                curseur[1] += 1
            if random_direction == "left":
                curseur[1] -= 1
            grille[curseur[0]][curseur[1]] = 1
    #on retourne la grille sans les -1
    grille_propre = [[0 for i in range(size_lab)] for i in range (size_lab)]
    for i in range (size_lab):
        for j in range (size_lab):
            grille_propre[i][j]=grille[i+1][j+1]
    return np.array(grille_propre)


