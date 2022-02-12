# an example for a script you can use to resize images to the same dimension
#
# from PIL import Image
#
# i = 0
# while i <= 10:
#     new_image = Image.open(fp='assets/background/' + str(i) + '.png').convert('RGBA')
#     resized = new_image.resize((500, 500))
#     resized.save(fp='assets/background/' + str(i) + '.png', format="PNG")
#     i += 1
