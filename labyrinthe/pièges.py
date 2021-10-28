import pygame
from numpy import random as rd




import random as rd
def element_aleatoire_liste(liste):
    n = len(liste)
    m= rd.randint(0,n-1)
    return liste[m]



def direction_possible(direction,position,grille):
    n = len(grille)
    i,j = position
    if direction == "droite":
        if j!=n-1:
            if grille[i][j+1]!=0:
                return True
    if direction == "gauche":
        if j>0:
            if grille[i][j-1]!=0:
                return True
    if direction == "haut":
        if i>0:
            if grille[i-1][j]!=0:
                return True
    if direction == "bas":
        if i!=n-1:
            if grille[i+1][j]!=0:
                return True
    return False


def liste_direction_possible(position,grille):
    res = []
    direction = ["gauche","droite","haut","bas"]
    for x in direction:
        if direction_possible(x,position,grille):
            res.append(x)
    return res


def deplacer_position(direction,position):
    position_copy = position
    if direction == "gauche":
        position_copy = (position_copy[0]-1,position_copy[1])
    if direction == "droite":
        position_copy = (position_copy[0]+1,position_copy[1])
    if direction == "haut":
        position_copy = (position_copy[0],position_copy[1]-1)
    if direction == "bas":
        position_copy = (position_copy[0],position_copy[1]+1)
    return position_copy

def grille_sans_piege(grille_piege):
    grille_copy = grille_piege.copy()
    n=len(grille_piege)
    for k in range(n):
        for j in range(n):
            if grille_piege[k][j]==3:
                grille_copy[k][j]=1
    return grille_copy







def direction_avant(direction_precedente):
    #donne la liste des directions permettant d'aller vers l'avant selon la direction précédente
    if direction_precedente == "gauche":
        return ["gauche","haut","bas"]
    if direction_precedente == "droite":
        return ["droite","haut","bas"]
    if direction_precedente == "bas":
        return ["gauche","droite","bas"]
    if direction_precedente == "haut":
        return ["gauche","droite","haut"]

def direction_avant_possible(direction_precedente, position, grille):
    # nous dit si on peut avancer ver l'avant ou non
    forward_direction = direction_avant(direction_precedente)
    for x in forward_direction:
        if direction_possible(x,position,grille):
            return True
    return False

def avancer_de_l_avant(direction_précédente, position, grille):
    #nous avance vers l'avant de manière aléatoire
    possible_direction = direction_avant(direction_précédente)
    choix_direction = element_aleatoire_liste(possible_direction)
    position = deplacer_position(choix_direction,position)
    return (position,choix_direction)


"""
def trouver_chemin(position, grille):
    #Permet de trouver une solution possible en testant toutes
    #solutions possibles
    grille_copy = grille.copy()
    position_copy = position
    possible_direction = liste_direction_possible(position, grille_copy)
    for x in possible_direction:
        chemin=[]
        index_cases_deja_faite =[]
        position = deplacer_position(x,position)
        chemin.append(grille_copy[position[0]][position[1]])
        index_cases_deja_faite.append(position)
        direction_precedente = x
        while direction_avant_possible(direction_precedente, position, grille_copy) :#tant qu'on peut avancer de l'avant
            position, direction_precedente = avancer_de_l_avant(direction_precedente,position,grille)
            #on avance de l'avant de manière aléatoire
            if position not in index_cases_deja_faite:# on vérifie qu'on est pas passé par cette case
                chemin.append(grille_copy[position[0]][position[1]])
                index_cases_deja_faite.append(position)
                print(index_cases_deja_faite)
                if 2 in chemin: #on vérifie si ce chemin est bien la solution
                    return index_cases_deja_faite

        if 2 in chemin:
            return index_cases_deja_faite
        else:
            for indexes in index_cases_deja_faite:
                grille_copy[indexes[0]][indexes[1]]=0
            position = position_copy #On revient à la position initiale

def trouver_chemin_bis(position, grille):
    grille_copy = grille.copy
    possible_direction = liste_direction_possible(position, grille_copy)
    for x in possible_direction:
        chemin=[]
        index_chemin =[]
        position = deplacer_position(x,position)
        chemin.append(grille_copy[position[0]][position[1]])
        index_chemin.append(position)
        direction_precedente = x
        while direction_avant_possible(direction_precedente, position, grille_copy) :
            grille_copy[position[0]][position[1]]=0
            #tant qu'on peut avancer de l'avant
            position, direction_precedente = avancer_de_l_avant(direction_precedente, position, grille)
            #on avance de l'avant de manière aléatoire
            chemin.append(grille_copy[position[0]][position[1]])
            index_chemin.append(position)
            print(chemin)
            if 2 in chemin:
                return index_chemin

print(trouver_chemin_bis((7,7),grille))


def liste_case_sans_solution(grille,position_depart):
    chemin = trouver_chemin(position_depart,grille)
    chemin_sans_solution = []
    n=len(grille)
    for i in range(n):
        for j in range (n):
            if (i,j) not in chemin:
                chemin_sans_solution.append((i,j))
    return chemin_sans_solution





def generer_piege (grille,position_depart):#crée un piège aléatoirement sur une case vide
    grille_copy = grille.copy()            #Ne modifie pas la grille initiale
    chemin_sans_solution = liste_case_sans_solution(grille,position_depart)
    m = len(chemin_sans_solution)//2
    chemin_sans_solution = chemin_sans_solution[:m]
    for x in chemin_sans_solution:
        grille_copy[x[0]][x[1]] = 3
"""
def grille_piege_vu(grille,piege_vu):#Modifie la grille initiale en ajoutant les pièges vus
    for x in piege_vu:               #au fur et à mesure
        grille[x[0]][x[1]]=3
    return grille



def afficher_jeu_piege_vue(vue, fenetre,direction,compteur_sprite):
    largeur=50
    size=13
    for i in range (size):
        for j in range(size):
            if vue[j][i] == -1:
                pygame.draw.rect(fenetre,[120,120,120],(i*largeur,j*largeur,largeur,largeur))
            if vue[j][i] == 1:
                pygame.draw.rect(fenetre,[255,255,255],(i*largeur,j*largeur,largeur,largeur))
            if vue[j][i] == 0:
                pygame.draw.rect(fenetre,[0,0,0],(i*largeur,j*largeur,largeur,largeur))
            if vue[j][i] == 2:
                pygame.draw.rect(fenetre,[0,255,0],(i*largeur,j*largeur,largeur,largeur))
            if vue[j][i] == 3:
                pygame.draw.rect(fenetre, [255,255,0], (i * largeur, j * largeur, largeur, largeur))
            if vue[j][i] == 4:
                pygame.draw.rect(fenetre, [255,255,255], (i * largeur, j * largeur, largeur, largeur))
                image_TNT = pygame.image.load("Images\TNT.jpg").convert()
                image_TNT.set_colorkey((255,255,255))
                fenetre.blit(image_TNT, (i * largeur, j * largeur))
            if vue[j][i] == 5:
                pygame.draw.rect(fenetre,[255,255,255],(i*largeur,j*largeur,largeur,largeur))
    if direction=='droite' :
        perso = pygame.image.load("Images\sprite{}.png".format(compteur_sprite)).convert()
    if direction=='gauche' :
        perso = pygame.image.load("Images\sprite{}.png".format(compteur_sprite+3)).convert()
    if direction=='haut' :
        perso = pygame.image.load("Images\sprite{}.png".format(compteur_sprite+6)).convert()
    if direction=='bas' :
        perso = pygame.image.load("Images\sprite{}.png".format(compteur_sprite+9)).convert()
    if direction=='fixe' :
        perso = pygame.image.load("Images\sprite0.png").convert()
    perso.set_colorkey((255,255,255))
    fenetre.blit(perso, (300,300))




def partie_terminee_piege(grille, position) :
    i,j=position
    return grille[i][j]==3



