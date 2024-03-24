# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
Plateau de jeu Blokus
"""

from tkinter import *
import customtkinter
import pyglet
import pyglet.media as media
import time
from PIL import Image, ImageTk
from tkextrafont import Font
import pygame
pygame.init()
from random import *


global dev_mode,mute_son
dev_mode = 0
mute_son = 1


#SONS :
son_placement_piece = "sons/lego_build.wav"
son_reset = "sons/lego_reset.wav"


#MENU MODE LANCEMENT :
global nb_joueurs

nb_joueurs = 1




# pgm principal

old=[None, None]



global c, plateau, rect, num_rect, coords_rect, flag_pose
c = 0

rect = None
num_rect = -1
coords_rect = None
flag_pose = 0

unity = 40
taille_plateau = 20

width_cnv=1280
height_cnv=960
#width_cnv2 = taille_plateau*unity+taille_plateau/2+unity*6
width_cnv2 = width_cnv
height_cnv2 = taille_plateau*unity+taille_plateau/2+100


decalage_x = width_cnv2/2-(taille_plateau*unity)/2
decalage_y = 0

nb_tours = 0


global joueur, nb_joueurs_out, liste_joueurs_out
joueur = 1
nb_joueurs_out = 0
liste_joueurs_out = []

liste_couleurs_en = ["blue","red","green","yellow"]
liste_couleurs_fr = ["bleu","rouge","vert","jaune"]


plateau = []





for i in range(taille_plateau):
    plateau_temp = []
    for j in range(taille_plateau):
        plateau_temp.append(0)

    plateau.append(plateau_temp)







def verif_alentours(x,y,joueur,plateau,nb_tours):
    liste_indicatif = [0]
    


    liste_indicatif.append(joueur)
    # print("---",x,y)



    try:		
        
        if (x>=0 and x<=taille_plateau) and (y>=0 and y<=taille_plateau):
            #COIN SUPERIEUR GAUCHE
            if (x == 0 and y == 0) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x-1] != joueur):
                if (plateau[y+1][x+1] == joueur) or (nb_tours<=joueur-1):
                    return 1
                else:
                    return 0            
            
            #COIN INFERIEUR GAUCHE
            elif (x == 0 and y == len(plateau)-1) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x+1] != joueur):
                if (plateau[y-1][x+1] == joueur) or (nb_tours<=joueur-1):
                    return 1
                else:
                    return 0            
            
            #COIN SUPERIEUR DROIT
            elif (x == len(plateau)-1 and y == 0) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x-1] != joueur):
                if (plateau[y+1][x-1] == joueur) or (nb_tours<=joueur-1):
                    return 1
                else:
                    return 0            
            
            #COIN INFERIEUR DROIT
            elif (x == len(plateau)-1 and y == len(plateau)-1) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x-1] != joueur):
                if (plateau[y-1][x-1] == joueur) or (nb_tours<=joueur-1):
                    return 1
                else:
                    return 0            
            
            
            #COLONNE GAUCHE
            elif (y != 0 and y != len(plateau)-1) and (x == 0) and ((plateau[y][x+1] != joueur) and (plateau[y-1][x] != joueur) and (plateau[y+1][x] != joueur)) and (plateau[y][x] == 0):
                if (plateau[y+1][x+1] == joueur or plateau[y-1][x+1] == joueur):
                    return 1
                else:
                    return 0
            
            #COLONNE DROITE
            elif (y != 0 and y != len(plateau)-1) and (x == len(plateau)-1) and ((plateau[y][x-1] != joueur) and (plateau[y-1][x] != joueur) and (plateau[y+1][x] != joueur)) and (plateau[y][x] == 0):
                if (plateau[y+1][x-1] == joueur or plateau[y-1][x-1] == joueur):
                    return 1
                else:
                    return 0
            
            #LIGNE HAUT 
            elif (x != 0 and x != len(plateau)-1) and (y == 0) and ((plateau[y+1][x] != joueur) and (plateau[y][x+1] != joueur) and (plateau[y][x-1] != joueur)) and (plateau[y][x] == 0):	
                if (plateau[y+1][x+1] == joueur or plateau[y+1][x-1] == joueur):
                    return 1
                else:
                    return 0
            
            
            #LIGNE BAS
            elif (x != 0 and x != len(plateau)-1) and (y == len(plateau)-1) and ((plateau[y-1][x] != joueur) and (plateau[y][x-1] != joueur) and (plateau[y][x+1] != joueur)) and (plateau[y][x] == 0):
                if (plateau[y-1][x+1] == joueur or plateau[y-1][x-1] == joueur):
                    return 1
                else:
                    return 0

            #TOUT LE RESTE
            elif (x != 0 and x != len(plateau)-1 and y != 0 and y != len(plateau)-1) and ((plateau[y-1][x] != joueur) and (plateau[y+1][x] != joueur) and (plateau[y][x-1] != joueur) and (plateau[y][x+1] != joueur)) and (plateau[y][x] == 0):
                if (plateau[y+1][x-1] == joueur or plateau[y+1][x+1] == joueur or plateau[y-1][x-1] == joueur or plateau[y-1][x+1] == joueur):
                    return 1
                else:
                    return 0
                
            else:	
                return -1
        else:
            return -1
        
        
    except:
        return -1
    










