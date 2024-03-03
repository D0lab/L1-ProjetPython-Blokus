import tkinter as tk

def on_drag_start(event):
    global prev_x, prev_y
    prev_x = event.x
    prev_y = event.y

def on_drag_motion(event):
    global prev_x, prev_y
    new_x = event.x
    new_y = event.y
    canvas.move("L", new_x - prev_x, new_y - prev_y)
    prev_x = new_x
    prev_y = new_y

# Création de la fenêtre principale
root = tk.Tk()
root.title("Dessiner un L avec Tkinter")

# Création d'un canevas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Dessiner les rectangles pour former le "L"
rect1 = canvas.create_rectangle(50, 50, 100, 150, fill="blue", tags="L")  # Rectangle vertical
rect2 = canvas.create_rectangle(100, 100, 150, 150, fill="blue", tags="L") # Rectangle horizontal

# Activation du glisser-déposer
canvas.bind("<ButtonPress-1>", on_drag_start)
canvas.bind("<B1-Motion>", on_drag_motion)

# Lancement de la boucle principale
root.mainloop()
