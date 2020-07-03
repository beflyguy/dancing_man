import imageio
from PIL import Image
import os
import shutil
import random
from tqdm import tqdm

root = "C:/Users/sambe/Documents/Personal/dancing_man/"
src = "original_images"

colors = {'red': (255,0,0),
          'green': (0,255,0),
          'blue': (0,0,255),
          'yellow': (255,255,0),
          'orange': (255,127,0),
          'white': (255,255,255),
          'black': (0,0,0),
          'gray': (127,127,127),
          'pink': (255,127,127),
          'purple': (127,0,255),}

def distance(left, right):
    return sum( (l - r) ** 2 for l, r in zip(left, right)) ** 0.5

class NearestColorKey(object):
    def __init__(self, goal):
        self.goal = goal
    def __call__(self, item):
        return distance(self.goal, item[1])

def change_color(image,color_1,color_2,color_3):
    picture = Image.open(image)
    picture = picture.convert('RGB')
    width, height = picture.size
    
    for x in range(width):
        for y in range(height):
            r,g,b  = picture.getpixel( (x,y) )

            new_color_1 = colors[color_1]
            new_color_2 = colors[color_2]
            new_color_3 = colors[color_3]

            if min(colors.items(), key=NearestColorKey((r,g,b)))[0] == 'blue':
                picture.putpixel((x,y), new_color_1)
            if min(colors.items(), key=NearestColorKey((r,g,b)))[0] == 'white':
                picture.putpixel((x,y), new_color_2)
            if min(colors.items(), key=NearestColorKey((r,g,b)))[0] == 'black':
                picture.putpixel((x,y), new_color_3)
            
    picture.save(image)

def reset_color(image,color_1,color_2,color_3):
    picture = Image.open(image)
    picture = picture.convert('RGB')
    width, height = picture.size
    
    for x in range(width):
        for y in range(height):
            r,g,b  = picture.getpixel( (x,y) )

            if min(colors.items(), key=NearestColorKey((r,g,b)))[0] == color_1:
                picture.putpixel((x,y), (0,0,255))
            if min(colors.items(), key=NearestColorKey((r,g,b)))[0] == color_2:
                picture.putpixel((x,y), (255,255,255))
            if min(colors.items(), key=NearestColorKey((r,g,b)))[0] == color_3:
                picture.putpixel((x,y), (0,0,0))
    
    picture.save(image)

random_int = random.randint(0,9)
def change_all(color_1,color_2,color_3):
    for file in tqdm(os.listdir(root + src)):
        if str(random_int) in file: 
            change_color(root + src + '/' + file, color_1, color_2, color_3)

def reset_all(color_1,color_2,color_3):
    for file in tqdm(os.listdir(root + src)):
        if str(random_int) in file: 
            reset_color(root + src + '/' + file, color_1, color_2, color_3)

def gif_time():
    images = []
    for file in tqdm(os.listdir(root + src)):
        images.append(imageio.imread(src + '/' + file))
    imageio.mimsave(root + 'dancing_man.gif')


# change_all('purple','green','red')
print(random_int)
gif_time()
# reset_all('purple','green','red')