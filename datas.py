# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
Plateau de jeu Blokus
"""

from tkinter import *
import pyglet
import pyglet.media as media
import time
from PIL import Image, ImageTk
from tkinter.font import Font


global dev_mode,mute_son
dev_mode = 0
mute_son = 0


#SONS :
son_placement_piece = "sons/lego_build.wav"
son_reset = "sons/lego_reset.wav"

# pgm principal

old=[None, None]



global c, plateau, rect, num_rect, coords_rect, flag_pose
c = 0

rect = None
num_rect = -1
coords_rect = None
flag_pose = 0

unity = 50
taille_plateau = 12

width_cnv=1280
height_cnv=960
#width_cnv2 = taille_plateau*unity+taille_plateau/2+unity*6
width_cnv2 = width_cnv
height_cnv2 = taille_plateau*unity+taille_plateau/2+100


decalage_x = width_cnv2/2-(taille_plateau*unity)/2
decalage_y = 0

nb_joueurs = 2
nb_tours = 0

global joueur
joueur = 0





plateau = []
for i in range(taille_plateau):
    plateau_temp = []
    for j in range(taille_plateau):
        plateau_temp.append(0)

    plateau.append(plateau_temp)



if dev_mode == 0:
    mute_son = 0
else:
    mute_son = 1


def verif_alentours(x,y,joueur):
    global plateau
    liste_indicatif = [0]


    liste_indicatif.append(joueur)
    print("---",x,y)


    


    try:		
    
    
        #COIN SUPERIEUR GAUCHE
        if (x == 0 and y == 0) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x-1] != joueur):
            print("Salut, je v")
            return 1
        
        #COIN INFERIEUR GAUCHE
        elif (x == 0 and y == len(plateau)-1) and (plateau[y][x] == 0) and (plateau[y+1][x] != joueur and plateau[y][x+1] != joueur):
            return 1
        
        #COIN SUPERIEUR DROIT
        elif (x == len(plateau)-1 and y == 0) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x-1] != joueur):
            return 1
        
        #COIN INFERIEUR DROIT
        elif (x == len(plateau)-1 and y == len(plateau)-1) and (plateau[y][x] == 0) and (plateau[y+1][x] != joueur and plateau[y][x-1] != joueur):
            return 1
        
        
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
        elif (x != 0 and x != len(plateau)-1) and (y == 0) and (plateau[y][x+1] != joueur) and (plateau[y+1][x] != joueur) and (plateau[y][x] == 0):	
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
        
        
    except:
        return -1





