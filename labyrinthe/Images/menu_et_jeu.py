import pygame
from pygame.locals import *
from labyrinthe_grille import *
from Constantes import *
from Images.constantes_propres import *
pygame.init()


def afficher_jeu(vue):
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
    pygame.draw.rect(fenetre,[255,0,0],(6*largeur,6*largeur,largeur,largeur))


#vue=[[0 for i in range(13)] for j in range(13)]
#vue[0][0]=1
#vue[12][12]=-1
#vue[0][12]=2
#afficher_jeu(vue)

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

fenetre = pygame.display.set_mode((650, 650))



continuer = 1

while continuer:
    accueil = pygame.image.load(fond_ecran_accueil).convert()
    fenetre.blit(accueil,(0,0))
    pygame.display.flip()
    continuer_jeu = True
    continuer_accueil = 1

    while continuer_accueil :
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_jeu = False
                continuer_accueil = 0
                continuer = 0
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    continuer_accueil = 0
        font=pygame.font.Font(None, 24)
        text = font.render("PRESS ENTER",1,(255,255,255))
        fenetre.blit(accueil,(0,0))
        pygame.display.flip()

    portee_affichage=6
    portee_eclairage=3
    grille_eclairage=[[0 for i in range(16)] for j in range(16)]
    position=(7,7)
    grille_eclairage=actualisation_grille_eclairage(grille_eclairage,position,portee_eclairage)
    vue0=creer_vue(grille,grille_eclairage,position,portee_affichage)
    pygame.key.set_repeat(70,70)
    afficher_jeu(vue0)

    while continuer_jeu:
        pygame.time.Clock().tick(30)
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
                 vue, grille_eclairage, position= infos_apres_deplacement(grille,grille_eclairage,position,direction,portee_eclairage,portee_affichage)
                 afficher_jeu(vue)
             if event.type == QUIT:
                 continuer_jeu = False
                 continuer_accueil = 0
                 continuer = 0
             if partie_terminee(grille,position):
                 continuer_jeu=False #On retourne au menu
        pygame.display.flip()
