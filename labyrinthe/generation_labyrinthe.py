
#Editeur
import random
import numpy as np
import pygame
from pygame.locals import *
from labyrinthe_grille import *
from Constantes import *
import fichiers
from Fonctions_generation import *


continuer_jeu=True

pygame.init()
fenetre = pygame.display.set_mode((taille_fenetre, taille_fenetre))
pygame.key.set_repeat(70,70) #Permet de rester appuyer sur une touche






def creer_niveau(taille,nom,position_initiale):
    text='couloir' #initialise le titre
    pygame.display.set_caption("Editeur Niveau : Mode {}".format(text))
    n=taille
    grille=[[0 for i in range(n)]for j in range(n)]
    def afficher_grille(vue):
        size=2*portee_affichage +1
        largeur=taille_fenetre/size
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
                    pygame.draw.rect(fenetre,[255,255,0],(i*largeur,j*largeur,largeur,largeur))
                if vue[j][i] == 4:
                    pygame.draw.rect(fenetre,[180,180,180],(i*largeur,j*largeur,largeur,largeur))
                if vue[j][i] == 5:
                    pygame.draw.rect(fenetre,[0,0,255],(i*largeur,j*largeur,largeur,largeur))
        pygame.draw.rect(fenetre,[255,0,0],(6*largeur,6*largeur,largeur,largeur))
    position=position_initiale
    vue0=update_vue(grille,position_initiale,portee_affichage)
    continuer_jeu=True
    pygame.init()
    fenetre = pygame.display.set_mode((taille_fenetre, taille_fenetre))
    afficher_grille(vue0)
    commande = 1
    while continuer_jeu:
        pygame.time.Clock().tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction="gauche"
                if event.key == K_RIGHT:
                    direction="droite"
                if event.key == K_UP:
                    direction="haut"
                if event.key == K_DOWN:
                    direction="bas"
                if event.key==K_RETURN:
                    commande=2
                    direction='fixe'
                if event.key == K_SPACE:
                    if commande!=2:
                        commande=1-commande
                    else:
                        commande=1
                    direction='fixe'
                if commande==2:
                    x,y=position
                    if event.key==K_2:
                        direction='fixe'
                        grille[x][y]=2
                    if event.key==K_3:
                        direction='fixe'
                        grille[x][y]=3
                    if event.key==K_4:
                        direction='fixe'
                        grille[x][y]=4
                    if event.key==K_5:
                        direction='fixe'
                        grille[x][y]=5
                if commande==1:
                    text='Couloir'
                if commande==0:
                    text='Mur'
                if commande==2:
                    text='Ajout fonctionnalités'
                pygame.display.set_caption("Editeur Niveau : Mode {}".format(text))
                vue, grille, position= maj(grille,direction,position,commande,portee_affichage)
                afficher_grille(vue)
            if event.type == QUIT or event.type==KEYDOWN and event.key==K_s:
                continuer_jeu = False
                font=pygame.font.Font(None, 24)
                afficher_grille(vue0)
                size=2*portee_affichage +1
                largeur=taille_fenetre/size
                pygame.draw.rect(fenetre,[0,0,0],(6*largeur,6*largeur,largeur,largeur))
                text = font.render("Voulez-vous enregister ? (y/n)",1,(255,255,255))
                fenetre.blit(text,(200,200))
                pygame.display.flip()
                continuer_enregistrer=True
                while continuer_enregistrer:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key==121:
                                fichiers.niveau_text(grille,nom)
                                continuer_enregistrer=False
                            if event.key==110:
                                continuer_enregistrer=False


if __name__ == "__main__":
    creer_niveau(30,'1',(10,10))









