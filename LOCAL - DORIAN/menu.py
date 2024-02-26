from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import pyglet
import pyglet.media as media
#from tkextrafont import Font

import time

dev_mode = 0
mute_son = 0
width = 1280
height = 720
#font_omori = "./fonts/OMORI_GAME.ttf"
#font_omori = "Comic Sans MS"

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
if dev_mode == 0:
    menu.iconbitmap("images/logo.ico")
menu.geometry(str(width)+"x"+str(height))
label = Label(menu, text='BLO BLO BLO BLOKUS', font=('Arial 50'))
label.place(x=(20*width/100),y=10)

if dev_mode == 0 or mute_son == 0:
    player = pyglet.media.load("sons/blokus.wav")
    player.play()


if dev_mode == 0:
    # Load and display an image 
    #(replace 'your_logo.png' with the path to your image file)

    image = Image.open('./images/logo.png')

    image = image.resize((400,400))

    image = ImageTk.PhotoImage(image)

# Create a label to display the image
    image_label =Label(menu, image=image)
    image_label.place(x=(width/2-200),y=(height/2-200))


button1 = Button ( menu, text = "Play",font=("Comic Sans MS",30))
button1.place(x=10+(25*width/100),y=10+(80*height/100))

button2 = Button ( menu, text = "Settings",font=("Comic Sans MS",30))
button2.place(x=10+(40*width/100),y=10+(80*height/100))

button3 = Button ( menu, text = "Credits",font=("Comic Sans MS",30))
button3.place(x=10+(60*width/100),y=10+(80*height/100))

#font = Font(file="./fonts/OMORI_GAME.ttf", family="OMORI_GAME")
#Label(menu, text="Hello", font=font).pack()

menu.mainloop()