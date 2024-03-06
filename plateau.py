# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
Plateau de jeu Blokus
"""

from tkinter import *
import pyglet
import pyglet.media as media
import time

from ihm import *



def clic(event):
	global c,rectangle,nom_rectangle,tag_rectangle,nom_rectangle_split,joueur,nom_rectangle_complet,derniere_piece_bleu_jouee,derniere_piece_rouge_jouee

	print("TA MERE")
	#joueur = nb_tours%nb_joueurs+1
	joueur = 1

	if joueur == 1 :
	
		for rect_name, rect in pieces_bleu_loader.items():
			coords = cnv2.coords(rect)
			if event.x >= coords[0] and event.x <= coords[2] and event.y >= coords[1] and event.y <= coords[3]:
				rectangle = rect
				nom_rectangle_split = rect_name.split("-")
				nom_rectangle = nom_rectangle_split[0]
				nom_rectangle_complet = rect_name
				tag_rectangle = "rect"+nom_rectangle+"-"+nom_rectangle_split[4]

				derniere_piece_bleu_jouee = nom_rectangle

				c = (c+1)%2 #TEST SI CLIC OU DECLIC
				if (c == 1):
					cnv2.bind("<Motion>",glisser)
					old[0]=event.x
					old[1]=event.y
				else:
					cnv2.unbind("<Motion>")
					deposer(event.x,event.y)
					if flag_pose == 1:
						break
	
	
	elif joueur == 2:
	
		for rect_name, rect in pieces_rouge_loader.items():
			coords = cnv2.coords(rect)
			if event.x >= coords[0] and event.x <= coords[2] and event.y >= coords[1] and event.y <= coords[3]:
				rectangle = rect
				nom_rectangle_split = rect_name.split("-")
				nom_rectangle = nom_rectangle_split[0]
				nom_rectangle_complet = rect_name
				tag_rectangle = "rect"+nom_rectangle+"-"+nom_rectangle_split[4]

				derniere_piece_rouge_jouee = nom_rectangle

				c = (c+1)%2 #TEST SI CLIC OU DECLIC
				if (c == 1):
					cnv2.bind("<Motion>",glisser)
					cnv2.bind("<Motion>",glisser)
					old[0]=event.x
					old[1]=event.y
				else:
					cnv2.unbind("<Motion>")
					cnv2.unbind("<Motion>")
					deposer(event.x,event.y)
					if flag_pose == 1:
						break
					
	
def glisser(event):
	global rectangle
	x1, y1, x2, y2 = cnv2.coords(rectangle)
	if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
		cnv2.move(tag_rectangle, event.x-old[0], event.y-old[1])
		old[0]=event.x
		old[1]=event.y
		
		
def verif_alentours(x,y):
	global joueur
	liste_indicatif = [0]

	liste_indicatif.append(joueur)
	print("---",x,y)
	

	

	try:		
	
	
		#COIN SUPERIEUR GAUCHE
		if (x == 0 and y == 0) and (plateau[y][x] == 0) and (plateau[y-1][x] != joueur and plateau[y][x+1] != joueur):
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

def afficher_plateau_console():
	for k in plateau:
		print(k)	
		
def deposer(x,y):
	global taille_plateau,nb_tours,rectangle,nom_rectangle,flag_pose,nom_rectangle_split,mute_son,tag_rectangle,joueur,nom_rectangle_complet
		
	x1, y1, x2, y2 = cnv2.coords(rectangle)
	
	move = False
	for i in range(taille_plateau):
		for j in range(taille_plateau):
			if (5+i*unity+decalage_x <= x<= 5+(i+1)*unity+decalage_x and 5+j*unity <= y <= 5+(j+1)*unity):
				print("----EMPLACEMENT CASE----",i,j)


				flag_verif_boucle = True
				tagged_rectangles = []
				for item in cnv2.find_withtag(tag_rectangle):
					coordinates = cnv2.coords(item)
					tagged_rectangles.append(coordinates)
				
				i=(tagged_rectangles[int(nom_rectangle_split[3])][0])//unity-decalage_x//unity
				j=tagged_rectangles[int(nom_rectangle_split[3])][1]//unity

				total_code = 0
				for tag in tagged_rectangles:
					total_code += verif_alentours(int((tag[0]//unity)-decalage_x//unity),int(tag[1]//unity))
					
				if total_code <= 0:
					flag_verif_boucle = False
						

				if flag_verif_boucle:
					
					cnv2.move(tag_rectangle,5+i*unity-x1+decalage_x,5+j*unity-y1)
					for tag in tagged_rectangles:
						plateau[int(tag[1]//unity)][int((tag[0]//unity)-decalage_x//unity)] = joueur
					nb_tours += 1
					move = True

					flag_estSuppr = False
					compteur_estSuppr = 0

					if mute_son == 0 :
						joueur = pyglet.media.load(son_placement_piece)
						joueur.play()
					
					
					for i in range(5):
						try:
							if joueur == 1:					
								
								for rect_name, rect in pieces_bleu_loader.items():
									bleu_nom_rectangle_split = rect_name.split("-")
									if bleu_nom_rectangle_split[0] == nom_rectangle:
										pieces_bleu_loader.pop(rect_name)

							elif joueur == 2:
								
								for rect_name, rect in pieces_rouge_loader.items():
									rouge_nom_rectangle_split = rect_name.split("-")
									if rouge_nom_rectangle_split[0] == nom_rectangle:
										pieces_rouge_loader.pop(rect_name)
								
							compteur_estSuppr+=1
						except:
							pass
							
					flag_pose = 1

	
	afficher_plateau_console()		
	if (move == False):

		if joueur == 1:
			index_rect = pieces_bleu_noms.index(nom_rectangle_split[0]+"-0-"+nom_rectangle_split[2]+"-"+nom_rectangle_split[2]+"-"+nom_rectangle_split[4])
			coord_base = pieces_bleu_coords_base[index_rect]
		elif joueur == 2:
			index_rect = pieces_rouge_noms.index(nom_rectangle_split[0]+"-0-"+nom_rectangle_split[2]+"-"+nom_rectangle_split[2]+"-"+nom_rectangle_split[4])
			coord_base = pieces_rouge_coords_base[index_rect]

		cnv2.move(tag_rectangle,coord_base[0]-x1+unity*int(nom_rectangle_split[1]),coord_base[1]-y1)

def score():
	score_rouge = 0
	score_bleu = 0
	# score_vert = 0
	# score_jaune = 0

	loader = [pieces_rouge_loader,pieces_bleu_loader]
	derniere_piece = [derniere_piece_rouge_jouee,derniere_piece_bleu_jouee]

	for i in range(len(loader)):
		if len(loader[i]) == 0:
			if derniere_piece[i] == "0":
				score_rouge += 20
			else:
				score_rouge += 15
		else:
									
			for rect_name, rect in loader[i].items():
				score -= 1
										
			for rect_name, rect in loader[i].items():
				score -= 1

	return score_rouge,score_bleu






cnv2.bind("<Button-1>",clic)




			













	
	

