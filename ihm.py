# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
Plateau de jeu Blokus
"""

from datas import *


#-----------------------MENU
def charger_menu():
	width_menu = 1280
	height_menu = 720
	#font_omori = "./fonts/OMORI_GAME.ttf"
	#font_omori = "Comic Sans MS"

	def bouton_jouer():
		
		menu.destroy()
		charger_root()

	def gcd1(x, y):
		if y == 0:
			return x
		else:
			return gcd1(y, x % y)
		
	pgcd = gcd1(width_menu,height_menu)
	aspect_ratio_width_menu = width_menu/pgcd
	aspect_ratio_height_menu = height_menu/pgcd

	menu = Tk()
	menu.title('MENU BLOKUS')
	if dev_mode == 0:
		menu.iconbitmap("./images/logo.ico")
	menu.geometry(str(width_menu)+"x"+str(height_menu))
	label_menu = Label(menu, text='BLO BLO BLO BLOKUS', font=('Arial 50'))
	label_menu.place(x=(20*width_menu/100),y=10)

	if dev_mode == 0 and mute_son == 0:
		player = pyglet.media.load("sons/blokus.wav")
		player.play()


	if dev_mode == 0:
		# Load and display an image_menu 
		#(replace 'your_logo.png' with the path to your image_menu file)

		image_menu = Image.open('./images/logo.png')

		image_menu = image_menu.resize((400,400))

		image_menu = ImageTk.PhotoImage(image_menu)

	# Create a label to display the image
		image_label =Label(menu, image=image_menu)
		image_label.place(x=(width_menu/2-200),y=(height_menu/2-200))

		
		# font = Font(file="./fonts/OMORI_GAME.ttf", family="OMORI_GAME")
		# pyglet.font.add_file('./fonts/OMORI-GAME.ttf')

		# Label(menu, text="OMORI tu connais non", font=('OMORI_GAME',25)).pack()
	# else:
	# 	font



	button1_menu = Button ( menu, text = "Play",font=("Comic Sans MS",30), command=bouton_jouer)
	button1_menu.place(x=10+(25*width_menu/100),y=10+(80*height_menu/100))

	button2_menu = Button ( menu, text = "Settings",font=("Comic Sans MS",30))
	button2_menu.place(x=10+(40*width_menu/100),y=10+(80*height_menu/100))

	button3_menu = Button ( menu, text = "Credits",font=("Comic Sans MS",30))
	button3_menu.place(x=10+(60*width_menu/100),y=10+(80*height_menu/100))


	menu.mainloop()
#-----------------------
def charger_root():
	def build_pieces_rouge():
		global pieces_rouge_loader, nb_pieces_rouge, pieces_rouge_coords_base,decalage_x,pieces_rouge_noms
		
		pieces_rouge_loader = {
			#"NUMERO-X-Y :" (cnv2.create_rectangle((x1, y1, x2, y2, fill='couleur', outline='', tags="rectNUM_RECT"))
			"0-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity, fill='red', outline='', tags="rect0-R")),
			
			"1-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (2*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (2*30)+(1*unity)+unity, fill='red', outline='', tags="rect1-R")),
				"1-1-0-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (2*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (2*30)+(1*unity)+unity, fill='red', outline='', tags="rect1-R")),
			
			"2-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2-R")),
				"2-1-0-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2-R")),
				"2-2-0-2-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2-R")),
			
			"3-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (4*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(3*unity)+unity, fill='red', outline='', tags="rect3-R")),
				"3-0-1-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (4*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(4*unity)+unity, fill='red', outline='', tags="rect3-R")),
				"3-1-1-2-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (4*30)+(4*unity)+unity, fill='red', outline='', tags="rect3-R")),
			
			"4-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4-R")),
				"4-1-0-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4-R")),
				"4-2-0-2-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4-R")),
				"4-3-0-3-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (7*30)+(4*unity)+unity, fill='red', outline='', tags="rect4-R")),
			
			"5-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (8*30)+(5*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (8*30)+(5*unity)+unity, fill='red', outline='', tags="rect5-R")),
				"5-0-1-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (8*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (8*30)+(6*unity)+unity, fill='red', outline='', tags="rect5-R")),
				"5-1-1-2-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (8*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (8*30)+(6*unity)+unity, fill='red', outline='', tags="rect5-R")),
				"5-2-1-3-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (8*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (8*30)+(6*unity)+unity, fill='red', outline='', tags="rect5-R"))
			
			# "6-0-0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (9*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(6*unity)+unity, fill='red', outline='', tags="rect6-R")),
			# 	"6-1-0-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(6*unity)+unity, fill='red', outline='', tags="rect6-R")),
			# 	"6-2-0-2-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (9*30)+(6*unity)+unity, fill='red', outline='', tags="rect6-R")),
			# 	"6-1-1-3-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(7*unity)+unity, fill='red', outline='', tags="rect6-R"))

			}
		
		# pieces_rouge_loader = {
		# 	#"NUMERO-X-Y :" (cnv2.create_rectangle((x1, y1, x2, y2, fill='couleur', outline='', tags="rectNUM_RECT"))
		# 	"0-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity, fill='red', outline='', tags="rect0-R")),
		# 	"1-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (2*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (2*30)+(1*unity)+unity, fill='red', outline='', tags="rect1-R")),
		# 		"1-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (2*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (2*30)+(1*unity)+unity, fill='red', outline='', tags="rect1-R")),
		# 	"2-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2-R")),
		# 		"2-1-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2-R")),
		# 		"2-2-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity)+unity, fill='red', outline='', tags="rect2-R")),
		# 	"3-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (4*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (4*30)+(3*unity)+unity, fill='red', outline='', tags="rect3-R")),
		# 	"4-0-R": (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (5*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (5*30)+(4*unity)+unity, fill='red', outline='', tags="rect4-R"))
		# 	}
		nb_pieces_rouge = len(pieces_rouge_loader)

		pieces_rouge_coords_base = []
		pieces_rouge_noms = []
		for rect_name, rect in pieces_rouge_loader.items():
			nom_rectangle_split = rect_name.split("-")
			if nom_rectangle_split[1] == "0":
				pieces_rouge_coords_base.append(cnv2.coords(rect))
				pieces_rouge_noms.append(rect_name)

		
	def build_pieces_bleu():
		global pieces_bleu_loader, nb_pieces_bleu, pieces_bleu_coords_base,decalage_x,pieces_bleu_noms
		
		pieces_bleu_loader = {
			#"NUMERO-X-Y :" (cnv2.create_rectangle((x1, y1, x2, y2, fill='couleur', outline='', tags="rectNUM_RECT"))
			"0-0-0-0-B": (cnv2.create_rectangle(10, 30, 10+unity, 30+unity, fill='blue', outline='', tags="rect0-B")),
			
			"1-0-0-0-B": (cnv2.create_rectangle(10, (2*30)+(1*unity), 10+unity, (2*30)+(1*unity)+unity, fill='blue', outline='', tags="rect1-B")),
				"1-1-0-1-B": (cnv2.create_rectangle(10+unity, (2*30)+(1*unity), 10+unity*2, (2*30)+(1*unity)+unity, fill='blue', outline='', tags="rect1-B")),
			
			"2-0-0-0-B": (cnv2.create_rectangle(10, (3*30)+(2*unity), 10+unity, (3*30)+(2*unity)+unity, fill='blue', outline='', tags="rect2-B")),
				"2-1-0-1-B": (cnv2.create_rectangle(10+unity, (3*30)+(2*unity), 10+unity*2, (3*30)+(2*unity)+unity, fill='blue', outline='', tags="rect2-B")),
				"2-2-0-2-B": (cnv2.create_rectangle(10+unity*2, (3*30)+(2*unity), 10+unity*3, (3*30)+(2*unity)+unity, fill='blue', outline='', tags="rect2-B")),
			
			"3-0-0-0-B": (cnv2.create_rectangle(10, (4*30)+(3*unity), 10+unity, (4*30)+(3*unity)+unity, fill='blue', outline='', tags="rect3-B")),
				"3-0-1-1-B": (cnv2.create_rectangle(10, (4*30)+(4*unity), 10+unity, (4*30)+(4*unity)+unity, fill='blue', outline='', tags="rect3-B")),
				"3-1-1-2-B": (cnv2.create_rectangle(10+unity, (4*30)+(4*unity), 10+unity*2, (4*30)+(4*unity)+unity, fill='blue', outline='', tags="rect3-B")),
			
			"4-0-0-0-B": (cnv2.create_rectangle(10, (7*30)+(4*unity), 10+unity, (7*30)+(4*unity)+unity, fill='blue', outline='', tags="rect4-B")),
				"4-1-0-1-B": (cnv2.create_rectangle(10+unity, (7*30)+(4*unity), 10+unity*2, (7*30)+(4*unity)+unity, fill='blue', outline='', tags="rect4-B")),
				"4-2-0-2-B": (cnv2.create_rectangle(10+unity*2, (7*30)+(4*unity), 10+unity*3, (7*30)+(4*unity)+unity, fill='blue', outline='', tags="rect4-B")),
				"4-3-0-3-B": (cnv2.create_rectangle(10+unity*3, (7*30)+(4*unity), 10+unity*4, (7*30)+(4*unity)+unity, fill='blue', outline='', tags="rect4-B")),
			
			"5-0-0-0-B": (cnv2.create_rectangle(10, (8*30)+(5*unity), 10+unity, (8*30)+(5*unity)+unity, fill='blue', outline='', tags="rect5-B")),
				"5-0-1-1-B": (cnv2.create_rectangle(10, (8*30)+(6*unity), 10+unity, (8*30)+(6*unity)+unity, fill='blue', outline='', tags="rect5-B")),
				"5-1-1-2-B": (cnv2.create_rectangle(10+unity, (8*30)+(6*unity), 10+unity*2, (8*30)+(6*unity)+unity, fill='blue', outline='', tags="rect5-B")),
				"5-2-1-3-B": (cnv2.create_rectangle(10+unity*2, (8*30)+(6*unity), 10+unity*3, (8*30)+(6*unity)+unity, fill='blue', outline='', tags="rect5-B"))
			
			# "6-0-0-0-B": (cnv2.create_rectangle(10, (9*30)+(6*unity), 10+unity, (9*30)+(6*unity)+unity, fill='blue', outline='', tags="rect6-B")),
			# 	"6-1-0-1-B": (cnv2.create_rectangle(10+unity, (9*30)+(6*unity), 10+unity*2, (9*30)+(6*unity)+unity, fill='blue', outline='', tags="rect6-B")),
			# 	"6-2-0-2-B": (cnv2.create_rectangle(10+unity*2, (9*30)+(6*unity), 10+unity*3, (9*30)+(6*unity)+unity, fill='blue', outline='', tags="rect6-B")),
			# 	"6-1-1-3-B": (cnv2.create_rectangle(10+unity, (9*30)+(7*unity), 10+unity*2, (9*30)+(7*unity)+unity, fill='blue', outline='', tags="rect6-B"))
			}
		nb_pieces_bleu = len(pieces_bleu_loader)

		pieces_bleu_coords_base = []
		pieces_bleu_noms = []
		for rect_name, rect in pieces_bleu_loader.items():
			nom_rectangle_split = rect_name.split("-")
			if nom_rectangle_split[1] == "0":
				pieces_bleu_coords_base.append(cnv2.coords(rect))
				pieces_bleu_noms.append(rect_name)
		

	def build_plateau():
			
		#cnv2.create_rectangle((taille_plateau+1.05)*unity, 30, (taille_plateau+1.05)*unity+unity, 30+unity, fill='red', outline='')

		
		for i in range(taille_plateau+1):
			cnv2.create_line(5+decalage_x,5+unity*i,(taille_plateau+0.1)*unity+decalage_x,5+unity*i)
			cnv2.create_line(5+unity*i+decalage_x,5,5+unity*i+decalage_x,(taille_plateau+0.1)*unity)


	def waithere():
		var = IntVar()
		root.after(25, var.set, 1)
		root.wait_variable(var)





	def game_reload():
		global nb_tours

		btn_reload.place_forget()
		btn_mute.place_forget()
		cnv2.unbind("<Button-1>")

		for j in range(taille_plateau):
			for i in range(taille_plateau):
				if j%2 == 0:
					(cnv2.create_rectangle(i*unity+decalage_x+5,j*unity+decalage_y+5,i*unity+unity+decalage_x+5,j*unity+unity+decalage_y+5, fill='white', outline='black'))
				else:
					(cnv2.create_rectangle((taille_plateau-1-i)*unity+decalage_x+5,j*unity+decalage_y+5,(taille_plateau-1-i)*unity+unity+decalage_x+5,j*unity+unity+decalage_y+5, fill='white', outline='black'))
				
				
				if mute_son == 0 and (i+j)%(taille_plateau) == 0 and dev_mode == 0 :
					joueur = pyglet.media.load(son_reset)
					joueur.play()
				waithere()

		cnv2.delete('all')

		nb_tours = 0

		btn_reload.place(x=(width_cnv/100)*50-20,y=(height_cnv/100)*90)
		btn_mute.place(x=(width_cnv/100)*50-29,y=(height_cnv/100)*95)
		cnv2.bind("<Button-1>",clic)



		build_pieces_rouge()
		build_pieces_bleu()
		build_plateau()
		
	def mute():
		global mute_son

		mute_son = (mute_son+1)%2
		if mute_son == 1:
			btn_mute["text"] = "Mute ON"
		else:
			btn_mute["text"] = "Mute OFF"
			
			
	def clic(event):
		global c,rectangle,nom_rectangle,tag_rectangle,nom_rectangle_split,nom_rectangle_complet,derniere_piece_bleu_jouee,derniere_piece_rouge_jouee,joueur
		

		joueur = nb_tours%nb_joueurs+1
		
		#joueur = 1

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
			
			


	def afficher_plateau_console():
		for k in plateau:
			print(k)	

			
	def deposer(x,y):
		global taille_plateau,nb_tours,rectangle,nom_rectangle,flag_pose,nom_rectangle_split,mute_son,tag_rectangle,joueur,nom_rectangle_complet,coord_base
			
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
						total_code += verif_alentours(int((tag[0]//unity)-decalage_x//unity),int(tag[1]//unity),joueur)
						
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

		
		# afficher_plateau_console()		
		if (move == False):

			print(joueur)

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













	root = Tk()


	root.title("BLO BLO BLO BLOKUS")
	if dev_mode == 0:
		root.iconbitmap("./images/logo.ico")

	cnv=Canvas(root,width=width_cnv, height=height_cnv,bg='brown')
	cnv2 = Canvas(cnv, width=width_cnv2, height=height_cnv2,bg='gray')

	cnv.pack()
	cnv2.place(x=(width_cnv/2)-width_cnv2/2, y=(height_cnv/2)-height_cnv2/2)
	root.lift(cnv2)


	btn_reload = Button(cnv,text="Restart",command = game_reload)
	btn_reload.place(x=(width_cnv/100)*50-20,y=(height_cnv/100)*90)

	btn_mute = Button(cnv,text="Mute OFF",command = mute)
	btn_mute.place(x=(width_cnv/100)*50-29,y=(height_cnv/100)*95)


	cnv2.bind("<Button-1>",clic)

	build_pieces_rouge()
	build_pieces_bleu()
	build_plateau()


	root.mainloop()