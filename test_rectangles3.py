
from tkinter import Tk, Canvas

def clic(event):
	global c,rectangle
	
	for rect_name, rect in pieces_rouge_loader.items():
		coords = cnv.coords(rect)
		print(coords)
		if event.x >= coords[0] and event.x <= coords[2] and event.y >= coords[1] and event.y <= coords[3]:
			rectangle = rect
	
	
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
		
		
def deposer(x,y):
	global taille_plateau, nb_tours, rectangle
	
	x1, y1, x2, y2 = cnv.coords(rectangle)
	
	move = False
	for i in range(taille_plateau):
		for j in range(taille_plateau):
			if (5+i*unity <= x<= 5+(i+1)*unity and 5+j*unity <= y <= 5+(j+1)*unity):
				print("----EMPLACEMENT CASE----",i,j)
				cnv.move(rectangle,5+i*unity-x1,5+j*unity-y1)
				plateau[j][i] = 1
				nb_tours += 1
				afficher_plateau_console()
					
					
				move = True
	if (move == False):
		cnv.move(rect,(taille_plateau+1.05)*unity-x1,30-y1)


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

pieces_rouge_loader = {
	"0": (cnv.create_rectangle((taille_plateau+1.05)*unity, 30, (taille_plateau+1.05)*unity+unity, 30+unity, fill='red', outline=''))
	}
	

cnv.bind("<Button-1>",clic)

root.mainloop()
