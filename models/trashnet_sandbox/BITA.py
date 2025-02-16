# Big Image Tiling and Analysis

import os
import image_eval
import image_tiling


def bita(big_image_path, t_num):
    image_tiling.big_image(big_image_path, t_num)  # tiles by 64 by default
    save_path = 'data/Segmented_BITA/'
    tiles_info = []
    i = 0
    for _ in enumerate(os.listdir('data/Segmented_BITA')):
        filename = 'Image_' + f'Segment_{i + 1}' + '.jpg'
        complete_path = os.path.join(save_path, filename)
        tile_info = image_eval.choose_and_predict(complete_path)
        tiles_info.append(tile_info)
        print(i)
        if tile_info[0] != 'cardboard':
            print(str(tile_info[0]) + " at" + str(tile_info[1]) + "%")
        i += 1

    return tiles_info


tiles = 64
pred = bita('data/Possible_trash_on_platforms/platform_16.jpg', tiles)

