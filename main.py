from time import time
from utilities.generate_nft_set import generate_nft_set


start = time()
generate_nft_set()
end = time()
print('Done! It took ' + str(end - start) + ' seconds to finish')
