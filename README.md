# nftgen

### Introduction:

nftgen is a simple project made to improve my python programming skills and help a friend with an NFT project.

The aim of the script is to generate NFT art combining images with weighted chances 

A JSON file is created for every image generated this way.
The JSON file can be used to bulk upload images on Opensea using **infotrex/bulk-upload-to-opensea** script

### Install language and dependencies:

1. Install python 3
2. Install pipenv
3. run `pipenv install`

### Add assets:

1. Put backgrounds in **_asset/background_** folder numbered from 0
2. Put bodies in _**asset/body**_ folder numbered from 0 
and so on (replacing examples)...

### Configuration:

The script can be configured editing variables values in `config.py` file:
- `number_of_nfts` is the number of images you want to generate (commonly 10000)
- `background_population` (numbers assigned to background images, using (0, 1, 2, ..., 10000) might be good idea)
- `background_weights` (percentage chance of every image, total must be 100 for example (15, 35, 50))
- `background_values` (names of every component, used to create the bulk upload JSON)
and so on ...

(GIF components are also supported, but I'm too lazy to explain how to configure it, try to figure it yourself if needed!)

### Run script:

Run `pipenv run python main.py`

All files will be generated under **_generated_nft_set_** directory

### Notes:

1. Bodies, eyes, ... must be renders with exact same dimension of backgrounds (check examples)
2. If you want to add a different number of items to your image, attach items with different names, use images with 
different sizes or format it is really simple to edit project files to do so with some super-basic python knowledge, 

If you still have any doubt feel free to ask!
