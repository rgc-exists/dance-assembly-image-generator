
width = 25
height = 25
x_pos = 0
y_pos = 0
z_pos = 3
pixel_size_x = .1
pixel_size_y = .1
pixel_size_z = .1
im_path = "C:\\Users\\User1\Example_Path\\Example_File.png"





























#https://www.tutorialspoint.com/How-to-clamp-floating-numbers-in-Python
#Because I am too lazy to write a clamp function
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

import cv2
import numpy as np
obj_id = 1
output = ""
i = 0
width = 25
height = 25
img = cv2.imread(im_path)
img = cv2.resize(img, (width, height))
for x in range(width):
    for y in range(height):
        pixel = img[height-1-y][x]
        #print(pixel)
        #print(pixel[2])
        output += r'{"objectId":' + str(obj_id) + r',"objectName":"Pixel","originalPrefab":0,"objectParentId":-1,"color":{"r":'+ str(clamp((pixel[2]/255), 0, 1)) + r',"g":' + str(clamp((pixel[1]/255), 0, 1)) +  r',"b":' + str(clamp((pixel[0]/255), 0, 1)) + r',"a":1},"position":{"x":' + str((x*pixel_size_x)+x_pos) + r',"y":' + str((y*pixel_size_y)+y_pos) + r',"z":' + str(z_pos) + r'},"rotation":{"x":0.0,"y":0.0,"z":0.0,"w":1.0},"scale":{"x":' + str(pixel_size_x) + r'0.1,"y":' + str(pixel_size_y) + r'0.1,"z":' + str(pixel_size_z) + r'0.1},"receiveShadows":false,"emitLight":false,"emitLightColor":{"r":0.0,"g":0.0,"b":0.0,"a":1.0},"emitLightIntensity":0.0,"isCamera":false,"isDisplayingCamera":false,"cameraDisplayingValue":0,"objectIsEnabled":true},'
        obj_id += 1
f = open("C:\\Users\\rando\\OneDrive\\Documents\\Output.txt", "w")
f.write(output)
