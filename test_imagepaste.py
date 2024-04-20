from PIL import Image, ImageDraw, ImageFont

# Charger l'image
image = Image.open("bleu.png")

# Initialiser le module ImageDraw
draw = ImageDraw.Draw(image)

# Charger une police
font = ImageFont.truetype("arial.ttf", size=24)

# Texte à mesurer
text = "Hello World!"

# Obtenir la taille du texte
text_size = draw.textlength(text, font=font)

print("Taille du texte:", text_size)
