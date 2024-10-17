def rgb_to_cmyk(r,g,b):
    r/=255
    g/=255
    b/=255
    
    v = max(r,g,b)
    k = 1-v
    if v == 0:
        return (0,0,0,1)
    c = 1 - r/v
    m = 1 - g/v
    y = 1 - b/v
    return (c,m,y,k)

def cmyk_to_rgb(c,m,y,k):
    v = 1 - k
    r = v - v *c
    g = v - v *m
    b = v - v *y
    return (round(r * 255), round(g * 255), round(b * 255))

print(rgb_to_cmyk(0,0,0))
print(rgb_to_cmyk(50, 100, 75))
print(cmyk_to_rgb(*rgb_to_cmyk(50, 100, 75)))

from PIL import Image

image = Image.open("parrot.jpg")
data = image.load()

for y in range(image.height):
    for x in range(image.width):
        pixel = data[x,y]
        
        bw = (pixel[0], pixel[0], pixel[0])
        
        cmyk = rgb_to_cmyk(*pixel)
        
        cmyk2 = (min(1,cmyk[0]+.5), cmyk[1], cmyk[2], min(1,cmyk[3]), )
        
        rgb = cmyk_to_rgb(*cmyk2)
        data[x,y] = rgb

image.save("done.png")
