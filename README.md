**PROJET PYTHON**  
**RENDU FINAL : Lundi 8 avril 2024**  
**LABASTE Dorian & LAURENT Matys**    

Pour voir d'anciennes versions, voici le lien de notre GitHub :  
**https://github.com/D0lab/L1-ProjetPython-Blokus**    

**ATTENTION :**    

Si vous avez des problèmes avec les sons :  
- datas.py : initialiser la variable mute_son à 1 *(ligne 23)*    
  
Si vous avez des problèmes avec les images :   
- datas.py : initialiser la variable dev_mode à 1 *(ligne 22)*   


Les images utilisées dans le projet se trouvent à l'emplacement suivant : "./images/"  
Les sons utilisés dans le projet se trouvent à l'emplacement suivant : "./sons/"  
Les polices de caractères utilisées dans le projet se trouvent à l'emplacement suivant : "./fonts/"   


Voici la liste détaillée de ce que nous avons fait au fil des différents rendus :  

**Rendu 1 :**  
- Groupes constitués : Dorian & Matys  
- Affichage de la grille et des pièces sur le tableau *(pièces plus complexes en cours)*  
- Déplacement de la première pièce/repositionnement à sa place initiale si clic en dehors de la grille    

**Rendu 2 :**  
- Déplacement de toutes les pièces sur la grille/repositionnement automatique à la place initiale si clic en dehors de la grille  
- Attention au placement sur la grille au plus près du clic    

**Rendu 3 :**  
- On vérifie que les pièces sont correctement positionnées par rapport aux règles de placement    

**Rendu 4 :**  
- On peut recommencer    
- On gère la fin du jeu  
- On peut jouer contre la machine  

**BONUS :**  
- Menu  
    - Son de démarrage  
    - Logo  
    - Nom du jeu  
    - Bouton "Jouer"  
    - Bouton "Jouer" fonctionnel 
    - Bouton "Paramètres"  
    - Bouton "Paramètres" fonctionnel  
    - Bouton "Crédits"  
    - Bouton "Crédits" fonctionnel  
    - Police d'écriture provenant du jeu "Omori"  
    - Sélection nombre de joueurs  
- Plateau  
    - Sons : pièces posées et recommencer  
    - Pièces améliorées  
    - Nom du joueur en tête  
- Paramètres  
    - Slider volume son 
    - Sélection de résolution de fenêtre  
- Ecran de fin  
    - Podium 
- Conversion du fichier plateau.py en modèle MVC :
    - controller.py  
    - ihm.py  
    - datas.py    
