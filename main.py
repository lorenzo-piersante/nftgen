from PIL import Image


def generate_art():
    base_image = Image.open(fp='images_to_compose/base.png')
    resized_base_image = base_image.resize(size=(256, 256))

    attachment_image = Image.open(fp='images_to_compose/attachment.png')
    resized_attachment_image = attachment_image.resize(size=(64, 64))

    mask = resized_attachment_image.convert('L').point(lambda x: 0 if x > 128 else 255, '1')

    resized_base_image.paste(im=resized_attachment_image, box=(92, 104), mask=mask)
    resized_base_image.save(fp="generated_nft_set/test_image.png", format="PNG")

    print("Art generated!")


if __name__ == "__main__":
    generate_art()
