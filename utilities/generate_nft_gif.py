from PIL import Image


def generate_nft_gif(new_image_id: int, combination: dict) -> None:
    background = Image.open(fp='assets/background/' + str(combination['background_id']) + '.gif')
    body = Image.open(fp='assets/body/' + str(combination['body_id']) + '.png').convert('RGBA')
    eyes = Image.open(fp='assets/eyes/' + str(combination['eyes_id']) + '.png').convert('RGBA')
    hat = Image.open(fp='assets/hat/' + str(combination['hat_id']) + '.png').convert('RGBA')
    mouth = Image.open(fp='assets/mouth/' + str(combination['mouth_id']) + '.png').convert('RGBA')

    frames = []
    for frame in range(background.n_frames):
        new_gif = Image.new('RGBA', (500, 500), (0, 0, 0, 0))
        background.seek(frame=frame)
        new_gif.paste(im=background, box=(0, 0))
        new_gif.paste(im=body, box=(0, 0), mask=body)
        new_gif.paste(im=eyes, box=(0, 0), mask=eyes)
        new_gif.paste(im=hat, box=(0, 0), mask=hat)
        new_gif.paste(im=mouth, box=(0, 0), mask=mouth)
        frames.append(new_gif)

    frames[0].save(
        fp='generated_nft_set/animated_images/' + str(new_image_id) + '.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=85,
        loop=0
    )
