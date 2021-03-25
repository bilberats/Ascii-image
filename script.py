import PIL.Image,PIL.ImageOps  

#ascii chars
ASCII_CHARS = "@%#*+=-:. "

#resize
def resize_image(image,new_width):
    width, height = image.size
    ratio = height / width / 3
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

#convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    grayscale_image_inverted = PIL.ImageOps.invert(grayscale_image)
    return grayscale_image_inverted

#convert pixels to ascii
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[int(pixel//(255/(len(ASCII_CHARS)-1)))] for pixel in pixels])
    return characters


def main():
    path = input("Image path:\n")
    new_width = int(input("Ascii image width :\n"))
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Is not a valid path !")


    #convert image to ascii
    new_image_data = pixel_to_ascii(grayify(resize_image(image,new_width)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))


    print(ascii_image)


    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()

a = input("Appuyez sur une touche pour fermer...")
