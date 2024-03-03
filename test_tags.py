import tkinter as tk

def print_rectangles_with_tag():
    tagged_rectangles = []
    for item in canvas.find_withtag("rect4"):
        coordinates = canvas.coords(item)
        tagged_rectangles.append(coordinates)
    print("Rectangles avec le tag 'rect4' :", tagged_rectangles)

root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Créer quelques rectangles avec le tag 'rect4' pour les besoins de l'exemple
canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags="rect4")
canvas.create_rectangle(150, 150, 200, 200, fill="red", tags="rect4")
canvas.create_rectangle(250, 250, 300, 300, fill="green", tags="rect4")

# Appel de la fonction pour imprimer les rectangles avec le tag 'rect4'
print_rectangles_with_tag()

root.mainloop()
