# an example for a script you can use to resize images to the same dimension
#
# from PIL import Image
#
# i = 3
# while i <= 10:
#     new_image = Image.open(fp='assets/background/' + str(i) + '.png').convert('RGBA')
#     resized = new_image.resize((500, 500))
#     resized.save(fp='assets/background/' + str(i) + '.png', format="PNG")
#     i += 1
#
# i = 0
# new_image = Image.open(fp='assets/body/' + str(i) + '.png').convert('RGBA')
# resized = new_image.resize((500, 500))
# resized.save(fp='assets/body/' + str(i) + '.png', format="PNG")
