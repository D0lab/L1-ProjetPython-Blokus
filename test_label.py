import tkinter as tk

def afficher_longueur():
    texte = label_texte.cget("text")  # Récupère le texte du label
    longueur = label_texte.winfo_reqwidth()  # Récupère la longueur du label en pixels
    print("Longueur du texte dans le label (en pixels) :", longueur)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exemple de Longueur de Label")

# Création du label avec un texte
texte_label = "Ceci est un exemple de texte dans un label"
label_texte = tk.Label(fenetre, text=texte_label)
label_texte.pack()

# Bouton pour afficher la longueur du texte
bouton_afficher_longueur = tk.Button(fenetre, text="Afficher longueur du texte", command=afficher_longueur)
bouton_afficher_longueur.pack()

# Lancement de la boucle principale
fenetre.mainloop()
