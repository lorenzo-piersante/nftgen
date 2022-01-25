from config import number_of_nfts, animated_backgrounds
from utilities.generate_json_data import generate_json_data
from utilities.generate_new_combination import generate_new_combination
from utilities.generate_nft_gif import generate_nft_gif
from utilities.generate_nft_image import generate_nft_image


def generate_nft_set() -> None:
    new_image_id = 1
    while new_image_id < number_of_nfts + 1:
        combination = generate_new_combination()

        if combination['background_id'] in animated_backgrounds:
            generate_nft_gif(new_image_id=new_image_id, combination=combination)
            generate_json_data(new_image_id=new_image_id, combination=combination)
            print('CryptoCactus#' + str(new_image_id) + ' generated! [animated]')
            new_image_id += 1
            continue

        generate_nft_image(new_image_id=new_image_id, combination=combination)
        generate_json_data(new_image_id=new_image_id, combination=combination)
        print('CryptoCactus#' + str(new_image_id) + ' generated!')
        new_image_id += 1
