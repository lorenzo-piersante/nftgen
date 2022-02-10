from PIL import Image


def generate_nft_image(new_image_id: int, combination: dict) -> None:
    new_image = Image.open(fp='assets/background/' + str(combination['background_id']) + '.png')
    _add_attachment(new_image, 'assets/body/', combination['body_id'])
    _add_attachment(new_image, 'assets/eyes/', combination['eyes_id'])
    _add_attachment(new_image, 'assets/hat/', combination['hat_id'])
    _add_attachment(new_image, 'assets/mouth/', combination['mouth_id'])
    _add_attachment(new_image, 'assets/accessory/', combination['accessory_id'])
    new_image.save(fp='generated_nft_set/images/' + str(new_image_id) + '.png', format="PNG")


def _add_attachment(original_image: Image, attachment_path: str, attachment_id: int) -> None:
    body = Image.open(fp=attachment_path + str(attachment_id) + '.png').convert('RGBA')
    original_image.paste(im=body, mask=body)
