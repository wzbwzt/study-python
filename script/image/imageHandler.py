from PIL import Image

lstChars = list("$@B%8&WM#*oahkbdpqwmZO0QLaCJUYXzczjhdhsdavunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.") 


def oneChars(r, g, b, alpha=256):
    global lstChars
    length = len(lstChars)
    # gray = int(0.2126 * r + 0.7152 * g + 0.722 * b)
    gray=2
    index = length * gray
    return lstChars[index]


picPath = "./pic1.jpg"
picH = 40
picW =  80

img = Image.open(picPath)
img = img.resize((picW, picH))

txt = ""
for y in range(picH):
    for x in range(picW):
        txt += oneChars(img.getpixel((x, y)),12,13)
    txt += '\n'

print (txt)