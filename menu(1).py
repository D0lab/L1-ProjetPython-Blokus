from tkinter import *

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
label.pack(side=TOP, expand=True)

f = font.Font(size=35)

button1 = Button ( menu, text = "salut", font=(size=35))
button1.pack(side=LEFT)
button1['font'] = f

button2 = Button ( menu, text = "toiiii")
button2.pack(side=LEFT)


menu.mainloop()