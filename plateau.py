# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:35:45 2022

@author: fpouit
Déplacement d'un objet dans un Canvas 2
"""

from tkinter import Tk, Canvas


def clic(event):
    global c
    c = (c+1)%2
    if ( c == 1):
        cnv.bind("<Motion>",glisser)
        old[0]=event.x
        old[1]=event.y
    else:
        cnv.unbind("<Motion>")
        deposer(event.x,event.y)

def glisser(event):
    x1, y1, x2, y2 = cnv.coords(rect)
    if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
        cnv.move(rect, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y
        
def deposer(x,y):
    x1, y1, x2, y2 = cnv.coords(rect)
    move = False
    for i in range(12):
        for j in range(12):
            if (5+i*unity <= x<= 5+(i+1)*unity and 5+j*unity <= y <= 5+(j+1)*unity):
                cnv.move(rect,5+i*unity-x1,5+j*unity-y1)
                #print("----EMPLACEMENT CASE----",5+i*unity,5+j*unity)
                move = True
    if (move == False):
        cnv.move(rect,13.05*unity-x1,30-y1)



# pgm principal

old=[None, None]

global c
c = 0
root = Tk()
cnv = Canvas(root, width=1280, height=960)
unity = 70
cnv.pack()

pieces_bleu = []
pieces_rouge = []

rect = cnv.create_rectangle(13.05*unity, 30, 13.05*unity+unity, 30+unity, fill='red', outline='')
for i in range(13):
    cnv.create_line(5,5+unity*i,12.05*unity,5+unity*i)
    cnv.create_line(5+unity*i,5,5+unity*i,12.05*unity)


cnv.bind("<Button-1>",clic)

root.mainloop()
