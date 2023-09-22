# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor
Homework 6 Problem 1

"""

"""
This example demonstrates how to use NumPy to do image transition.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def image_load(filename):
    return plt.imread(filename)

def image_gen(file1, steps=30):
    """Generator for image arrays."""
    img1 = image_load(file1)     # load the image file into ndarrays
    img2 = convert_bw(img1)
        
    # go from img1 to img2 than back to img1. s varies from 0 to 1 and then back to 0:
    svalues = np.hstack([np.linspace(0.0, 1.0, steps), np.linspace(1.0, 0, steps)])
    # construct now the list of images, so that we don't have to repeat that later:
    images = [np.uint8(img2 * (1.0 - s) + img1 * s) for s in svalues]   
    
    # get a  new image as a combination of img1 and img2
    while True:             # repeat all images in a loop
        for img in images:
           yield img 
            
fig = plt.figure()
# create image plot and indicate this is animated. Start with an image.
im = plt.imshow(image_load("ImageManipulation/Data/florida-keys-800-480.jpg"), interpolation='none', 
animated=True)
# the two images must have the same shape:
imggen = image_gen("ImageManipulation/Data/florida-keys-800-480.jpg", steps=30)

# updatefig is called for each frame, each update interval:
def updatefig(*args):
    global imggen
    img_array = next(imggen)     # get next image animation frame
    im.set_array(img_array)       # set it. FuncAnimation will display it
    return (im,)

"""
function convert_bw(img) that takes an image ndarray with shape (height,width,3)
and dtype np.uint8 and returns the B/W (actually, grayscale) version of that image,
also with shape (height,width,3) and the same dtype. 
"""
def convert_bw(img):
    #average all RGB pixels 
    bw_img = np.uint8(np.average(img, axis = 2, weights = None))
    #stack arrays on the 3rd dimension
    bw_img3 = np.dstack([bw_img]*3)
    #return the new image
    return bw_img3

# create animation object that will call function updatefig every 60 ms
ani = animation.FuncAnimation(fig, updatefig, interval=60, blit=False)
plt.title("Image transformation")
plt.show()