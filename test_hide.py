import tkinter as tk


root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Créer quelques rectangles avec le tag 'rect4' pour les besoins de l'exemple
rect = canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags="rect4")

canvas.itemconfigure(rect,state='hidden')

root.mainloop()
