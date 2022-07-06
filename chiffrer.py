from PIL import Image

def chiffrer(image: Image.Image, message: str) -> Image.Image:
    image2 = image.copy()
    bin_message = [f"1{bin(ord(x)).replace('b', '')}" for x in message]
    x, y = 0, 0
    pixels = iter(image.getdata())
    for letter in bin_message:
        for i in range(3):
            rgb = list(next(pixels))
            for j in range(3):
                number_letter = int(letter[i*3 + j])
                if rgb[j] % 2 != number_letter:
                    if number_letter == 0:
                        rgb[j] -= 1
                    else : # number letter is 1
                        rgb[j] += 1
            image2.putpixel((x, y), tuple(rgb))
            x += 1
            if x == image.width:
                y += 1
                x = 0
    return image2
            
if __name__ == "__main__":
    with Image.open('asset.png', 'r') as image:
        message = "a"
        print(*list(image.getdata())[:3*len(message)])
        image2 = chiffrer(image, message)
        print(*list(image2.getdata())[:3*len(message)])
