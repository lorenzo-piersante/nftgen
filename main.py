from random import randint
from PIL import Image
from time import time

from utilities.generate_json_data import generate_json_data
from utilities.generate_new_combination import generate_new_combination


def main():
    x = 1
    while x < 7:
        combination = generate_new_combination()

        new_image = Image.open(fp='assets/background/' + str(combination['background_id']) + '.png')

        body = Image.open(fp='assets/body/' + str(combination['body_id']) + '.png').convert('RGBA')
        new_image.paste(im=body, mask=body)

        eyes = Image.open(fp='assets/eyes/' + str(combination['eyes_id']) + '.png').convert('RGBA')
        new_image.paste(im=eyes, mask=eyes)

        hat = Image.open(fp='assets/hat/' + str(combination['hat_id']) + '.png').convert('RGBA')
        new_image.paste(im=hat, mask=hat)

        mouth = Image.open(fp='assets/mouth/' + str(combination['mouth_id']) + '.png').convert('RGBA')
        new_image.paste(im=mouth, mask=mouth)

        new_image.save(fp='generated_nft_set/images/' + str(x) + '.png', format="PNG")

        generate_json_data(new_image_id=x, combination=combination)
        print('CryptoCactus#' + str(x) + ' generated!')
        x += 1


start = time()
main()
end = time()
print('Done! It took ' + str(end - start) + ' seconds to finish')
