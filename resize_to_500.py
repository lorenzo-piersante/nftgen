from PIL import Image

bg = Image.open(fp='assets/mouth/0.png')
resized = bg.resize(size=(500, 500))
resized.save(fp='assets/mouth/0.png', format="PNG")

bg = Image.open(fp='assets/mouth/1.png')
resized = bg.resize(size=(500, 500))
resized.save(fp='assets/mouth/1.png', format="PNG")

# bg = Image.open(fp='assets/hat/2.png')
# resized = bg.resize(size=(500, 500))
# resized.save(fp='assets/hat/2.png', format="PNG")
