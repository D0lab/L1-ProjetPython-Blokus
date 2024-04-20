from tkinter import *


root = Tk()

root.resizable(width=False, height=False)


root.title("BLO BLO BLO BLOKUS TEST")


cnv=Canvas(root,width=width_cnv, height=height_cnv,bg='brown')
cnv2 = Canvas(cnv, width=width_cnv2, height=height_cnv2,bg='gray')

cnv.pack()
cnv2.place(x=(width_cnv/2)-width_cnv2/2, y=(height_cnv/2)-height_cnv2/2)
root.lift(cnv2)





cnv2.bind("<Button-1>",clic)



root.mainloop()

test_dico = {
"3-0-0-0-test": (cnv2.create_rectangle(10, (4*30)+(3*unity), 10+unity, (4*30)+(3*unity)+unity, fill=blue, outline='', tags="rect3-test")),
"3-0-1-1-test": (cnv2.create_rectangle(10, (4*30)+(4*unity), 10+unity, (4*30)+(4*unity)+unity, fill=blue, outline='', tags="rect3-test")),
"3-1-1-2-test": (cnv2.create_rectangle(10+unity, (4*30)+(4*unity), 10+unity*2, (4*30)+(4*unity)+unity, fill=blue, outline='', tags="rect3-test"))
}