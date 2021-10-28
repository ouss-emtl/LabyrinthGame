from pièges import *
import pygame
from pygame.locals import *
from labyrinthe_grille import *
from fichiers import *
from generateur_aleatoire import *
from generation_labyrinthe import *
from Constantes import *
fond_ecran_accueil = 'Images/fond_écran_accueil.jpg'
fond_game_over = 'Images/game_over_fond.jpg'
fond_victoire='Images/You_won.png'
pygame.init()

import time

def quitter():
    continuer_editeur=0
    continuer_jeu=0
    continuer_menu=0
    continuer_accueil=0
    continuer_aleatoire=0
    continuer_choix_save=0
    continuer_difficulte=0
    continuer_histoire=0
    continuer_taille=0
    continuer_gameover=0
    continuer=0

icone=pygame.image.load(image_icon)
pygame.display.set_icon(icone)

fichier_son_deplacement = 'son_jeu/1113.wav'
son_deplacement=pygame.mixer.Sound(fichier_son_deplacement)

fichier_son_accueil = 'son_jeu/musique-qui-fait-peur.wav'
son_accueil=pygame.mixer.Sound(fichier_son_accueil)

fichier_son_jeux = 'son_jeu/musique-stressante-n03.wav'
son_jeux = pygame.mixer.Sound(fichier_son_jeux)






length = 120 #timer de 2 minutes





taille_fenetre = 650


fenetre = pygame.display.set_mode((taille_fenetre, taille_fenetre))
pygame.display.set_caption("The maze")
joue = 0

on_est_pas_dans_le_menu_aleatoire = True
coordonnee_piege_vu = []
continuer = 1
compteur_sprite=0
compteur_explosion = 0
grille_piege=[[0 for i in range(30)] for j in range(30)]
while continuer:
    pygame.display.set_caption("The maze")
    son_accueil.play()
    accueil = pygame.image.load(fond_ecran_accueil).convert()
    fenetre.blit(accueil,(0,0))
    pygame.display.flip()
    continuer_jeu = True
    continuer_accueil = 1
    continuer_histoire = 0
    continuer_aleatoire = 0
    continuer_editeur = 0
    continuer_gameover = 0
    while continuer_accueil :
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                quitter()
                continuer_jeu = 0
                continuer_accueil = 0
                continuer = 0
            elif event.type == KEYDOWN and event.key == K_SPACE:
                    continuer_accueil = 0
                    continuer_menu=1
        fenetre.blit(accueil,(0,0))
        pygame.display.flip()
    while continuer_menu:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    quitter()
                    continuer_menu = 0
                    continuer = 0
                    continuer_jeu=0
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 300 and event.pos[1] > 200:
                    continuer_histoire=1
                    continuer_menu=0
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 450 and event.pos[1] > 350:
                    continuer_aleatoire=1
                    continuer_menu=0
                    on_est_pas_dans_le_menu_aleatoire = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 600 and event.pos[1] > 500:
                continuer_editeur=1
                continuer_menu=0
        font_title=pygame.font.Font(None, 100)
        font_content = pygame.font.Font(None, 50)
        pygame.draw.rect(fenetre,[0,0,0],(0,0,650,650))
        pygame.draw.rect(fenetre,[200,200,200],(50,200,550,100))
        pygame.draw.rect(fenetre,[135,135,135],(50,350,550,100))
        pygame.draw.rect(fenetre,[100,100,100],(50,500,550,100))
        text = font_title.render("MENU",1,(255,255,255))
        fenetre.blit(text,(230,50))
        text = font_content.render("Choix du Niveau",1,(255,255,255))
        fenetre.blit(text,(200,220))
        text = font_content.render("Niveau aléatoire",1,(255,255,255))
        fenetre.blit(text,(200,370))
        text = font_content.render("Editeur de niveau",1,(255,255,255))
        fenetre.blit(text,(200,520))
        pygame.display.flip()
    while continuer_histoire:
        font_title=pygame.font.Font(None, 100)
        font_content = pygame.font.Font(None, 50)
        pygame.draw.rect(fenetre,[0,0,0],(0,0,650,650))
        pygame.draw.rect(fenetre,[255,255,255],(50,50,550,100))
        pygame.draw.rect(fenetre,[255,255,255],(50,200,550,100))
        pygame.draw.rect(fenetre,[255,255,255],(50,350,550,100))
        pygame.draw.rect(fenetre,[255,255,255],(50,500,550,100))
        text = font_content.render("Niveau 1",1,(0,0,0))
        fenetre.blit(text,(200,70))
        text = font_content.render("Niveau 2",1,(0,0,0))
        fenetre.blit(text,(200,220))
        text = font_content.render("Niveau 3",1,(0,0,0))
        fenetre.blit(text,(200,370))
        text = font_content.render("Niveau 4",1,(0,0,0))
        fenetre.blit(text,(200,520))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                quitter()
                continuer_histoire=0
                continuer=0
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 150 and event.pos[1] > 50:
                continuer_histoire=0
                continuer_jeu=1
                grille_piege = niveau_matrice('1.txt')
                grille= grille_sans_piege(grille_piege)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 300 and event.pos[1] > 200:
                continuer_histoire=0
                continuer_jeu=1
                grille_piege = niveau_matrice('2.txt')
                grille= grille_sans_piege(grille_piege)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 450 and event.pos[1] > 350:
                continuer_histoire=0
                continuer_jeu=1
                grille_piege = niveau_matrice('3.txt')
                grille= grille_sans_piege(grille_piege)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 600 and event.pos[1] > 500:
                continuer_histoire=0
                continuer_jeu=1
                grille_piege = niveau_matrice('4.txt')
                grille= grille_sans_piege(grille_piege)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil=1
                continuer_histoire=0
                continuer_jeu=0
        position=position_initiale(grille_piege)
    while continuer_aleatoire:
        continuer_taille=1
        while continuer_taille:
            pygame.draw.rect(fenetre,[0,0,0],(0,0,650,650))
            pygame.draw.rect(fenetre,[255,255,255],(50,200,550,100))
            pygame.draw.rect(fenetre,[255,255,255],(50,350,550,100))
            pygame.draw.rect(fenetre,[255,255,255],(50,500,550,100))
            text = font_title.render("Choisir taille",1,(255,255,255))
            fenetre.blit(text,(120,50))
            text = font_content.render("Petit",1,(0,0,0))
            fenetre.blit(text,(200,220))
            text = font_content.render("Moyen",1,(0,0,0))
            fenetre.blit(text,(200,370))
            text = font_content.render("Grand",1,(0,0,0))
            fenetre.blit(text,(200,520))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    quitter()
                    continuer_taille=0
                    continuer_aleatoire=0
                    continuer=0
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 300 and event.pos[1] > 200:
                    continuer_taille=0
                    continuer_difficulte=1
                    size_lab=20
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 450 and event.pos[1] > 350:
                    continuer_taille=0
                    continuer_difficulte=1
                    size_lab=30
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 600 and event.pos[1] > 500:
                    continuer_taille=0
                    continuer_difficulte=1
                    size_lab=40
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer_accueil=1
                    continuer_difficulte=0
                    continuer_aleatoire=0
                    continuer_taille=0
                    continuer_jeu=0
        while continuer_difficulte:
            pygame.draw.rect(fenetre,[0,0,0],(0,0,650,650))
            pygame.draw.rect(fenetre,[255,255,255],(50,200,550,100))
            pygame.draw.rect(fenetre,[255,255,255],(50,350,550,100))
            pygame.draw.rect(fenetre,[255,255,255],(50,500,550,100))
            text = font_title.render("Choisir difficulté",1,(255,255,255))
            fenetre.blit(text,(50,50))
            text = font_content.render("Facile",1,(0,0,0))
            fenetre.blit(text,(200,220))
            text = font_content.render("Moyen",1,(0,0,0))
            fenetre.blit(text,(200,370))
            text = font_content.render("Difficile",1,(0,0,0))
            fenetre.blit(text,(200,520))
            pygame.display.flip()
            proportion=0
            for event in pygame.event.get():
                if event.type == QUIT:
                    quitter()
                    continuer_difficulte=0
                    continuer_aleatoire=0
                    continuer=0
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 300 and event.pos[1] > 200:
                    continuer_taille=0
                    continuer_difficulte=0
                    continuer_aleatoire=0
                    continuer_jeu=1
                    proportion=0.2
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 450 and event.pos[1] > 350:
                    continuer_taille=0
                    continuer_difficulte=0
                    continuer_aleatoire=0
                    continuer_jeu=1
                    proportion=0.3
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 600 and event.pos[1] > 500:
                    continuer_taille=0
                    continuer_difficulte=0
                    continuer_aleatoire=0
                    continuer_jeu=1
                    proportion=0.4
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer_accueil=1
                    continuer_difficulte=0
                    continuer_aleatoire=0
                    continuer_taille=0
                    continuer_jeu=0
            grille=grille_totale(size_lab,proportion)
            position=(len(grille)//2,len(grille)//2)
    while continuer_editeur:
        save=1
        font_title=pygame.font.Font(None, 100)
        font_content = pygame.font.Font(None, 50)
        pygame.draw.rect(fenetre,[0,0,0],(0,0,650,650))
        pygame.draw.rect(fenetre,[255,255,255],(50,50,550,100))
        pygame.draw.rect(fenetre,[255,255,255],(50,200,550,100))
        pygame.draw.rect(fenetre,[255,255,255],(50,350,550,100))
        pygame.draw.rect(fenetre,[255,255,255],(50,500,550,100))
        text = font_content.render("Sauvegarde 1",1,(0,0,0))
        fenetre.blit(text,(200,70))
        text = font_content.render("Sauvegarde 2",1,(0,0,0))
        fenetre.blit(text,(200,220))
        text = font_content.render("Sauvegarde 3",1,(0,0,0))
        fenetre.blit(text,(200,370))
        text = font_content.render("Sauvegarde 4",1,(0,0,0))
        fenetre.blit(text,(200,520))
        pygame.display.flip()
        continuer_choix_save=True
        while continuer_choix_save:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quitter()
                    continuer_histoire=0
                    continuer_choix_save=False
                    continuer=0
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 150 and event.pos[1] > 50:
                    continuer_histoire=0
                    continuer_jeu=0
                    continuer_choix_save=False
                    save='1.txt'
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 300 and event.pos[1] > 200:
                    continuer_histoire=0
                    continuer_jeu=0
                    continuer_choix_save=False
                    save='2.txt'
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 450 and event.pos[1] > 350:
                    continuer_histoire=0
                    continuer_jeu=0
                    save='3.txt'
                    continuer_choix_save=False

                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 600 and event.pos[1] > 500:
                    continuer_histoire=0
                    continuer_jeu=0
                    continuer_choix_save=False
                    save='4.txt'

                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer_accueil=1
                    continuer_histoire=0
                    continuer_jeu=0
                    continuer_choix_save=False

        creer_niveau(30,save,(1,1))
        continuer_editeur=0
        continuer_menu=1
        continuer_jeu=0
    if continuer_jeu:
        portee_affichage=6
        portee_eclairage=2
        grille_eclairage=[[0 for i in range(len(grille))] for j in range(len(grille))]
        grille_eclairage=actualisation_grille_eclairage(grille_eclairage,position,portee_eclairage)
        vue0=creer_vue(grille,grille_eclairage,position,portee_affichage)
        afficher_jeu_piege_vue(vue0,fenetre,'bas',compteur_sprite)
    son_accueil.stop()
    pygame.key.set_repeat(70,70)
    start = time.time()
    while continuer_jeu:
        son_jeux.play()
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                 if event.key == K_LEFT :
                     compteur_sprite+=1
                     if joue ==0:
                         son_deplacement.play()
                         joue = 1
                     direction="gauche"
                 if event.key == K_RIGHT:
                     compteur_sprite+=1
                     if joue ==0:
                         son_deplacement.play()
                         joue = 1
                     direction="droite"
                 if event.key == K_UP:
                     compteur_sprite+=1
                     if joue ==0:
                        son_deplacement.play()
                        joue = 1
                        direction="haut"
                 if event.key == K_DOWN:
                     compteur_sprite+=1
                     if joue ==0:
                        son_deplacement.play()
                        joue = 1
                        direction="bas"
                 if event.key == K_SPACE and sur_une_tnt(grille, position):
                     x,y = position


                     direction="fixe"
                     compteur_explosion=0
                     while compteur_explosion<12 :
                         if compteur_explosion == 4 :
                             for i in range(-1,2):
                                 for j in range(-1,2):
                                     if grille[x+i][y+j] != -1:
                                         grille[x+i][y+j] = 1
                         compteur_explosion+=1
                         vue, grille_eclairage, position= infos_apres_deplacement(grille,grille_eclairage,position,direction,portee_eclairage,portee_affichage)
                         afficher_jeu_piege_vue(vue, fenetre,direction,compteur_sprite)
                         image_explosion=pygame.image.load("Images\explosion{}.png".format(compteur_explosion)).convert()
                         image_explosion.set_colorkey((255,255,255))
                         fenetre.blit(image_explosion,(250,250))
                         pygame.display.flip()
                         time.sleep(0.06)
                 if event.key == K_ESCAPE:
                     continuer_jeu=0
                     continuer=1
                     continuer_menu=1
                 vue, grille_eclairage, position= infos_apres_deplacement(grille,grille_eclairage,position,direction,portee_eclairage,portee_affichage)
                 compteur_sprite=compteur_sprite % 3
                 afficher_jeu_piege_vue(vue,fenetre,direction,compteur_sprite)
                 if  partie_terminee(grille,position):
                     continuer_vic=1
                     while continuer_vic:
                        gagne=pygame.image.load(fond_victoire)
                        fenetre.blit(gagne,(0,0))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type==QUIT or event.type==KEYDOWN and event.key==K_SPACE:
                                continuer_vic=0
                     continuer_jeu=0
                     continuer_menu=1
                     continuer_gameover=0
            if event.type == KEYUP:
                joue =0
                son_deplacement.stop()
            if event.type == QUIT:
                 quitter()
                 continuer_jeu = False
                 continuer_accueil = 0
                 continuer = 0
            if on_est_pas_dans_le_menu_aleatoire:
                if partie_terminee_piege(grille_piege, position):
                     if grille[position[0]][position[1]] !=3:

                         coordonnee_piege_vu.append(position)
                         grille[position[0]][position[1]]=3
                     continuer_jeu=False #On retourne au menu
                     continuer_gameover = 1
            if not on_est_pas_dans_le_menu_aleatoire:
                if partie_terminee(grille,position):
                    continuer_jeu = False

        if time.time() - start >= length:
            text = font_content.render( "GameOver",1,(255,255,255))
            continuer_jeu = False
            continuer_gameover = 1
        else:
            pygame.draw.rect(fenetre,[0,0,0],(10,10,100,100))
            text = font_content.render("%.1f " % (length - (time.time() - start)),1,(255,255,255))



        fenetre.blit(text,(10,10))


        pygame.display.flip()
    son_jeux.stop()

    gameover = pygame.image.load(fond_game_over).convert()

    while continuer_gameover:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_SPACE:
                continuer_gameover = 0
                quitter()
        fenetre.blit(gameover,(0,0))
        pygame.display.flip()


