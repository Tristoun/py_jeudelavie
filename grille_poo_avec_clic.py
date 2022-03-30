# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:36:54 2021

@author: charamond
"""

import pygame 		# import de la bibliothèque pygame
from jeudelavie import *
from random import randint


fenetre = pygame.display.set_mode((500,500)) # instance fenêtre graphique
pygame.init()
pygame.mixer.init() #initialise le module mixer de pygame
"""pygame.mixer.music.load('musicsub.mp3') # charge la musique souhaiter"""
pygame.mouse.set_cursor(pygame.cursors.broken_x) #change l'icone du curseur

def dessin_grille(g,cote):
    """ dessine les ligne de la grille """
    xfin = pygame.display.get_window_size()[0]
    yfin = pygame.display.get_window_size()[1]
    for pos in range(len(g.matrix)):
        pygame.draw.line(fenetre,(150,100,100),(pos*cote,0),(pos*cote,xfin),2) # définition d'une ligne
        pygame.draw.line(fenetre,(150,100,100),(0,pos*cote),(xfin,pos*cote),2) # définition d'une ligne

def des_carre(x,y,coul,cote):
    """dessine la couleur du carré de coordonnée x,y"""
    pygame.draw.rect(fenetre, coul,(x*cote,y*cote,cote,cote))
    

def dessin_cellules(g,cote):
    """ dessine les carrés de la grille soit allumé soit eteint"""
    for celX in range(len(g.matrix)):           # chaque verticale
        for celY in range(len(g.matrix[0])) :   # chaque cellule de la verticale
            if g.matrix[celX][celY].actuel == False:
                des_carre(celX,celY,(255,255,255),cote)
            else :
                c1 = randint (0, 255)
                c2 = randint (0, 255)
                c3 = randint (0, 255)
                des_carre(celX,celY,(c1,c2,c3),cote)

def main1():     # fonction principale
    pourcentage = int(input("Combien souhaitez vous en pourcentage de cellules vivantes ? : "))  
    
    g = Grille(50,50)                           # largeur, hauteur
    g.affecte_voisins()
    g.remplir_alea(pourcentage)

    fenetre.fill((250,250,150))                 # couleur
    run = True                                  # boucke du script pour l'arret
    cote = int(pygame.display.get_window_size()[0]/50) # nbre de pixel d'un coté
    """ pygame.mixer.music.play(loops = -1)"""
    while run:                                  # boucle sans fin!!
        for event in pygame.event.get():        # parcours les évéments pygame
            if event.type == pygame.QUIT:       # croix en haut à droite de la fenetre (True or False)
                run = False                     # fin du while
            if event.type == pygame.MOUSEBUTTONDOWN:        # evenement appui
                
                if pygame.mouse.get_pressed() == (1,0,0):   # détection button gauche
                    i = pygame.mouse.get_pos()[0] // cote   # coordonnée x de la souris
                    j = pygame.mouse.get_pos()[1] // cote   # sur y # 
                    
                    
            if event.type == pygame.MOUSEBUTTONUP:  # evement lacher bouton
                pass                                # ne fain rien 
     
            
        fenetre.fill((250,250,150))         # efface la fenetre avec la couleur
        g.jeu()
        dessin_cellules(g,cote)             # dessinne les cellules
        dessin_grille(g,cote)               # dessine la grille
        pygame.display.flip()               # affiche des présentations graphiques (nécessaire)
        time.sleep(0.1)
            
    pygame.quit()                           # méthode de fermeture de l'instance fenêtre



if __name__ == "__main__" :    
    main1()