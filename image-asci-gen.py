from re import ASCII
from PIL import Image

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^\'. "

with Image.open('./images/Darth-Vader-Tatler-7feb14_alamy_b.jpg.webp').convert('L') as im:
    width, height = im.size
    ratio = height / width
    new_width = 256
    new_height = int(new_width * ratio)
    im = im.resize((new_width, new_height))
    pixels = list(im.getdata())
    data = [pixels[offset:offset+new_width] for offset in range(0, new_width*new_height, new_width)]
    with open('./converted/test.txt', 'w') as newImg:
        for row in data:
            for val in row:
                newImg.write(' ' + ASCII_CHARS[val %len(ASCII_CHARS)] + ' ')
            newImg.write('\n')



