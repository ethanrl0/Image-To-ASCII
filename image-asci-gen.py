from PIL import Image
import os 

# Select ASCII characters ordered by descending intensity (somewhat arbitrary)
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`\'. "

# Iterate over the images directory
for filename in os.listdir('./images'):
    f = os.path.join('./images', filename) # Get relative image path of file
    with Image.open(f).convert('L') as im:
        # Compute image ratio
        width, height = im.size
        ratio = height / width
        new_width = width # Substitute with smaller value for smaller resulting image
        new_height = int(new_width * ratio)
        im = im.resize((new_width, new_height))
        pixels = list(im.getdata())
        # Structure into rows of pixels
        data = [pixels[offset:offset+new_width] for offset in range(0, new_width*new_height, new_width)]
        # New file path and name
        base = os.path.basename(f)
        new_f = os.path.splitext(base)[0] + '_new' + '.txt'
        new_file = './converted/' + new_f
        with open(new_file, 'w') as newImg:
            for row in data:
                for val in row:
                    # Write an ASCII character according to the intensity of the given pixel
                    newImg.write(' ' + ASCII_CHARS[val %len(ASCII_CHARS)])
                newImg.write('\n')



