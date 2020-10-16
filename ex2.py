import random
from PIL import Image, ImageDraw  

img = Image.open('pic.jpg')  
draw = ImageDraw.Draw(img)  
w = img.size[0]  
h = img.size[1]  
px = img.load()  

for x in range(w):
    for y in range(h):
       r = px[x, y][0] 
       g = px[x, y][1] 
       b = px[x, y][2] 
       sr = (r + g + b) 
       draw.point((x, y), (sr, sr, sr)) 

image.save("respic.jpg", "JPEG") 