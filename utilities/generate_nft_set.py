from config import number_of_nfts
from utilities.generate_json_data import generate_json_data
from utilities.generate_new_combination import generate_new_combination
from utilities.generate_nft_image import generate_nft_image


def generate_nft_set() -> None:
    x = 1
    while x < number_of_nfts + 1:
        combination = generate_new_combination()
        generate_nft_image(new_image_id=x, combination=combination)
        generate_json_data(new_image_id=x, combination=combination)
        print('CryptoCactus#' + str(x) + ' generated!')
        x += 1
