from random import randint
from PIL import Image
from utilities.generate_mask_for_image import generate_mask_for_image


def generate_art():
    x = 0
    while x < 6:
        background_id = randint(0, 2)
        new_image = Image.open(fp='assets/background/' + str(background_id) + '.png')

        cactus_id = 0
        cactus = Image.open(fp='assets/cactus/' + str(cactus_id) + '.png')
        cactus_mask = generate_mask_for_image(cactus)
        new_image.paste(im=cactus, box=(0, 0), mask=cactus_mask)

        first_attachment_id = randint(0, 1)
        first_attachment = Image.open(fp='assets/first_attachment/' + str(first_attachment_id) + '.png')
        first_attachment_mask = generate_mask_for_image(first_attachment)
        new_image.paste(im=first_attachment, box=(0, 0), mask=first_attachment_mask)

        second_attachment_id = randint(0, 1)
        second_attachment = Image.open(fp='assets/second_attachment/' + str(second_attachment_id) + '.png')
        second_attachment_mask = generate_mask_for_image(second_attachment)
        new_image.paste(im=second_attachment, box=(0, 0), mask=second_attachment_mask)

        third_attachment_id = randint(0, 1)
        third_attachment = Image.open(fp='assets/third_attachment/' + str(third_attachment_id) + '.png')
        third_attachment_mask = generate_mask_for_image(third_attachment)
        new_image.paste(im=third_attachment, box=(0, 0), mask=third_attachment_mask)

        new_image.save(fp='generated_nft_set/CryptoCactus#' + str(x) + '.png', format="PNG")
        x += 1


if __name__ == "__main__":
    generate_art()
    print("Art generated!")
