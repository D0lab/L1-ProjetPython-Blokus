import tkinter as tk


def onclick(event):
    global rectangles
    item = cv.find_closest(event.x, event.y)
    if item[0] in rectangles:
        current_color = cv.itemcget(item, 'fill')

        if current_color == 'black':
            cv.itemconfig(item, fill='white')
        else:
            cv.itemconfig(item, fill='black')

rectangles = []

root = tk.Tk()
cv = tk.Canvas(root, height=800, width=800)
cv.pack()
cv.bind('<Button-1>', onclick)

id_a = cv.create_rectangle(80, 80, 100, 100)
id_b = cv.create_rectangle(100, 100, 120, 120)
rectangles.append(id_a)
rectangles.append(id_b)

root.mainloop()
