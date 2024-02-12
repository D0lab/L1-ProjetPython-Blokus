from tkinter import *
#from tkinter.font import Font
from tkextrafont import Font

width = 1280
height = 720

def gcd1(x, y):
    if y == 0:
        return x
    else:
        return gcd1(y, x % y)
    
pgcd = gcd1(width,height)
aspect_ratio_width = width/pgcd
aspect_ratio_height = height/pgcd


menu = Tk()
menu.title('MENU BLOKUS')
menu.geometry(str(width)+"x"+str(height))
label = Label(menu, text='BLO BLO BLO BLOKUS', font=('Arial 50'))
label.place(x=(20*width/100),y=10)




button1 = Button ( menu, text = "salut")
button1['text'] = "caca"
button1['font'] = Font(family="Comic Sans MS")
button1.place(x=10+(25*width/100),y=10+(80*height/100))


button2 = Button ( menu, text = "toiiii")
button2.place(x=10+(50*width/100),y=10+(80*height/100))

font = Font(file="./fonts/OMORI_GAME.ttf", family="OMORI_GAME")
Label(menu, text="Hello", font=font).pack()

menu.mainloop()





