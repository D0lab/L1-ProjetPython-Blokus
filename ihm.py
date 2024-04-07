# -*- coding: utf-8 -*-
"""
@author: mlaurent,dlabaste
ihm de jeu Blokus
"""

from datas import *

global bot

#-----------------------MENU
def charger_menu():	
	global width_menu,height_menu




	def bouton_jouer():
		
		menu.destroy()
		charger_play()

	def bouton_settings():
	
		menu.destroy()
		charger_settings("menu")

	def bouton_credits():
	
		menu.destroy()
		charger_credits()
		


	

	menu = Tk()
	menu.resizable(width=False, height=False)
	menu.title('MENU - BLOKUS')
	if dev_mode == 0:
		menu.iconbitmap("./images/logo.ico")
		
	
		Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',70,'bold')
		font_bouton = ('OMORI_GAME',50)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)

	menu.geometry(str(width_menu)+"x"+str(height_menu))



	label_menu = Label(menu, text='BLO BLO BLO BLOKUS', font=font_label)
	label_menu.place(x=(width_menu/2-label_menu.winfo_reqwidth()/2),y=(5*width_menu/100))
	
	if mute_son == 0:
		player_son = pygame.mixer.music.load("sons/blokus.wav")
		pygame.mixer.music.play()


	if dev_mode == 0:

		image_menu = Image.open('./images/logo.png')

		image_menu = image_menu.resize((12*unity,12*unity))
		
		largeur_image_menu, hauteur_image_menu = image_menu.size

		image_menu = ImageTk.PhotoImage(image_menu)


		image_label =Label(menu, image=image_menu)
		image_label.place(x=(width_menu/2-largeur_image_menu/2),y=(height_menu/2-hauteur_image_menu/2))

	button1_menu = Button ( menu, text = "Play",font=font_bouton, command=bouton_jouer)
	button1_menu.place(x=(width_menu/2 - button1_menu.winfo_reqwidth()/2 - 25*width_menu/100),y=10+(80*height_menu/100))

	button2_menu = Button ( menu, text = "Settings",font=font_bouton, command=bouton_settings)
	button2_menu.place(x=(width_menu/2 - button2_menu.winfo_reqwidth()/2),y=10+(80*height_menu/100))

	button3_menu = Button ( menu, text = "Credits",font=font_bouton, command=bouton_credits)
	button3_menu.place(x=(width_menu/2 - button3_menu.winfo_reqwidth()/2 + 25*width_menu/100) ,y=10+(80*height_menu/100))


	menu.mainloop()

#-----------------------JOUER
def charger_play():
	global nb_joueurs,bot,nb_joueurs_reels

	bot = []
	nb_joueurs_reels = 1

	
	play=Tk()
	play.resizable(width=False, height=False)
	play.title('NOMBRE DE JOUEUR - BLOKUS')
	
	if dev_mode == 0:
		play.iconbitmap("./images/logo.ico")
		
	
		Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',50,'bold')
		font_bouton = ('OMORI_GAME',30)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)

	def sl_player(x):
		global nb_joueurs_reels
		
		bot_slider["to"] = 4-int(x)

		nb_joueurs_reels = int(x)

	def sl_bot(x):
		global bot,nb_joueurs,nb_joueurs_reels

		bot = []
		for i in range(nb_joueurs_reels+1,int(x)+nb_joueurs_reels+1):
			bot.append(i)

		nb_joueurs = nb_joueurs_reels + int(x)




	
	def bouton_jouer():
		
		play.destroy()
		charger_root()
	
	def bouton_retour():
		
		play.destroy()
		charger_menu()

		

	

	master_frame=Frame(play)
	master_frame.pack(pady=20)

	label_titre = Label(master_frame, text='NOMBRE DE JOUEURS', font=font_label)
	label_titre.pack(anchor="center")	

	controls_frame = Frame(master_frame)
	controls_frame.pack(pady=20)

	player_frame = LabelFrame(master_frame, text="Nombre d'utilisateurs",font=font_bouton)
	player_frame.pack(pady=20)

	player_var=DoubleVar()
	player_var.set(1)

	player_slider= Scale(player_frame, 
						from_=1,
						to=4,
						orient=HORIZONTAL,
						length=500,
						font=font_bouton,
						variable=player_var,
						command=sl_player
						)
	player_slider.pack()

	player_slider.set(1)


	bot_frame = LabelFrame(master_frame, text="Nombre de robots",font=font_bouton)
	bot_frame.pack(pady=20)

	bot_var=DoubleVar()
	bot_var.set(3)

	bot_slider= Scale(bot_frame, 
						from_=0,
						to=3,
						orient=HORIZONTAL,
						length=500,
						font=font_bouton,
						variable=bot_var,
						command=sl_bot
						)
	

	bot_slider.set(3)
	bot_slider.pack()


	button_back = Button (master_frame, text = "Back",font=font_bouton, command=bouton_retour)
	button_back.pack()

	button_play = Button (master_frame, text = "Play",font=font_bouton, command=bouton_jouer)
	button_play.pack()



	
	sl_player(1)
	sl_bot(3)




	play.mainloop()


#-----------------------PARAMETRES
def charger_settings(x):
	global width_menu,height_menu,width_cnv,height_cnv,width_cnv2,height_cnv2,unity
	
	settings=Tk()
	settings.resizable(width=False, height=False)
	settings.title('SETTINGS - BLOKUS')
	if dev_mode == 0:
		settings.iconbitmap("./images/logo.ico")
			
			
		if x == "menu" : 
			Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',50,'bold')
		font_bouton = ('OMORI_GAME',30)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)


	def volume(x):
		global volume_sons
		pygame.mixer.music.set_volume(volume_slider.get()/100)
		
		volume_sons = son_var.get()

	

	
	def bouton_retour():
		settings.destroy()
		if x == "menu":
			charger_menu()
	

	master_frame=Frame(settings)
	master_frame.pack(pady=20)

	label_titre = Label(master_frame, text='SETTINGS', font=font_label)
	label_titre.pack(anchor="center")	

	if mute_son == 0 :

		controls_frame = Frame(master_frame)
		controls_frame.pack(pady=20)

		volume_frame = LabelFrame(master_frame, text="Volume",font=font_bouton)
		volume_frame.pack(pady=20)

		son_var=DoubleVar()
		son_var.set(volume_sons)

		volume_slider= Scale(volume_frame, 
							from_=0,
							to=100,
							orient=HORIZONTAL,
							command=volume,
							length=500,
							font=font_bouton,
							variable=son_var
							)
		volume_slider.pack()

		volume_slider.set(volume_sons)	
	
	



	button_back = Button (master_frame, text = "Back",font=font_bouton, command=bouton_retour)
	
	button_back.pack(pady = 10)
	
	settings.mainloop()


#-----------------------CREDITS
def charger_credits():
	global width_menu,height_menu,width_cnv,height_cnv,width_cnv2,height_cnv2,unity
	
	credits=Tk()
	credits.resizable(width=False, height=False)
	credits.title('CREDITS - BLOKUS')
	if dev_mode == 0:
		credits.iconbitmap("./images/logo.ico")
			
			
		Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',50,'bold')
		font_bouton = ('OMORI_GAME',30)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)
		

	
	def bouton_retour():
		credits.destroy()
		charger_menu()
	


	master_frame=Frame(credits)
	master_frame.pack(pady=0)

	label_titre = Label(master_frame, text='CREDITS', font=font_label)
	label_titre.pack(anchor="center")	

	controls_frame = Frame(master_frame)
	controls_frame.pack(pady=10)

	dev_frame = LabelFrame(master_frame, text="Developpeurs",font=font_bouton)
	dev_frame.pack(pady=10)

	label_dorian = Label(dev_frame, text='Dorian LABASTE', font=font_label)
	label_dorian.pack(pady=2)

	label_matys = Label(dev_frame, text='Matys LAURENT', font=font_label)
	label_matys.pack(pady=2)

	bibli_frame = LabelFrame(master_frame, text="Bibliotheques",font=font_bouton)
	bibli_frame.pack(pady=10)

	label_bibl1 = Label(bibli_frame, text='Random - Math - Tkinter', font=font_label)
	label_bibl1.pack(pady=2)

	label_bibl2 = Label(bibli_frame, text='Customtkinter - Tkextrafont - Time', font=font_label)
	label_bibl2.pack(pady=2)

	label_bibl3 = Label(bibli_frame, text='Pygame - Pillow - Webbrower', font=font_label)
	label_bibl3.pack(pady=2)

	def rickroll():
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


	cheat_frame = LabelFrame(master_frame, text="CHEAT",font=font_bouton)
	cheat_frame.pack(pady=10)

	button_rickroll = Button(cheat_frame, text="cheat", font=font_bouton, command=rickroll)
	button_rickroll.pack(pady=5)

	button_back = Button (master_frame, text = "Back",font=font_bouton, command=bouton_retour)	
	button_back.pack(pady = 5)
	
	


		
	
	
	credits.mainloop()


#-----------------------ECRAN DE FIN
def charger_final(score):

	def classement():
		global podium,prem_place


		score_temp = score.copy()
		score_temp.sort(reverse = True)

		
		

		prem_place = [score_temp[0]]
		deux_place = []
		trois_place = []
		quatr_place = []

		podium = [prem_place,deux_place,trois_place,quatr_place]

		score_temp.pop(0)

		for i in range(len(score_temp)):
			if prem_place[0][0] == score_temp[0][0]:
				prem_place.append(score_temp[0])
				score_temp.pop(0)

			elif len(deux_place) == 0:
				deux_place.append(score_temp[0])
				score_temp.pop(0)
			elif deux_place[0][0] == score_temp[0][0]:
				deux_place.append(score_temp[0])
				score_temp.pop(0)

			elif len(trois_place) == 0:
				trois_place.append(score_temp[0])
				score_temp.pop(0)
			elif trois_place[0][0] == score_temp[0][0]:
				trois_place.append(score_temp[0])
				score_temp.pop(0)

			elif len(quatr_place) == 0:
				quatr_place.append(score_temp[0])
				score_temp.pop(0)
			elif quatr_place[0][0] == score_temp[0][0]:
				quatr_place.append(score_temp[0])
				score_temp.pop(0)


	final=Tk()
	final.resizable(width=False, height=False)
	final.title('FINAL - BLOKUS')
	
	cnv = Canvas(final, width=width_menu, height=height_menu, bg='white')
	cnv.pack()

	classement()

	if dev_mode == 0:
		final.iconbitmap("./images/logo.ico")
		
	
		Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',50,'bold')
		font_bouton = ('OMORI_GAME',50)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)

	final.geometry(str(width_menu)+"x"+str(height_menu))


	if dev_mode == 0:

		image_menu = Image.open('./images/podium.png')
		image_menu = image_menu.resize((width_menu//2,height_menu//2))

		j_bleu = Image.open('./images/bleu.png')
		j_bleu = j_bleu.resize((150//2,150//2))

		j_rouge = Image.open('./images/rouge.png')
		j_rouge = j_rouge.resize((150//2,150//2))

		j_vert = Image.open('./images/vert.png')
		j_vert = j_vert.resize((150//2,150//2))

		j_jaune = Image.open('./images/jaune.png')
		j_jaune = j_jaune.resize((150//2,150//2))

		images_couleur = [j_bleu,j_rouge,j_vert,j_jaune]
	
		coords_1 = [(275,180),(85,240),(460,280),(350,400)]		
		coords_2 = [[(220,180),(300,180),(230,100),(310,100)],[(20,240),(100,240),(60,160)],[(420,280),(500,280)]]

		coords_txt = [(275,200),(85,260),(460,300),(350,420)]

		draw = ImageDraw.Draw(image_menu)
		font = ImageFont.truetype("arial.ttf", size=42)

		for i in range(len(podium)):
			if len(podium[i]) == 1 :
				image_menu.paste(images_couleur[podium[i][0][1]], coords_1[i])

				text_width = draw.textlength(str(podium[i][0][0]), font)
				image_width, image_height = j_bleu.size
				x = (image_width - text_width) / 2


				draw.text((coords_1[i][0]+x,coords_1[i][1]+14.5), str(podium[i][0][0]), font=font, fill="black")
			else:		
				for j in range(len(podium[i])):	

					text_width = draw.textlength(str(podium[i][j][0]), font)
					image_width, image_height = j_bleu.size
					x = (image_width - text_width) / 2

					image_menu.paste(images_couleur[podium[i][j][1]], coords_2[i][j])
					draw.text((coords_2[i][j][0]+x,coords_2[i][j][1]+14.5), str(podium[i][0][0]), font=font, fill="black")



		
		image_menu = ImageTk.PhotoImage(image_menu)
  
  
	if len(prem_place)==1:
		gagnant="Bravo joueur "+liste_couleurs_fr[prem_place[0][1]]
	else:
		gagnant="Bravo joueurs"
		for i in range(len(prem_place)):
			if i == 0:
				gagnant+=" "+liste_couleurs_fr[prem_place[i][1]]

			elif i == len(prem_place)-1:
				gagnant+=" et "+liste_couleurs_fr[prem_place[i][1]]
			
			else :
				gagnant+=", "+liste_couleurs_fr[prem_place[i][1]]
	
  
	image_label =Label(cnv, image=image_menu)
	image_label.place(x=width_menu//4,y=height_menu//4)

	label_final = Label(final, text=gagnant, font=font_label)
	label_final.place(x=(width_menu/2-label_final.winfo_reqwidth()/2),y=(5*width_menu/100))
		
	def bouton_menu():
		
		final.destroy()
		charger_menu()
	
	def bouton_exit():
		final.destroy()


	
	button_menu = Button (final, text = "Menu",font=font_bouton, command=bouton_menu)
	button_menu.place(x=(width_menu/2 - button_menu.winfo_reqwidth()/2 - 10*width_menu/100),y=10+(80*height_menu/100))

	button_exit = Button (final, text = "Exit",font=font_bouton, command=bouton_exit)
	button_exit.place(x=(width_menu/2 - button_exit.winfo_reqwidth()/2 + 10*width_menu/100),y=10+(80*height_menu/100))

	final.mainloop()
	

#-----------------------PLATEAU
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
				
				f"1-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(30+unity, 30, 30+unity*2, 30+(1*unity), fill=coul_en, outline='', tags=f"rect1-{coul_fr[0:1]}")),
					f"1-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(30+unity*2, 30, 30+unity*3, 30+(1*unity), fill=coul_en, outline='', tags=f"rect1-{coul_fr[0:1]}")),
				
				f"2-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (2*30)+(1*unity), 10+unity, (2*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect2-{coul_fr[0:1]}")),
					f"2-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (2*30)+(1*unity), 10+unity*2, (2*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect2-{coul_fr[0:1]}")),
					f"2-2-0-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (2*30)+(1*unity), 10+unity*3, (2*30)+(1*unity)+unity, fill=coul_en, outline='', tags=f"rect2-{coul_fr[0:1]}")),
				
				f"3-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (3*30)+(2*unity), 10+unity, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
					f"3-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (3*30)+(2*unity), 10+unity*2, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
					f"3-2-0-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (3*30)+(2*unity), 10+unity*3, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
					f"3-3-0-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*3, (3*30)+(2*unity), 10+unity*4, (3*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect3-{coul_fr[0:1]}")),
	
				f"4-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (4*30)+(3*unity), 10+unity, (4*30)+(3*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
					f"4-0-1-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (4*30)+(4*unity), 10+unity, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
					f"4-1-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (4*30)+(4*unity), 10+unity*2, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect4-{coul_fr[0:1]}")),
				
				f"5-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(110, (4*30)+(3*unity), 110+unity, (4*30)+(3*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
					f"5-0-1-1-{coul_fr[0:1]}": (cnv2.create_rectangle(110, (4*30)+(4*unity), 110+unity, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
					f"5-1-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(110+unity, (4*30)+(4*unity), 110+unity*2, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
					f"5-2-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(110+unity*2, (4*30)+(4*unity), 110+unity*3, (4*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect5-{coul_fr[0:1]}")),
				
				f"6-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (5*30)+(5*unity), 10+unity, (5*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
					f"6-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (5*30)+(5*unity), 10+unity*2, (5*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
					f"6-2-0-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (5*30)+(5*unity), 10+unity*3, (5*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
					f"6-1-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (5*30)+(6*unity), 10+unity*2, (5*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect6-{coul_fr[0:1]}")),
	
				f"7-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(150, (5*30)+(5*unity), 150+unity, (5*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),
					f"7-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(150+unity, (5*30)+(5*unity), 150+unity*2, (5*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),
					f"7-0-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(150, (5*30)+(6*unity), 150+unity, (5*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),
					f"7-1-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(150+unity, (5*30)+(6*unity), 150+unity*2, (5*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect7-{coul_fr[0:1]}")),

				f"8-0-0-0-{coul_fr[0:1]}": (cnv2.create_rectangle(10, (7*30)+(6*unity), 10+unity, (7*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
					f"8-1-0-1-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (7*30)+(6*unity), 10+unity*2, (7*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
					f"8-1-1-2-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity, (7*30)+(7*unity), 10+unity*2, (7*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),
					f"8-2-1-3-{coul_fr[0:1]}": (cnv2.create_rectangle(10+unity*2, (7*30)+(7*unity), 10+unity*3, (7*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect8-{coul_fr[0:1]}")),

				f"9-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle(70+unity, (4*30)+(8*unity), 70+unity*2, (4*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
					f"9-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle(70+unity*2, (4*30)+(8*unity), 70+unity*3, (4*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
					f"9-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle(70+unity*2, (4*30)+(9*unity), 70+unity*3, (4*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
					f"9-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle(70+unity*3, (4*30)+(9*unity), 70+unity*4, (4*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),
					f"9-2-2-4-{coul_fr[0:1]}" : (cnv2.create_rectangle(70+unity*3, (4*30)+(10*unity), 70+unity*4, (4*30)+(10*unity)+unity, fill=coul_en, outline='', tags=f"rect9-{coul_fr[0:1]}")),

				f"10-1-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity, (8*30)+(8*unity), 10+unity*2, (8*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
					f"10-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle(10, (8*30)+(9*unity), 10+unity, (8*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
					f"10-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity, (8*30)+(9*unity), 10+unity*2, (8*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
					f"10-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity*2, (8*30)+(9*unity), 10+unity*3, (8*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),
					f"10-1-2-4-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity, (8*30)+(10*unity), 10+unity*2, (8*30)+(10*unity)+unity, fill=coul_en, outline='', tags=f"rect10-{coul_fr[0:1]}")),	
	
				f"11-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle(10, (10*30)+(10*unity), 10+unity, (10*30)+(10*unity)+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
					f"11-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle(10, (10*30)+(11*unity), 10+unity, (10*30)+(11*unity)+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
					f"11-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity, (10*30)+(11*unity), 10+unity*2, (10*30)+(11*unity)+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
					f"11-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity*2, (10*30)+(11*unity), 10+unity*3, (10*30)+(11*unity)+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
					f"11-1-2-4-{coul_fr[0:1]}" : (cnv2.create_rectangle(10+unity, (10*30)+(12*unity), 10+unity*2, (10*30)+(12*unity)+unity, fill=coul_en, outline='', tags=f"rect11-{coul_fr[0:1]}")),
	
				f"12-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, 30, (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, 30+unity,  fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
					f"12-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
					f"12-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
					f"12-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),
					f"12-3-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (1*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (1*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect12-{coul_fr[0:1]}")),

				f"13-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (3*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect13-{coul_fr[0:1]}")),
					f"13-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(1*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(1*unity)+unity,  fill=coul_en, outline='', tags=f"rect13-{coul_fr[0:1]}")),
					f"13-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity)+unity,  fill=coul_en, outline='', tags=f"rect13-{coul_fr[0:1]}")),
					f"13-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity)+unity,  fill=coul_en, outline='', tags=f"rect13-{coul_fr[0:1]}")),
					f"13-3-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (3*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (3*30)+(2*unity)+unity,  fill=coul_en, outline='', tags=f"rect13-{coul_fr[0:1]}")),

				f"14-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (5*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (5*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect14-{coul_fr[0:1]}")),
					f"14-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (5*30)+(2*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (5*30)+(2*unity)+unity, fill=coul_en, outline='', tags=f"rect14-{coul_fr[0:1]}")),
					f"14-0-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (5*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (5*30)+(3*unity), fill=coul_en, outline='', tags=f"rect14-{coul_fr[0:1]}")),
					f"14-1-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (5*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (5*30)+(3*unity), fill=coul_en, outline='', tags=f"rect14-{coul_fr[0:1]}")),
					f"14-2-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (5*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (5*30)+(3*unity), fill=coul_en, outline='', tags=f"rect14-{coul_fr[0:1]}")),

				f"15-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (7*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(3*unity)+unity, fill=coul_en, outline='', tags=f"rect15-{coul_fr[0:1]}")),
					f"15-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect15-{coul_fr[0:1]}")),
					f"15-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect15-{coul_fr[0:1]}")),
					f"15-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (7*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect15-{coul_fr[0:1]}")),
					f"15-2-0-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (7*30)+(3*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (7*30)+(3*unity)+unity, fill=coul_en, outline='', tags=f"rect15-{coul_fr[0:1]}")),

				f"16-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (9*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect16-{coul_fr[0:1]}")),
					f"16-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (9*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect16-{coul_fr[0:1]}")),
					f"16-2-0-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (9*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (9*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect16-{coul_fr[0:1]}")),
					f"16-3-0-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (9*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (9*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect16-{coul_fr[0:1]}")),
					f"16-4-0-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (9*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*6, (9*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect16-{coul_fr[0:1]}")),

				f"17-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (10*30)+(5*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (10*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect17-{coul_fr[0:1]}")),
					f"17-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (10*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (10*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect17-{coul_fr[0:1]}")),
					f"17-0-2-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (10*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (10*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect17-{coul_fr[0:1]}")),
					f"17-1-2-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (10*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (10*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect17-{coul_fr[0:1]}")),
					f"17-2-2-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (10*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (10*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect17-{coul_fr[0:1]}")),
	
				f"18-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+60+unity, (11*30)+(4*unity), (width_cnv2/2)+(taille_plateau*unity/2)+60+unity*2, (11*30)+(4*unity)+unity, fill=coul_en, outline='', tags=f"rect18-{coul_fr[0:1]}")),
					f"18-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+60+unity, (11*30)+(5*unity), (width_cnv2/2)+(taille_plateau*unity/2)+60+unity*2, (11*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect18-{coul_fr[0:1]}")),
					f"18-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+60+unity*2, (11*30)+(5*unity), (width_cnv2/2)+(taille_plateau*unity/2)+60+unity*3, (11*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect18-{coul_fr[0:1]}")),
					f"18-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+60+unity*3, (11*30)+(5*unity), (width_cnv2/2)+(taille_plateau*unity/2)+60+unity*4, (11*30)+(5*unity)+unity, fill=coul_en, outline='', tags=f"rect18-{coul_fr[0:1]}")),
					f"18-2-2-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+60+unity*3, (11*30)+(6*unity), (width_cnv2/2)+(taille_plateau*unity/2)+60+unity*4, (11*30)+(6*unity)+unity, fill=coul_en, outline='', tags=f"rect18-{coul_fr[0:1]}")),

				f"19-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (12*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (12*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect19-{coul_fr[0:1]}")),
					f"19-1-0-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (12*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (12*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect19-{coul_fr[0:1]}")),
					f"19-2-0-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (12*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (12*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect19-{coul_fr[0:1]}")),
					f"19-3-0-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (12*30)+(7*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*5, (12*30)+(7*unity)+unity, fill=coul_en, outline='', tags=f"rect19-{coul_fr[0:1]}")),
					f"19-2-1-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (12*30)+(8*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (12*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect19-{coul_fr[0:1]}")),

				f"20-0-0-0-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (13*30)+(8*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (13*30)+(8*unity)+unity, fill=coul_en, outline='', tags=f"rect20-{coul_fr[0:1]}")),
					f"20-0-1-1-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (13*30)+(9*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (13*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect20-{coul_fr[0:1]}")),
					f"20-1-1-2-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity, (13*30)+(10*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (13*30)+(10*unity)+unity, fill=coul_en, outline='', tags=f"rect20-{coul_fr[0:1]}")),
					f"20-2-1-3-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*2, (13*30)+(9*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (13*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect20-{coul_fr[0:1]}")),
					f"20-0-2-4-{coul_fr[0:1]}" : (cnv2.create_rectangle((width_cnv2/2)+(taille_plateau*unity/2)+unity*3, (13*30)+(9*unity), (width_cnv2/2)+(taille_plateau*unity/2)+unity*4, (13*30)+(9*unity)+unity, fill=coul_en, outline='', tags=f"rect20-{coul_fr[0:1]}")),

				
	
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
					if nom_rectangle_split[1] == "0" :
						coords_x_temp = coords_charge[0] 					
					coords_charge[0] = coords_x_temp
					coords_charge[2] = coords_x_temp+unity

					globals()[f"pieces_{coul_fr}_coords_base"].append(coords_charge)
					globals()[f"pieces_{coul_fr}_noms"].append(rect_name)
					globals()[f"pieces_{coul_fr}_utiles"].append([nom_rectangle_split[0],nom_rectangle_split[1],nom_rectangle_split[2],nom_rectangle_split[3]])
					flag_y_nom = nom_rectangle_split[2]
					flag_y = True
					flag_num_rect = nom_rectangle_split[0]
			
			loader.append(globals()[f"pieces_{coul_fr}_loader"])

			
		

	def build_plateau():

		
		for i in range(taille_plateau+1):
			cnv2.create_line(5+decalage_x,5+unity*i+decalage_y,(taille_plateau+0.1)*unity+decalage_x,5+unity*i+decalage_y)
			cnv2.create_line(5+unity*i+decalage_x,5+decalage_y,5+unity*i+decalage_x,(taille_plateau+0.1)*unity+decalage_y)


	def waithere():
		var = IntVar()
		root.after(100, var.set, 1)
		root.wait_variable(var)






			
			
	def clic(event):
		global c,rectangle,nom_rectangle,tag_rectangle,nom_rectangle_split,nom_rectangle_complet,derniere_piece_bleu_jouee,derniere_piece_rouge_jouee,joueur,nb_joueurs_out,bot

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
					
					for item in cnv2.find_withtag(tag_rectangle):
						cnv2.tag_raise(item)


					globals()[f"derniere_piece_{coul}_jouee"] = nom_rectangle

					c = (c+1)%2
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
				if (5+i*unity+decalage_x <= x<= 5+(i+1)*unity+decalage_x and 5+j*unity+decalage_y <= y <= 5+(j+1)*unity+decalage_y):


					flag_verif_boucle = True
					tagged_rectangles = []
					for item in cnv2.find_withtag(tag_rectangle):
						coordinates = cnv2.coords(item)
						tagged_rectangles.append(coordinates)
					
					i=(tagged_rectangles[int(nom_rectangle_split[3])][0])//unity-decalage_x//unity
					j=(tagged_rectangles[int(nom_rectangle_split[3])][1])//unity-decalage_y//unity



					total_code = 0
					for tag in tagged_rectangles:
						total_code += verif_alentours(int((tag[0]//unity)-decalage_x//unity),int((tag[1]//unity)-decalage_y//unity),joueur,plateau,nb_tours)
						
					if total_code <= 0:
						flag_verif_boucle = False
							

					if flag_verif_boucle:
						cnv2.move(tag_rectangle,5+i*unity-x1+decalage_x,5+j*unity-y1+decalage_y)
						for tag in tagged_rectangles:
							plateau[int((tag[1]//unity)-decalage_y//unity)][int((tag[0]//unity)-decalage_x//unity)] = joueur
						move = True
						

						flag_estSuppr = False
						compteur_estSuppr = 0

						if mute_son == 0 :
							player_son = pygame.mixer.music.load(son_placement_piece)
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


						
						cnv2.delete("soluce")
								
						flag_pose = 1
						

						
						nb_tours += 1

						
						verif_fin(plateau)

						
						
	

						while nb_tours%nb_joueurs+1 in liste_joueurs_out:
							nb_tours += 1

						for pieces_nom,pieces_num in loader[joueur-1].items():
							cnv2.itemconfigure(pieces_num,state="hidden")
						
						joueur = nb_tours%nb_joueurs+1
						if joueur not in liste_joueurs_out:
							for pieces_nom,pieces_num in loader[joueur-1].items():
								cnv2.itemconfigure(pieces_num,state="normal")

						if joueur in bot:
							bot_coup()

						
						joueur_en_tete()
						



		#-----------------JOUEUR-------
		# afficher_plateau_console()		
		if (move == False):			
			
			for i in range(len(globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"])):
				
				if nom_rectangle_split[0] == globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][0] and nom_rectangle_split[2] == globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][2]:
					num_index_rect = str(globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][3])
					y_index_rect = str(globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_utiles"][i][1]) 


			index_rect = globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_noms"].index(nom_rectangle_split[0]+"-"+y_index_rect+"-"+nom_rectangle_split[2]+"-"+num_index_rect+"-"+nom_rectangle_split[4])
			coord_base = globals()[f"pieces_{liste_couleurs_fr[joueur-1]}_coords_base"][index_rect]


			cnv2.move(tag_rectangle,coord_base[0]-x1+unity*int(nom_rectangle_split[1]),coord_base[1]-y1)

	def score(x):		
		score = []

		if x == 1:
			derniere_piece = []
			for i in range(nb_joueurs):
				score.append([0,i])
				derniere_piece.append(globals()[f"derniere_piece_{liste_couleurs_fr[i]}_jouee"])
		else:
			derniere_piece = []
			for i in range(nb_joueurs):
				score.append([0,i])
				derniere_piece.append(None)

		for i in range(len(loader)):
			if len(loader[i]) == 0:
				if derniere_piece[i] == "0":
					score[i][0] += 20
				else:
					score[i][0] += 15
			else:
				score[i][0] -= len(loader[i])



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
							if verif_alentours(int(poss[0]-tag[0]),int(poss[1]-tag[1]),joueur,plateau,nb_tours) == -1:
								total_code = -9999
						if total_code > 0:
							liste_coups_possibles.append([poss,rect_name,rect])


		return liste_coups_possibles


	def verif_fin(plateau):
		global nb_joueurs_out,nb_tours,liste_joueurs_out


		for i in range(1,nb_joueurs+1):
			if len(verif_pieces_possibilites(i,plateau)) == 0 or len(loader[i-1]) == 0:	
				if i not in liste_joueurs_out :
					liste_joueurs_out.append(i)
					nb_joueurs_out += 1

			
			if nb_joueurs_out == nb_joueurs:
				root.destroy()
				charger_final(score(1))

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

		x1,y1,x2,y2 = cnv2.coords(rectangle)

		
		cnv2.move(tag_rectangle,5+i*unity-x1+decalage_x,5+j*unity-y1+decalage_y)
				
		tagged_rectangles = []
		for item in cnv2.find_withtag(tag_rectangle):
			coordinates = cnv2.coords(item)
			tagged_rectangles.append(coordinates)

		for tag in tagged_rectangles:
			plateau[int((tag[1]//unity)-decalage_y//unity)][int((tag[0]//unity)-decalage_x//unity)] = joueur
			

		flag_estSuppr = False
		compteur_estSuppr = 0

				
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
		
		
						
		joueur_en_tete()

		
		#-----------------BOT-------
		# afficher_plateau_console()
		
	def joueur_en_tete():
		score_en_tete = score(0)
		score_en_tete.sort(reverse = True)
		print(score_en_tete)

		en_tete["text"]= f"Joueur {liste_couleurs_fr[score_en_tete[0][1]]} en tete !"
		en_tete["bg"]=liste_couleurs_en[score_en_tete[0][1]]


	def game_reload():
		global nb_tours,plateau,nb_joueurs_out,liste_joueurs_out,loader

		btn_reload.place_forget()
		cnv2.unbind("<Button-1>")
				
		for i in range(taille_plateau):
			(cnv2.create_rectangle(0*unity+decalage_x+5,i*unity+decalage_y+5,(taille_plateau-1)*unity+unity+decalage_x+5,i*unity+unity+decalage_y+5, fill='white', outline='black'))
				


			if mute_son == 0 and (i)%(taille_plateau//3) == 0:
				player_son = pygame.mixer.music.load(son_placement_piece)
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
		cnv2.bind("<Button-1>",clic)

		
			



		build_pieces()
		build_plateau()
		for couleurs in range(1,nb_joueurs):
			for pieces_nom,pieces_num in globals()[f"pieces_{liste_couleurs_fr[couleurs]}_loader"].items():
				cnv2.itemconfigure(pieces_num,state="hidden")
		
		loader = []
		for i in range(nb_joueurs):
			loader.append(globals()[f"pieces_{liste_couleurs_fr[i]}_loader"])
		

		
		
	

	def settings():
		charger_settings("plateau")
	
	def back():
		root.destroy()
		charger_menu()

	def voir_soluce(liste_coups_possibles):
		
		for i in liste_coups_possibles:
			(cnv2.create_rectangle(i[0][0]*unity+decalage_x+5,i[0][1]*unity+decalage_y+5,i[0][0]*unity+unity+decalage_x+5,i[0][1]*unity+unity+decalage_y+5, fill='black', outline='orange',tag="soluce"))



	root = Tk()
	
	root.resizable(width=False, height=False)


	root.title("BLO BLO BLO BLOKUS")
	if dev_mode == 0:
		root.iconbitmap("./images/logo.ico")
		
	
		Font(file="./fonts/OMORI-GAME.ttf", family="OMORI_GAME")	
		font_label = ('OMORI_GAME',20,'bold')
		font_bouton = ('OMORI_GAME',20)
	else:
		font_label= ('ARIAL',50)
		font_bouton = ("Comic Sans MS",30)

	cnv=Canvas(root,width=width_cnv, height=height_cnv,bg='brown')
	cnv2 = Canvas(cnv, width=width_cnv2, height=height_cnv2,bg='gray')

	cnv.pack()
	cnv2.place(x=(width_cnv/2)-width_cnv2/2, y=(height_cnv/2)-height_cnv2/2)
	root.lift(cnv2)



	en_tete= Label(root, text="Aucun joueur en tete", bg="white", fg="black", font=font_label, borderwidth=2, relief="solid")
	en_tete.place(x=(width_cnv/2-en_tete.winfo_reqwidth()/2),y=(90*height_cnv/100))

	btn_settings = Button(cnv,text="Settings",command = settings, font=font_bouton)
	btn_settings.place(x=(width_cnv/2-btn_settings.winfo_reqwidth()/2-25*width_cnv/100),y=(90*height_cnv/100))

	btn_retourmenu = Button(cnv,text="Menu",command = back, font=font_bouton)
	btn_retourmenu.place(x=(width_cnv/2-btn_retourmenu.winfo_reqwidth()/2-15*width_cnv/100),y=(90*height_cnv/100))

	btn_reload = Button(cnv,text="Restart",command = game_reload, font=font_bouton)
	btn_reload.place(x=(width_cnv/2-btn_reload.winfo_reqwidth()/2+15*width_cnv/100),y=(90*height_cnv/100))

	btn_settings = Button(cnv,text="Soluce",command = lambda: voir_soluce(verif_pieces_possibilites(joueur,plateau)), font=font_bouton)
	btn_settings.place(x=(width_cnv/2-btn_settings.winfo_reqwidth()/2+25*width_cnv/100),y=(90*height_cnv/100))


	cnv2.bind("<Button-1>",clic)

	build_pieces()
	build_plateau()

	


	for couleurs in range(1,nb_joueurs):
		for pieces_nom,pieces_num in globals()[f"pieces_{liste_couleurs_fr[couleurs]}_loader"].items():
			cnv2.itemconfigure(pieces_num,state="hidden")

	if 1 in bot:
		bot_coup()


	root.mainloop()