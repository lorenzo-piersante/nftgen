from PIL import Image

from utilities.generate_json_data import generate_json_data
from utilities.generate_new_combination import generate_new_combination


def generate_nft_set() -> None:
    x = 1
    while x < 7:
        combination = generate_new_combination()

        new_image = Image.open(fp='assets/background/' + str(combination['background_id']) + '.png')
        _add_attachment(new_image, 'assets/body/', combination['body_id'])
        _add_attachment(new_image, 'assets/eyes/', combination['eyes_id'])
        _add_attachment(new_image, 'assets/hat/', combination['hat_id'])
        _add_attachment(new_image, 'assets/mouth/', combination['mouth_id'])
        new_image.save(fp='generated_nft_set/images/' + str(x) + '.png', format="PNG")

        generate_json_data(new_image_id=x, combination=combination)
        print('CryptoCactus#' + str(x) + ' generated!')
        x += 1


def _add_attachment(original_image: Image, attachment_path: str, attachment_id: int) -> None:
    body = Image.open(fp=attachment_path + str(attachment_id) + '.png').convert('RGBA')
    original_image.paste(im=body, mask=body)
