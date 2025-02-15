# Big Image Tiling and Analysis

import os
import image_eval
import image_tiling


def bita(big_image_path):
    image_tiling.big_image(big_image_path)  # tiles by 256 by default
    save_path = 'data/Segmented_BITA/'
    tiles_info = []
    i = 0
    for _ in enumerate(os.listdir('data/Segmented_BITA')):
        filename = 'Image_' + f'Segment_{i + 1}' + '.jpg'
        complete_path = os.path.join(save_path, filename)
        tile_info = image_eval.choose_and_predict(complete_path)
        tiles_info.append(tile_info)
        print(i)
        i += 1

    return tiles_info


pred = bita('data/Possible_trash_on_platforms/platform_10.jpg')

print(pred)
