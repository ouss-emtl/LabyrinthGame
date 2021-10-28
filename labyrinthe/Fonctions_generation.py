from Constantes import *
import pygame
import numpy as np

def deplacement_admin(grille,direction,position):
    n=len(grille)
    x,y=position
    if direction=='haut':
        if x>0:
            x-=1
    if direction=='bas':
        if x<n-1:
            x+=1
    if direction=='gauche':
        if y>0:
            y-=1
    if direction=='droite':
        if y<n-1:
            y+=1
    return(x,y)


def actualisation(grille,position,commande):
    x,y=position
    nouvelle_grille=grille
    if commande==1:
        nouvelle_grille[x][y]=1
    elif commande==0:
        nouvelle_grille[x][y]=0
    return (nouvelle_grille)

def update_vue(grille,position,portee_affichage):
    x,y=position
    vue=[[0 for i in range(2*portee_affichage+1)] for j in range(2*portee_affichage+1)]
    for i in range((portee_affichage*2+1)):
        for j in range(portee_affichage*2+1):
            if x+i-portee_affichage>=0 and x+i-portee_affichage<len(grille)and y+j-portee_affichage>=0 and y+j-portee_affichage<len(grille):
                vue[i][j]=grille[x+i-portee_affichage][y+j-portee_affichage]
            else :
                vue[i][j]=-1
    return (vue)

def maj(grille,direction,position,commande,portee_affichage):
    nouvelle_position = deplacement_admin(grille, direction, position)
    nouvelle_grille = actualisation(grille, nouvelle_position,commande)
    vue = update_vue(nouvelle_grille, nouvelle_position, portee_affichage)
    return vue, nouvelle_grille, nouvelle_position


