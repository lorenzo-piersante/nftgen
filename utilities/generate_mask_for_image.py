from PIL import Image


def generate_mask_for_image(image: Image):
    image = image.convert("RGB")
    data = image.getdata()

    new_image = []
    for item in data:
        if item == (255, 255, 255):
            new_image.append((0, 0, 0))
            continue
        new_image.append((255, 255, 255))

    image.putdata(new_image)
    return image.convert("L")
