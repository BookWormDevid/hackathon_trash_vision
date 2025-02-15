import cv2
import math
import matplotlib.pyplot as plt
import os.path

def divide_image(image_path, num_parts):
    # Read the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Calculate the number of parts per dimension
    parts_per_dimension = int(math.sqrt(num_parts))
    while num_parts % parts_per_dimension != 0:
        parts_per_dimension -= 1

    # Calculate the dimensions of each part
    part_height = height // parts_per_dimension
    part_width = width // (num_parts // parts_per_dimension)

    # Divide the image into parts
    parts = []
    for i in range(parts_per_dimension):
        for j in range(num_parts // parts_per_dimension):
            part = image[i * part_height: (i + 1) * part_height, j * part_width: (j + 1) * part_width]
            parts.append(part)

    return parts


def main():
    folder_path = "data/Possible_trash_on_platforms/"
    num_parts = int(input("Enter the number of parts to segment the images into: "))

    for i in range(1, 108):
        ind_img_path = 'platform_' + str(i)
        image_path = folder_path + ind_img_path
        segmented_images = divide_image(image_path, num_parts)
        for j, segment in enumerate(segmented_images):
            save_path = 'Trash_on_plat_segmented'
            filename = 'ind_img_path' + f'Segment {j+1}'
            completeName = os.path.join(save_path, filename + ".jpg")
            filewriter = open(completeName, "w")

    cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
