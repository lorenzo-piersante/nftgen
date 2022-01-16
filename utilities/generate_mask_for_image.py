from PIL import Image


def generate_mask_for_image(image: Image):
    image = image.convert("RGBA")
    data = image.getdata()

    new_image = []
    for pixel in data:
        # pixel is represented from a tuple (r, g, b, a)
        if pixel[3] == 0:
            new_image.append((0, 0, 0))
            continue
        new_image.append((255, 255, 255))

    image.putdata(new_image)
    return image.convert("L")
