from PIL import Image
import os

image1 = Image.open('d:\\Users\\Sahand\\Documents\\GitHub\\Python\\Coursera\\Deep Learning\\Practice\\image01.jpg')

for f in os.listdir('.'):
    print(f)