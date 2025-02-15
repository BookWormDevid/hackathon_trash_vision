import cv2
import math


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
    image_path = "data/Possible_trash_on_platforms/platform-2.jpg"
    num_parts = int(input("Enter the number of parts to segment the image into: "))

    segmented_images = divide_image(image_path, num_parts)

    # Display the segmented images
    for i, segment in enumerate(segmented_images):
        cv2.imshow(f'Segment {i+1}', segment)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
