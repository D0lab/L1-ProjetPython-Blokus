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


	def bouton_jouer():
		
		menu.destroy()
		charger_play()

	def bouton_settings():
     
		menu.destroy()
		charger_settings()
 	
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
		
	
		Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',50,'bold')
		font_bouton = ('OMORI_GAME',30)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)

	menu.geometry(str(width_menu)+"x"+str(height_menu))




	label_menu = Label(menu, text='BLO BLO BLO BLOKUS', font=font_label)
	label_menu.place(x=(20*width_menu/100),y=10)
	
	if dev_mode == 0 and mute_son == 0:
		player = pygame.mixer.music.load("sons/blokus.wav")
		pygame.mixer.music.play()


	if dev_mode == 0:
		# Load and display an image_menu 
		#(replace 'your_logo.png' with the path to your image_menu file)

		image_menu = Image.open('./images/logo.png')

		image_menu = image_menu.resize((400,400))

		image_menu = ImageTk.PhotoImage(image_menu)

	# Create a label to display the image
		image_label =Label(menu, image=image_menu)
		image_label.place(x=(width_menu/2-200),y=(height_menu/2-200))

	button1_menu = Button ( menu, text = "Play",font=font_bouton, command=bouton_jouer)
	button1_menu.place(x=10+(25*width_menu/100),y=10+(80*height_menu/100))

	button2_menu = Button ( menu, text = "Settings",font=font_bouton, command=bouton_settings)
	button2_menu.place(x=10+(40*width_menu/100),y=10+(80*height_menu/100))

	button3_menu = Button ( menu, text = "Credits",font=font_bouton)
	button3_menu.place(x=10+(60*width_menu/100),y=10+(80*height_menu/100))


	menu.mainloop()
 
#-----------------------
def charger_play():
	play=Tk()
	play.title('SETTINGS BLOKUS')
	Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")

	def player(x):
		
		bot_slider["to"] = 4-int(x)

	
 
	master_frame=Frame(play)
	master_frame.pack(pady=20)
 
	controls_frame = Frame(master_frame)
	controls_frame.pack(pady=20)
 
	player_frame = LabelFrame(master_frame, text="Nombre de joueurs")
	player_frame.pack(pady=20)

	player_var=DoubleVar()
	player_var.set(1)
 
	player_slider= Scale(player_frame, 
                      	from_=0,
                        to=4,
                        orient=HORIZONTAL,
                        length=500,
                        variable=player_var,
						command=player
                        )
	player_slider.pack()

	player_slider.set(1)

 
	bot_frame = LabelFrame(master_frame, text="Nombre de robots")
	bot_frame.pack(pady=20)

	bot_var=DoubleVar()
	bot_var.set(3)

	bot_slider= Scale(bot_frame, 
						from_=0,
						to=3,
						orient=HORIZONTAL,
						length=500,
						variable=bot_var
						)
	

	bot_slider.set(3)
	bot_slider.pack()






	play.mainloop()


	
def charger_settings():
    
	settings=Tk()
	settings.title('SETTINGS BLOKUS')
	Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")

 
	def volume(x):
		pygame.mixer.music.set_volume(volume_slider.get()/100)
		# print(volume_slider.get()/100)
	
 
	# def sliding (value):
	#  	my_label.configure(text=int(value))
	
 
	master_frame=Frame(settings)
	master_frame.pack(pady=20)
 
	controls_frame = Frame(master_frame)
	controls_frame.pack(pady=20)
 
	volume_frame = LabelFrame(master_frame, text="Volume")
	volume_frame.pack(pady=20)

	son_var=DoubleVar()
	son_var.set(0.5)
 
	volume_slider= Scale(volume_frame, 
                      	from_=0,
                        to=100,
                        orient=HORIZONTAL,
                        command=volume,
                        length=500,
                        variable=son_var
                        )
	volume_slider.pack()

	volume_slider.set(0.5)
	
	
	# my_label = Label(settings,text=volume_slider.get(),font=('OMORI_GAME', 18))
	# my_label.pack(pady=20)
 

		
    
    
	settings.mainloop()


def charger_final(score):

		final=Tk()
		final.title('FINAL BLOKUS')
		# Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")


		resultat=Label(final, text="Scores Finaux", font=("Arial",34))
		resultat.pack()

		score=Label(final,text=score, font=("Arial",34))
		score.pack()


		final.mainloop()
#-----------------------

def charger_root():
	
	
		
	def build_pieces():
		global loader

		loader = []

		for i in range(nb_joueurs):
			
			coul_fr = liste_couleurs_fr[i]
			coul_en = liste_couleurs_en[i]


						
			globals()[f"pieces_{coul_fr}_loader"] = {
				#"NUMERO-X-Y :" (cnv2.create_rectangle((x1, y1, x2, y2, fill='couleur', outline='', tags=f"rectNUM_RECT"))
				f"0-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, 30, 10+unity, 30+unity, fill=coul_en, outline='', tags=f"rect0-{coul_fr[0:1]}")),
				
				f"1-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (2*30)+(1*unity), 10+unity, (2*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect1-{coul_fr[0:1]}")),
					f"1-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (2*30)+(1*unity), 10+unity*2, (2*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect1-{coul_fr[0:1]}")),
				
				f"2-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (3*30)+(2*unity), 10+unity, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect2-{coul_fr[0:1]}")),
					f"2-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (3*30)+(2*unity), 10+unity*2, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect2-{coul_fr[0:1]}")),
					f"2-2-0-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (3*30)+(2*unity), 10+unity*3, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect2-{coul_fr[0:1]}")),
				
				f"3-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (4*30)+(3*unity), 10+unity, (4*30)+(3*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
					f"3-0-1-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (4*30)+(4*unity), 10+unity, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
					f"3-1-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (4*30)+(4*unity), 10+unity*2, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
				
				f"4-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (6*30)+(4*unity), 10+unity, (6*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
					f"4-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (6*30)+(4*unity), 10+unity*2, (6*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
				 	f"4-2-0-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (6*30)+(4*unity), 10+unity*3, (6*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
				 	f"4-3-0-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*3, (6*30)+(4*unity), 10+unity*4, (6*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
				
				 f"5-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (7*30)+(5*unity), 10+unity, (7*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
				 	f"5-0-1-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (7*30)+(6*unity), 10+unity, (7*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
					f"5-1-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (7*30)+(6*unity), 10+unity*2, (7*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
					f"5-2-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (7*30)+(6*unity), 10+unity*3, (7*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
				
				f"6-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (9*30)+(6*unity), 10+unity, (9*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
				 	f"6-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (9*30)+(6*unity), 10+unity*2, (9*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
				 	f"6-2-0-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (9*30)+(6*unity), 10+unity*3, (9*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
				 	f"6-1-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (9*30)+(7*unity), 10+unity*2, (9*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
      
				f"7-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (10*30)+(8*unity), 10+unity, (10*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),
					f"7-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (10*30)+(8*unity), 10+unity*2, (10*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),
					f"7-0-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (10*30)+(9*unity), 10+unity, (10*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),
					f"7-1-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (10*30)+(9*unity), 10+unity*2, (10*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),

				f"8-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (12*30)+(9*unity), 10+unity, (12*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
					f"8-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (12*30)+(9*unity), 10+unity*2, (12*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
					f"8-1-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (12*30)+(10*unity), 10+unity, (12*30)+(10*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
					f"8-2-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (12*30)+(10*unity), 10+unity*3, (12*30)+(10*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
     
				f"9-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity,  fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
				 	f"9-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
				 	f"9-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
					f"9-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
				 	f"9-3-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),

				f"10-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (3*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
				 	f"10-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
				 	f"10-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity)+unity,  fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
				 	f"10-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity)+unity,  fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
				 	f"10-3-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (3*30)+(2*unity)+unity,  fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),

				# f"11-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
				#  	f"11-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, 30+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
				#  	f"11-0-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(2*unity), fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
				#   f"11-1-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(2*unity), fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
				#  	f"11-2-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(2*unity), fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),

				# f"12-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity, fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
				# 	f"12-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
				# 	f"12-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
				# 	f"12-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
				# 	f"12-2-0-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(0*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(0*unity)+unity, fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
				}
			
			nb_pieces_bleu = len(globals()[f"pieces_{coul_fr}_loader"])

			globals()[f"pieces_{coul_fr}_coords_base"] = []
			globals()[f"pieces_{coul_fr}_noms"] = []
			globals()[f"pieces_{coul_fr}_utiles"] = []
			
			flag_y = False
			flag_y_nom = None
			flag_num_rect = None
			
			for rect_name, rect in globals()[f"pieces_{coul_fr}_loader"].items():
				nom_rectangle_split = rect_name.split("-")
				
				if flag_y_nom != nom_rectangle_split[2] :					
					flag_y = False

				if flag_num_rect != nom_rectangle_split[0]:
					flag_y = False
					flag_y_nom = None


				if (nom_rectangle_split[1] == "0" or nom_rectangle_split[1] == "1" or nom_rectangle_split[1] == "2") and flag_y == False:
					coords_charge = cnv2.coords(rect)
					if int(nom_rectangle_split[0]) <= 8: 					
						coords_charge[0] = 10
						coords_charge[2] = 10+unity
					else:				
						coords_charge[0] = (width_cnv2/2)+(taille_plateau*unity/2)+unity
						coords_charge[2] = (width_cnv2/2)+(taille_plateau*unity/2)+unity*2

					globals()[f"pieces_{coul_fr}_coords_base"].append(coords_charge)
					globals()[f"pieces_{coul_fr}_noms"].append(rect_name)
					globals()[f"pieces_{coul_fr}_utiles"].append([nom_rectangle_split[0],nom_rectangle_split[1],nom_rectangle_split[2],nom_rectangle_split[3]])
					flag_y_nom = nom_rectangle_split[2]
					flag_y = True
					flag_num_rect = nom_rectangle_split[0]
				

					
			print(globals()[f"pieces_{coul_fr}_noms"])
			print(globals()[f"pieces_{coul_fr}_utiles"])
			
			loader.append(globals()[f"pieces_{coul_fr}_loader"])

			
		

	def build_plateau():
			
		#cnv2.create_rectangle((taille_plateau+1.05)*unity, 30, (taille_plateau+1.05)*unity+unity, 30+unity, fill='red', outline='')

		
		for i in range(taille_plateau+1):
			cnv2.create_line(5+decalage_x,5+unity*i,(taille_plateau+0.1)*unity+decalage_x,5+unity*i)
			cnv2.create_line(5+unity*i+decalage_x,5,5+unity*i+decalage_x,(taille_plateau+0.1)*unity)


	def waithere():
		var = IntVar()
		root.after(100, var.set, 1)
		root.wait_variable(var)





	def game_reload():
		global nb_tours,plateau,nb_joueurs_out,liste_joueurs_out,loader

		btn_reload.place_forget()
		btn_mute.place_forget()
		cnv2.unbind("<Button-1>")

		# for j in range(taille_plateau):
		# 	for i in range(taille_plateau):
		# 		if j%2 == 0:
		# 			(cnv2.create_rectangle(i*unity+decalage_x+5,j*unity+decalage_y+5,i*unity+unity+decalage_x+5,j*unity+unity+decalage_y+5, fill='white', outline='black'))
		# 		else:
		# 			(cnv2.create_rectangle((taille_plateau-1-i)*unity+decalage_x+5,j*unity+decalage_y+5,(taille_plateau-1-i)*unity+unity+decalage_x+5,j*unity+unity+decalage_y+5, fill='white', outline='black'))
				
		for i in range(taille_plateau):
			(cnv2.create_rectangle(0*unity+decalage_x+5,i*unity+decalage_y+5,(taille_plateau-1)*unity+unity+decalage_x+5,i*unity+unity+decalage_y+5, fill='white', outline='black'))
				


			if mute_son == 0 and (i)%(taille_plateau//3) == 0 and dev_mode == 0 :
				joueur = pygame.mixer.music.load(son_placement_piece)
				pygame.mixer.music.play()
			waithere()

		cnv2.delete('all')

		nb_tours = 0
		nb_joueurs_out = 0

		

		plateau = []
		liste_joueurs_out = []



		for i in range(taille_plateau):
			plateau_temp = []
			for j in range(taille_plateau):
				plateau_temp.append(0)

			plateau.append(plateau_temp)

		btn_reload.place(x=(width_cnv/100)*50-20,y=(height_cnv/100)*90)
		btn_mute.place(x=(width_cnv/100)*50-29,y=(height_cnv/100)*95)
		cnv2.bind("<Button-1>",clic)

		
			



		build_pieces()
		build_plateau()
		for couleurs in range(1,nb_joueurs):
			for pieces_nom,pieces_num in globals()[f"pieces_{liste_couleurs_fr[couleurs]}_loader"].items():
				cnv2.itemconfigure(pieces_num,state="hidden")
		
		loader = []
		for i in range(nb_joueurs):
			loader.append(globals()[f"pieces_{liste_couleurs_fr[i]}_loader"])
		

		
		
	def mute():
		global mute_son

		mute_son = (mute_son+1)%2
		if mute_son == 1:
			btn_mute["text"] = "Mute ON"
		else:
			btn_mute["text"] = "Mute OFF"
			
			
	def clic(event):
		global c,rectangle,nom_rectangle,tag_rectangle,nom_rectangle_split,nom_rectangle_complet,derniere_piece_bleu_jouee,derniere_piece_rouge_jouee,joueur,nb_joueurs_out,bot
		

		# joueur = 1

		if joueur not in bot:
			coul=liste_couleurs_fr[joueur-1]
			pieces_loader = globals()[f"pieces_{coul}_loader"]
			for rect_name, rect in pieces_loader.items():
				coords = cnv2.coords(rect)
				if event.x >= coords[0] and event.x <= coords[2] and event.y >= coords[1] and event.y <= coords[3]:
					rectangle = rect
					nom_rectangle_split = rect_name.split("-")
					nom_rectangle = nom_rectangle_split[0]
					nom_rectangle_complet = rect_name
					tag_rectangle = "rect"+nom_rectangle+"-"+nom_rectangle_split[4]

					globals()[f"derniere_piece_{coul}_jouee"] = nom_rectangle

					c = (c+1)%2 #TEST SI CLIC OU DECLIC
					if (c == 1):
			
						cnv2["cursor"] = "fleur"
						cnv2.bind("<Motion>",glisser)
						old[0]=event.x
						old[1]=event.y
					else:
			
						cnv2["cursor"] = "arrow"
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
		global taille_plateau,nb_tours,rectangle,nom_rectangle,flag_pose,nom_rectangle_split,mute_son,tag_rectangle,joueur,nom_rectangle_complet,coord_base,plateau
			
		x1, y1, x2, y2 = cnv2.coords(rectangle)
		
		move = False
		for i in range(taille_plateau):
			for j in range(taille_plateau):
				if (5+i*unity+decalage_x <= x<= 5+(i+1)*unity+decalage_x and 5+j*unity <= y <= 5+(j+1)*unity):
					# print("----EMPLACEMENT CASE----",i,j)


					flag_verif_boucle = True
					tagged_rectangles = []
					for item in cnv2.find_withtag(tag_rectangle):
						coordinates = cnv2.coords(item)
						tagged_rectangles.append(coordinates)
					
					i=(tagged_rectangles[int(nom_rectangle_split[3])][0])//unity-decalage_x//unity
					j=tagged_rectangles[int(nom_rectangle_split[3])][1]//unity



					total_code = 0
					for tag in tagged_rectangles:
						total_code += verif_alentours(int((tag[0]//unity)-decalage_x//unity),int(tag[1]//unity),joueur,plateau,nb_tours)
						
					if total_code <= 0:
						flag_verif_boucle = False
							

					if flag_verif_boucle:
						cnv2.move(tag_rectangle,5+i*unity-x1+decalage_x,5+j*unity-y1)
						for tag in tagged_rectangles:
							plateau[int(tag[1]//unity)][int((tag[0]//unity)-decalage_x//unity)] = joueur
						move = True
						

						flag_estSuppr = False
						compteur_estSuppr = 0

						if mute_son == 0 :
							joueur = pygame.mixer.music.load(son_placement_piece)
							pygame.mixer.music.play()





						
						coul = liste_couleurs_fr[joueur-1]
							
						for i in range(5):
							try:					
									
								for rect_name, rect in globals()[f"pieces_{coul}_loader"].items():
									globals()[f"{coul}_nom_rectangle_split"] = rect_name.split("-")
									if globals()[f"{coul}_nom_rectangle_split"][0] == nom_rectangle:
										globals()[f"pieces_{coul}_loader"].pop(rect_name)

									
								compteur_estSuppr+=1
							except:
								pass
								
						flag_pose = 1
						

						
						nb_tours += 1

						
						verif_fin(plateau)

						
						
	

						while nb_tours%nb_joueurs+1 in liste_joueurs_out:
							nb_tours += 1

						for pieces_nom,pieces_num in loader[joueur-1].items():
							cnv2.itemconfigure(pieces_num,state="hidden")
						
						joueur = nb_tours%nb_joueurs+1
						tour_joueur()

						for pieces_nom,pieces_num in loader[joueur-1].items():
							cnv2.itemconfigure(pieces_num,state="normal")

						if joueur in bot:
							bot_coup()
						



		
		# afficher_plateau_console()		
		if (move == False):			
			
			for i in range(len(globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"])):
				
				if nom_rectangle_split[0] == globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][0] and nom_rectangle_split[2] == globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][2]:
					num_index_rect = str(globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][3])
					y_index_rect = str(globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][1]) 

			index_rect = globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_noms"].index(nom_rectangle_split[0]+"-"+y_index_rect+"-"+nom_rectangle_split[2]+"-"+num_index_rect+"-"+nom_rectangle_split[4])
			coord_base = globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_coords_base"][index_rect]

			cnv2.move(tag_rectangle,coord_base[0]-x1+unity*int(nom_rectangle_split[1]),coord_base[1]-y1)

	def score():
		resu1=0
		resu2=0
		score = []

		
		derniere_piece = []
		for i in range(nb_joueurs):
			#globals()[f"derniere_piece_{liste_couleurs_fr[i]}_jouee"] = None
			score.append(0)
			derniere_piece.append(globals()[f"derniere_piece_{liste_couleurs_fr[i]}_jouee"])

		for i in range(len(loader)):
			if len(loader[i]) == 0:
				if derniere_piece[i] == "0":
					score[i] += 20
				else:
					score[i] += 15
			else:
				score[i] -= len(loader[i])


		return score


	def verif_carres_possibilites(joueur,plateau):
		compteur_possibilites = 0
		liste_possibilites = []

		

		for i in range(len(plateau)):
			for j in range(len(plateau[0])):
				if plateau[i][j] == 0:
					if verif_alentours(j,i,joueur,plateau,nb_tours) == 1:
						compteur_possibilites += 1
						liste_possibilites.append([j,i])
		return liste_possibilites
	

	def verif_pieces_possibilites(joueur,plateau):
		liste_poss = verif_carres_possibilites(joueur,plateau)

		liste_coups_possibles = []


		
		for poss in liste_poss:

			for rect_name, rect in loader[joueur-1].items():
						verif_rect_name_split = rect_name.split("-")
						tag_rectangle = "rect"+verif_rect_name_split[0]+"-"+verif_rect_name_split[4]
						verif_x1,verif_y1,verif_x2,verif_y2 = cnv2.coords(rect)

						
						tagged_rectangles = []
						for item in cnv2.find_withtag(tag_rectangle):
							coordinates = cnv2.coords(item)
							tagged_rectangles.append([(verif_x1-coordinates[0])//unity,(verif_y1-coordinates[1])//unity])

						total_code = 0
						for tag in tagged_rectangles:
							total_code += verif_alentours(int(poss[0]-tag[0]),int(poss[1]-tag[1]),joueur,plateau,nb_tours)
						if total_code > 0:
							liste_coups_possibles.append([poss,rect_name,rect])

		return liste_coups_possibles


	def verif_fin(plateau):
		global nb_joueurs_out,nb_tours,liste_joueurs_out


		for i in range(1,nb_joueurs+1):
			if len(verif_pieces_possibilites(i,plateau)) == 0 or len(loader[i-1]) == 0:	
				# print(len(verif_pieces_possibilites(i,plateau)))
				if i not in liste_joueurs_out :
					liste_joueurs_out.append(i)
					nb_joueurs_out += 1

					print("joueur",i,"est out")
			
			if nb_joueurs_out == nb_joueurs:
				root.destroy()
				charger_final(score())

	def bot_coup():
		global rectangle,nom_rectangle_split,nom_rectangle_complet,nom_rectangle,tag_rectangle,derniere_piece_rouge_jouee,derniere_piece_bleu_jouee,nb_tours,joueur,plateau

		coups_poss = verif_pieces_possibilites(joueur,plateau)
		coup_aleatoire = coups_poss[randint(0,len(coups_poss)-1)]


		rectangle = coup_aleatoire[2]
		nom_rectangle_split = coup_aleatoire[1].split("-")
		nom_rectangle = nom_rectangle_split[0]
		nom_rectangle_complet = coup_aleatoire[1]
		tag_rectangle = "rect"+nom_rectangle+"-"+nom_rectangle_split[4]

		
		coul = liste_couleurs_fr[joueur-1]		
		globals()[f"derniere_piece_{coul}_jouee"] = nom_rectangle
		


		i = coup_aleatoire[0][0]
		j = coup_aleatoire[0][1]


		# print("----EMPLACEMENT CASE BOT----",i,j)
		# print(coup_aleatoire)

		x1,y1,x2,y2 = cnv2.coords(rectangle)

		
		cnv2.move(tag_rectangle,5+i*unity-x1+decalage_x,5+j*unity-y1)
				
		tagged_rectangles = []
		for item in cnv2.find_withtag(tag_rectangle):
			coordinates = cnv2.coords(item)
			tagged_rectangles.append(coordinates)

		for tag in tagged_rectangles:
			plateau[int(tag[1]//unity)][int((tag[0]//unity)-decalage_x//unity)] = joueur
			

		flag_estSuppr = False
		compteur_estSuppr = 0

		if mute_son == 0 :
			joueur = pygame.mixer.music.load(son_placement_piece)
			pygame.mixer.music.play()





		
		for i in range(5):
			try:					
					
				for rect_name, rect in globals()[f"pieces_{coul}_loader"].items():
					globals()[f"{coul}_nom_rectangle_split"] = rect_name.split("-")
					if globals()[f"{coul}_nom_rectangle_split"][0] == nom_rectangle:
						globals()[f"pieces_{coul}_loader"].pop(rect_name)

					
				compteur_estSuppr+=1
			except:
				pass
				
		flag_pose = 1
		

		
		nb_tours += 1

		
		verif_fin(plateau)

		

		while nb_tours%nb_joueurs+1 in liste_joueurs_out:
			nb_tours += 1

		for pieces_nom,pieces_num in loader[joueur-1].items():
			cnv2.itemconfigure(pieces_num,state="hidden")
		
		joueur = nb_tours%nb_joueurs+1

		for pieces_nom,pieces_num in loader[joueur-1].items():
			cnv2.itemconfigure(pieces_num,state="normal")


		if joueur in bot:
			bot_coup()
		
	def tour_joueur():
		tour_de["text"]= f"Au tour du joueur {liste_couleurs_fr[joueur-1]}"
		tour_de["bg"]=liste_couleurs_en[joueur-1]

	

	root = Tk()


	root.title("BLO BLO BLO BLOKUS")
	if dev_mode == 0:
		root.iconbitmap("./images/logo.ico")

	cnv=Canvas(root,width=width_cnv, height=height_cnv,bg='brown')
	cnv2 = Canvas(cnv, width=width_cnv2, height=height_cnv2,bg='gray')

	cnv.pack()
	cnv2.place(x=(width_cnv/2)-width_cnv2/2, y=(height_cnv/2)-height_cnv2/2)
	root.lift(cnv2)

	tour_de= Label(root, text="Au tour du joueur bleu", bg="blue")
	tour_de.place(x=(width_cnv/100)*50-20,y=(height_cnv/100)*5)

	btn_reload = Button(cnv,text="Restart",command = game_reload)
	btn_reload.place(x=(width_cnv/100)*50-20,y=(height_cnv/100)*90)

	btn_mute = Button(cnv,text="Mute OFF",command = mute)
	btn_mute.place(x=(width_cnv/100)*50-29,y=(height_cnv/100)*95)


	cnv2.bind("<Button-1>",clic)

	# build_pieces_rouge()
	build_pieces()
	build_plateau()

	


	for couleurs in range(1,nb_joueurs):
		for pieces_nom,pieces_num in globals()[f"pieces_{liste_couleurs_fr[couleurs]}_loader"].items():
			cnv2.itemconfigure(pieces_num,state="hidden")

	if 1 in bot:
		bot_coup()


	root.mainloop()