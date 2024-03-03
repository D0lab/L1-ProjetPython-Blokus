import tkinter as tk

# Fonction appelée lorsqu'un clic gauche est effectué sur le rectangle
def on_press(event):
    global is_pressed, start_x, start_y
    is_pressed = True
    start_x = event.x
    start_y = event.y
    # Assurez-vous que le rectangle est au-dessus des autres éléments
    canvas1.tag_raise(rectangle)

# Fonction appelée lors du déplacement de la souris tout en maintenant le clic gauche enfoncé
def on_drag(event):
    global is_pressed
    if is_pressed:
        x = canvas1.canvasx(event.x)
        y = canvas1.canvasy(event.y)
        canvas1.coords(rectangle, x, y, x + (canvas1.coords(rectangle)[2] - canvas1.coords(rectangle)[0]), y + (canvas1.coords(rectangle)[3] - canvas1.coords(rectangle)[1]))

# Fonction appelée lorsqu'un clic gauche est relâché
def on_release(event):
    global is_pressed
    is_pressed = False
    # Vérifie si le rectangle est dans le canvas 1 ou le canvas 2
    if event.widget == canvas1:
        canvas = canvas1
    elif event.widget == canvas2:
        canvas = canvas2
    # Sinon, le ramène au canvas d'origine
    else:
        canvas = original_canvas
    start_x = 0
    start_y = 0

# Crée la fenêtre principale
root = tk.Tk()
root.title("Rectangle Draggable")

# Crée deux widgets canvas
canvas1 = tk.Canvas(root, width=200, height=200, bg='white')
canvas1.pack(side=tk.LEFT, padx=5, pady=5)

canvas2 = tk.Canvas(root, width=200, height=200, bg='lightgray')
canvas2.pack(side=tk.LEFT, padx=5, pady=5)

# Crée un rectangle dans le canvas 1
rectangle = canvas1.create_rectangle(50, 50, 100, 100, fill='blue', tags="draggable")

# Variables globales pour le suivi de l'état du clic de la souris
is_pressed = False
start_x = 0
start_y = 0

# Lie les événements de la souris aux fonctions correspondantes
canvas1.tag_bind(rectangle, "<ButtonPress-1>", on_press)
canvas1.tag_bind(rectangle, "<B1-Motion>", on_drag)
canvas1.tag_bind(rectangle, "<ButtonRelease-1>", on_release)

# Exécute la boucle principale
root.mainloop()
