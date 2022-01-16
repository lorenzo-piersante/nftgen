from random import randint
from PIL import Image
from utilities.generate_mask_for_image import generate_mask_for_image
from config import *


def generate_art():
    x = 0
    while x < 4:
        background_id = randint(0, 2)
        background = Image.open(fp='assets/background/' + str(background_id) + '.png')
        new_image = background.resize(size=BACKGROUND_SIZE)

        cactus_id = randint(0, 2)
        cactus = Image.open(fp='assets/cactus/' + str(cactus_id) + '.png')
        resized_cactus = cactus.resize(size=CACTUS_SIZE)
        cactus_mask = generate_mask_for_image(resized_cactus)
        new_image.paste(im=resized_cactus, box=CACTUS_RIGHT_CORNER, mask=cactus_mask)

        first_attachment_id = randint(0, 2)
        first_attachment = Image.open(fp='assets/first_attachment/' + str(first_attachment_id) + '.png')
        resized_first_attachment = first_attachment.resize(size=FIRST_ATTACHMENT_SIZE)
        first_attachment_mask = generate_mask_for_image(resized_first_attachment)
        new_image.paste(im=resized_first_attachment, box=FIRST_ATTACHMENT_RIGHT_CORNER, mask=first_attachment_mask)

        second_attachment_id = randint(0, 2)
        second_attachment = Image.open(fp='assets/second_attachment/' + str(second_attachment_id) + '.png')
        resized_second_attachment = second_attachment.resize(size=SECOND_ATTACHMENT_SIZE)
        second_attachment_mask = generate_mask_for_image(resized_second_attachment)
        new_image.paste(im=resized_second_attachment, box=SECOND_ATTACHMENT_RIGHT_CORNER, mask=second_attachment_mask)

        new_image.save(fp='generated_nft_set/CryptoCactus#' + str(x) + '.png', format="PNG")
        x += 1


if __name__ == "__main__":
    generate_art()
    print("Art generated!")
