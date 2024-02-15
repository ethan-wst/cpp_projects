import sys
from PIL import Image, ImageOps
import math

def crop_input_image(im):
    cropped_im = ImageOps.fit(im, (320,240), centering = (0.5, 0.5))
    cropped_im.save("cropped-ascii-image.jpeg")
    return cropped_im

def get_pixel_matrix(im):
    pixels = list(im.getdata())
    return [pixels[i:i+im.width] for i in range(0, len(pixels), im.width)]

def get_brightness(pixel_matrix):
    brightness_matrix = []
    for rows in pixel_matrix:
        brightness_row = []
        for x in rows:
            R = x[0]
            G = x[1]
            B = x[2]
            brightness = round((R+B+G)/3)
            brightness_row.append(brightness)
        brightness_matrix.append(brightness_row)
    return brightness_matrix

def get_ascii_matrix(brightness_matrix, ascii_string):
    ascii_matrix = []
    ascii_num = math.ceil(255/len(ascii_string))
    for row in brightness_matrix:
        ascii_row = []
        for y in row:
            ascii_char = ascii_string[math.ceil(y/ascii_num)]
            ascii_row.append(ascii_char)
        ascii_matrix.append(ascii_row)
    return ascii_matrix

def print_ascii_art(ascii_matrix):
    file = open("ascii_art.txt", 'a')
    for row in ascii_matrix:
        for x in row:
            file.write(x)
            file.write(x)
        file.write("\n")


ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
im = Image.open(sys.argv[1])
if im.height != 480 and im.width != 640:
    im = crop_input_image(im)

pixel_matrix = get_pixel_matrix(im)
brightness_matrix = get_brightness(pixel_matrix)
ascii_matrix = get_ascii_matrix(brightness_matrix, ascii_string)
print_ascii_art(ascii_matrix)
