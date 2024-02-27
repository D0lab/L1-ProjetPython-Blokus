# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
Plateau de jeu Blokus
"""

from tkinter import *
import pyglet
import pyglet.media as media
import time

dev_mode = 1

def clic(event):
	global c,rectangle,nom_rectangle,tag_rectangle,nom_rectangle_split

	
	
	for rect_name, rect in pieces_rouge_loader.items():
		coords = cnv2.coords(rect)
		if event.x >= coords[0] and event.x <= coords[2] and event.y >= coords[1] and event.y <= coords[3]:
			rectangle = rect
			nom_rectangle_split = rect_name.split("-")
			nom_rectangle = nom_rectangle_split[0]
			tag_rectangle = "rect"+nom_rectangle

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
	global nb_joueurs, nb_tours
	liste_indicatif = [0,1,2]
	liste_indicatif.pop(1)
	print("---",x,y)

	try:
	
	
		#COIN SUPERIEUR GAUCHE
		if (x == 0 and y == 0):
			return 1
		
		#COIN INFERIEUR GAUCHE
		elif (x == 0 and y == len(plateau)-1):
			return 1
		
		#COIN SUPERIEUR DROIT
		elif (x == len(plateau)-1 and y == 0) and (plateau[y][x] == 0):
			return 1
		
		#COIN INFERIEUR DROIT
		elif (x == len(plateau)-1 and y == len(plateau)-1):
			return 1
		
		
		#COLONNE GAUCHE
		elif (y != 0 and y != len(plateau)-1) and (x == 0) and (plateau[y][x+1] == 0 and plateau[y-1][x] == 0 and plateau[y+1][x] == 0 and plateau[y][x] == 0):
			if (plateau[y+1][x+1] != 0 or plateau[y-1][x+1] != 0):
				return 1
			else:
				return 0
		
		#COLONNE DROITE
		elif (y != 0 and y != len(plateau)-1) and (x == len(plateau)-1) and (plateau[y][x-1] == 0 and plateau[y-1][x] == 0 and plateau[y+1][x] == 0 and plateau[y][x] == 0):
			if (plateau[y+1][x-1] != 0 or plateau[y-1][x-1] != 0):
				return 1
			else:
				return 0
		
		#LIGNE HAUT 
		
		elif (x != 0 and x != len(plateau)-1) and (y == 0) and (plateau[y][x+1] == 0 and plateau[y][x-1] == 0 and plateau[y+1][x] == 0 and plateau[y][x] == 0):	
			if (plateau[y+1][x+1] != 0 or plateau[y+1][x-1] != 0):
				return 1
			else:
				return 0
		
		
		#LIGNE BAS
		elif (x != 0 and x != len(plateau)-1) and (y == len(plateau)-1) and (plateau[y-1][x] == 0 and plateau[y][x-1] == 0 and plateau[y][x+1] == 0 and plateau[y][x] == 0):
			if (plateau[y-1][x+1] != 0 or plateau[y-1][x-1] != 0):
				return 1
			else:
				return 0

		#TOUT LE RESTE
		elif (x != 0 and x != len(plateau)-1 and y != 0 and y != len(plateau)-1) and (plateau[y-1][x] == 0 and plateau[y+1][x] == 0 and plateau[y][x-1] == 0 and plateau[y][x+1] == 0 and plateau[y][x] == 0):
			if (plateau[y+1][x-1] != 0 or plateau[y+1][x+1] != 0 or plateau[y-1][x-1] != 0 or plateau[y-1][x+1] != 0):
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
	global taille_plateau,nb_tours,rectangle,nom_rectangle,flag_pose,nom_rectangle_split,mute_son,tag_rectangle
		
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

				total_code = 0
				for tag in tagged_rectangles:
					total_code += verif_alentours(int((tag[0]//unity)-decalage_x//unity),int(tag[1]//unity))
				if total_code <= 0:
					flag_verif_boucle = False
						

				if flag_verif_boucle:
					# i = int(tag[0]//unity)
					# j = int(tag[1]//unity)
					cnv2.move(tag_rectangle,5+i*unity-x1+decalage_x,5+j*unity-y1)
					for tag in tagged_rectangles:
						plateau[int(tag[1]//unity)][int((tag[0]//unity)-decalage_x//unity)] = 1
					nb_tours += 1
					afficher_plateau_console()
					move = True

					flag_estSuppr = False
					compteur_estSuppr = 0

					if mute_son == 0 :
						player = pyglet.media.load(son_placement_piece)
						player.play()
					
					
					for i in range(5):
						try:					
							pieces_rouge_loader.pop(nom_rectangle+"-"+str(i))
							compteur_estSuppr+=1
						except:
							pass
							
					flag_pose = 1
					
	if (move == False):
	
		coord_base = pieces_rouge_coords_base[int(nom_rectangle)]
		print(coord_base)
		cnv2.move(tag_rectangle,coord_base[0]-x1+unity*int(nom_rectangle_split[1]),coord_base[1]-y1)
		print(coord_base[0]-x1+unity*int(nom_rectangle_split[1]),coord_base[1]-y1)



# pgm principal

old=[None, None]

global c
c = 0

rect = None
num_rect = -1
coords_rect = None
flag_pose = 0

unity = 60
taille_plateau = 12

width_cnv=1280
height_cnv=960
#width_cnv2 = taille_plateau*unity+taille_plateau/2+unity*6
width_cnv2 = width_cnv
height_cnv2 = taille_plateau*unity+taille_plateau/2


decalage_x = width_cnv2/2-(taille_plateau*unity)/2
decalage_y = 0

nb_joueurs = 1
nb_tours = 1
if dev_mode == 0:
	mute_son = 0
else:
	mute_son = 1




			

#SONS :
son_placement_piece = "sons/lego_build.wav"
son_reset = "sons/lego_reset.wav"





def build_pieces_rouge():
	global pieces_rouge_loader, nb_pieces_rouge, pieces_rouge_coords_base,decalage_x
	
	pieces_rouge_loader = {
		#"NUMERO-X-Y :" (cnv2.create_rectangle((x1, y1, x2, y2, fill='couleur', outline='', tags="rectNUM_RECT"))
		"0-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity, fill='red', outline='', tags="rect0")),
		"1-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (2*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (2*30)+(1*unity)+unity, fill='red', outline='', tags="rect1")),
			"1-1": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (2*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (2*30)+(1*unity)+unity, fill='red', outline='', tags="rect1")),
		"2-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2")),
			"2-1": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2")),
			"2-2": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2")),
		"3-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (4*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(3*unity)+unity, fill='red', outline='', tags="rect3")),
			"3-1": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (4*30)+(3*unity)+unity, fill='red', outline='', tags="rect3")),
			"3-2": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (4*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(4*unity)+unity, fill='red', outline='', tags="rect3")),
		"4-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4")),
			"4-1": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4")),
   			"4-2": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4")),
			"4-3": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4")),
		"5-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (8*30)+(5*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (8*30)+(5*unity)+unity, fill='red', outline='', tags="rect5")),
			"5-1": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (8*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (8*30)+(6*unity)+unity, fill='red', outline='', tags="rect5")),
   			"5-2": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (8*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (8*30)+(6*unity)+unity, fill='red', outline='', tags="rect5")),
			"5-3": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (8*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (8*30)+(6*unity)+unity, fill='red', outline='', tags="rect5")),
		"6-0": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (9*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(6*unity)+unity, fill='red', outline='', tags="rect6")),
			"6-1": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(6*unity)+unity, fill='red', outline='', tags="rect6")),
   			"6-2": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (9*30)+(6*unity)+unity, fill='red', outline='', tags="rect6")),
			"6-3": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(7*unity)+unity, fill='red', outline='', tags="rect6")),
		}	
	nb_pieces_rouge = len(pieces_rouge_loader)

	pieces_rouge_coords_base = []
	for rect_name, rect in pieces_rouge_loader.items():
		pieces_rouge_coords_base.append(cnv2.coords(rect))
	
def build_pieces_bleu():
	global pieces_bleu_loader, nb_pieces_bleu, pieces_bleu_coords_base,decalage_x
	
	pieces_bleu_loader = {
		#"NUMERO-X-Y :" (cnv2.create_rectangle((x1, y1, x2, y2, fill='couleur', outline='', tags="rectNUM_RECT"))
		"5-0": (cnv2.create_rectangle(0+unity, 30, unity, 30+unity, fill='blue', outline='', tags="rect500"))
		}
	nb_pieces_bleu = len(pieces_rouge_loader)

	pieces_bleu_coords_base = []
	for rect_name, rect in pieces_rouge_loader.items():
		pieces_rouge_coords_base.append(cnv2.coords(rect))
	

def build_plateau():
	global plateau
	
	plateau = []
	for i in range(taille_plateau):
		plateau_temp = []
		for j in range(taille_plateau):
			plateau_temp.append(0)
	
		plateau.append(plateau_temp)
		
	#cnv2.create_rectangle((taille_plateau+1.05)*unity, 30, (taille_plateau+1.05)*unity+unity, 30+unity, fill='red', outline='')

	
	for i in range(taille_plateau+1):
		cnv2.create_line(5+decalage_x,5+unity*i,(taille_plateau+0.1)*unity+decalage_x,5+unity*i)
		cnv2.create_line(5+unity*i+decalage_x,5,5+unity*i+decalage_x,(taille_plateau+0.1)*unity)



def waithere():
    var = IntVar()
    root.after(25, var.set, 1)
    root.wait_variable(var)


def game_reload():
	btn_reload.pack_forget()
	for j in range(taille_plateau):
		for i in range(taille_plateau):
			if j%2 == 0:
				(cnv2.create_rectangle(i*unity+decalage_x+5,j*unity+decalage_y+5,i*unity+unity+decalage_x+5,j*unity+unity+decalage_y+5, fill='white', outline='black'))
			else:
				(cnv2.create_rectangle((taille_plateau-1-i)*unity+decalage_x+5,j*unity+decalage_y+5,(taille_plateau-1-i)*unity+unity+decalage_x+5,j*unity+unity+decalage_y+5, fill='white', outline='black'))
			
			
			if mute_son == 0 and (i+j)%(taille_plateau) == 0 :
				player = pyglet.media.load(son_reset)
				player.play()
			waithere()
	cnv2.delete('all')
	build_pieces_rouge()
	build_pieces_bleu()
	build_plateau()
	btn_reload.pack()
	
def mute():
	global mute_son

	mute_son = (mute_son+1)%2
	if mute_son == 1:
		btn_mute["text"] = "mute ON"
	else:
		btn_mute["text"] = "mute OFF"
	
	
root = Tk()


root.title("BLO BLO BLO BLOKUS")
if dev_mode == 0:
	root.iconbitmap("./images/logo.ico")

cnv=Canvas(root,width=width_cnv, height=height_cnv,bg='brown')
cnv2 = Canvas(cnv, width=width_cnv2, height=height_cnv2,bg='gray')

cnv.pack()
cnv2.place(x=(width_cnv/2)-width_cnv2/2, y=(height_cnv/2)-height_cnv2/2)
root.lift(cnv2)

build_pieces_rouge()
build_pieces_bleu()
build_plateau() 


btn_reload = Button(cnv,text="restart",command = game_reload)
btn_reload.place(x=(width_cnv/100)*50-20,y=(height_cnv/100)*90)

btn_mute = Button(cnv,text="mute OFF",command = mute)
btn_mute.place(x=(width_cnv/100)*50-29,y=(height_cnv/100)*95)

cnv.bind("<Button-1>",clic)
cnv2.bind("<Button-1>",clic)

root.mainloop()