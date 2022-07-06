from PIL import Image

def convert(binary) -> str:
    print(binary)
    return chr(int(binary, 2))

def dechiffrer(chiffred: Image.Image, original_image: Image.Image) -> str:
    it = iter(chiffred.getdata())
    it2 = iter(original_image.getdata())
    validation = 1
    message = ""
    while validation:
        letter = ""
        for i in range(3):
            chiffred_pixel = tuple(next(it))
            original_pixel = tuple(next(it2))
            for j in range(3):
                if i != 0 or j != 0:
                    if chiffred_pixel[j] - original_pixel[j] == 1: # on a ajouté 1
                        letter += "1"
                    elif original_pixel[j] - chiffred_pixel[j] == 1:
                        letter += "0"
                    elif original_pixel[j] == chiffred_pixel[j]:
                        letter += str(original_pixel[j] % 2)
                elif chiffred_pixel[j] == original_pixel[j] or (original_pixel[j] == chiffred_pixel[j] and original_pixel[j] % 2 == 0): # on a ajouté 1
                        validation = False
                        break
        message += convert(letter)
    return message


                