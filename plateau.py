# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
Plateau de jeu Blokus
"""

from tkinter import Tk, Canvas


def clic(event):
	global c,rectangle,nom_rectangle
	
	for rect_name, rect in pieces_rouge_loader.items():
		coords = cnv.coords(rect)
		if event.x >= coords[0] and event.x <= coords[2] and event.y >= coords[1] and event.y <= coords[3]:
			rectangle = rect
			nom_rectangle = rect_name
	
	
	c = (c+1)%2 #TEST SI CLIC OU DECLIC
	if (c == 1):
		cnv.bind("<Motion>",glisser)
		old[0]=event.x
		old[1]=event.y
	else:
		cnv.unbind("<Motion>")
		deposer(event.x,event.y)
	
def glisser(event):
	global rectangle
	x1, y1, x2, y2 = cnv.coords(rectangle)
	if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
		cnv.move(rectangle, event.x-old[0], event.y-old[1])
		old[0]=event.x
		old[1]=event.y
		
def verif_alentours(x,y):
	global nb_joueurs, nb_tours
	
	print(x == 0 and y == len(plateau)-1)
	
	#COIN SUPERIEUR GAUCHE
	if (x == 0 and y == 0):
		return True
	
	#COIN INFERIEUR GAUCHE
	elif (x == 0 and y == len(plateau)-1):
		return True
	
	#COIN SUPERIEUR DROIT
	elif (x == len(plateau)-1 and y == 0):
		return True
	
	#COIN INFERIEUR DROIT
	elif (x == len(plateau)-1 and y == len(plateau)-1):
		return True
	
	
	#COLONNE GAUCHE
	elif (x == 0) and (plateau[y][x+1] == 0 and plateau[y-1][x] == 0 and plateau[y+1][x] == 0) and (nb_joueurs-nb_tours != 0):
		return True		
	
	#COLONNE DROITE
	elif (x == len(plateau)-1) and (plateau[y][x-1] == 0 and plateau[y-1][x] == 0 and plateau[y+1][x] == 0) and (nb_joueurs-nb_tours != 0):
		return True
	
	#LIGNE HAUT
	elif (y == 0) and (plateau[y][x+1] == 0 and plateau[y][x-1] == 0 and plateau[y+1][x] == 0) and (nb_joueurs-nb_tours != 0):
		return True
	
	#LIGNE BAS
	elif (y == len(plateau)-1) and (plateau[y-1][x] == 0 and plateau[y][x-1] == 0 and plateau[y][x+1] == 0) and (nb_joueurs-nb_tours != 0):
		return True
	
	#TOUT LE RESTE
	elif (x != 0 and x != len(plateau)-1 and y != 0 and y != len(plateau)-1) and (plateau[y-1][x] == 0 and plateau[y+1][x] == 0 and plateau[y][x-1] == 0 and plateau[y][x+1] == 0) and (nb_joueurs-nb_tours != 0):
		return True
		
	else:
		return False
	
def afficher_plateau_console():
	for k in plateau:
		print(k)	
		
def deposer(x,y):
	global taille_plateau,nb_tours,rectangle,nom_rectangle
		
	x1, y1, x2, y2 = cnv.coords(rectangle)
	
	move = False
	for i in range(taille_plateau):
		for j in range(taille_plateau):
			if (5+i*unity <= x<= 5+(i+1)*unity and 5+j*unity <= y <= 5+(j+1)*unity):
				print("----EMPLACEMENT CASE----",i,j)
				if verif_alentours(i,j) == True:
					cnv.move(rectangle,5+i*unity-x1,5+j*unity-y1)
					plateau[j][i] = 1
					nb_tours += 1
					afficher_plateau_console()
					
					
					move = True
	if (move == False):
	
		coord_base = pieces_rouge_coords_base[int(nom_rectangle)]
		cnv.move(rectangle,coord_base[0]-x1,coord_base[1]-y1)



# pgm principal

old=[None, None]

global c
c = 0

rect = None
num_rect = -1
coords_rect = None
root = Tk()
cnv = Canvas(root, width=1280, height=960)
unity = 70
taille_plateau = 12
nb_joueurs = 1
nb_tours = 1
cnv.pack()


plateau = []
pieces_bleu = []

pieces_rouge = []
pieces_rouge_loader = {
	"0": (cnv.create_rectangle((taille_plateau+1.05)*unity, 30, (taille_plateau+1.05)*unity+unity, 30+unity, fill='red', outline='')),
	"1": (cnv.create_rectangle((taille_plateau+1.05)*unity, (2*30)+(1*unity), (taille_plateau+1.05)*unity+unity, (2*30)+(1*unity)+unity, fill='red', outline='')),
	"2": (cnv.create_rectangle((taille_plateau+1.05)*unity, (3*30)+(2*unity), (taille_plateau+1.05)*unity+unity, (3*30)+(2*unity)+unity, fill='red', outline='')),
	"3": (cnv.create_rectangle((taille_plateau+1.05)*unity, (4*30)+(3*unity), (taille_plateau+1.05)*unity+unity, (4*30)+(3*unity)+unity, fill='red', outline='')),
	"4": (cnv.create_rectangle((taille_plateau+1.05)*unity, (5*30)+(4*unity), (taille_plateau+1.05)*unity+unity, (5*30)+(4*unity)+unity, fill='red', outline=''))
	}

pieces_rouge_coords_base = []
for rect_name, rect in pieces_rouge_loader.items():
	pieces_rouge_coords_base.append(cnv.coords(rect))
	
	
for i in range(taille_plateau):
	plateau_temp = []
	for j in range(taille_plateau):
		plateau_temp.append(0)
	
	plateau.append(plateau_temp)

		


#cnv.create_rectangle((taille_plateau+1.05)*unity, 30, (taille_plateau+1.05)*unity+unity, 30+unity, fill='red', outline='')

for i in range(taille_plateau+1):
	cnv.create_line(5,5+unity*i,(taille_plateau+0.05)*unity,5+unity*i)
	cnv.create_line(5+unity*i,5,5+unity*i,(taille_plateau+0.05)*unity)


cnv.bind("<Button-1>",clic)

root.mainloop()
