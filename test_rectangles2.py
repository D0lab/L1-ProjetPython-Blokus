import tkinter as tk

def on_rectangle_click(event):
    for rect_name, rect in rectangles.items():
        if event.x >= rect[0] and event.x <= rect[2] and event.y >= rect[1] and event.y <= rect[3]:
            print("Rectangle cliqué :", rect_name)
            break

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Créez des rectangles avec des noms de variables associés
rectangles = {
    "rectangle1": (50, 50, 100, 100),  # Format : (x1, y1, x2, y2)
    "rectangle2": (120, 50, 170, 100),  # Format : (x1, y1, x2, y2)
    "rectangle3": (200, 50, 250, 100),  # Format : (x1, y1, x2, y2)
    "rectangle4": (270, 50, 320, 100),  # Format : (x1, y1, x2, y2)
    "rectangle5": (50, 120, 100, 170),  # Format : (x1, y1, x2, y2)
    "rectangle6": (120, 120, 170, 170),  # Format : (x1, y1, x2, y2)
    "rectangle7": (200, 120, 250, 170),  # Format : (x1, y1, x2, y2)
    "rectangle8": (270, 120, 320, 170),  # Format : (x1, y1, x2, y2)
    # Ajoutez plus de rectangles au besoin
}

# Dessinez les rectangles sur le canevas
for rect_name, rect_coords in rectangles.items():
    canvas.create_rectangle(*rect_coords, fill="gray", tags=rect_name)

# Associez la fonction de rappel à l'événement clic de la souris pour chaque rectangle
canvas.bind("<Button-1>", on_rectangle_click)

root.mainloop()
