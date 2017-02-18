#!/usr/bin/python

from website import app
from website.config import *

import math
import sys
from PIL import Image, ImageMath
import numpy as np


def colorize(img):
    #r,g,b = np.array(img)
    pixels = img.load()
    for x in range(img.size[0]):    # for every pixel:
        for y in range(img.size[1]):
            pixel = pixels[x,y]
            v = (pixel[0] / 128.0) - 1
            #new_green = int(127 * (1 + (green / math.sqrt(1 + green**2))))
            new_lum = int(64 * (math.tanh(v) + 1))
            pixels[x,y] = (new_lum, pixel[0], new_lum)

    #colorized = np.array([r, g / np.sqrt(1 + np.square(g)), b])
    #return Image.fromarray(colorized,'RGB')


def heatmap(r_path, mono_path):
    print "Reading red channel from %s" % r_path
    r = Image.open(r_path)

    print "Reading mono channel from %s" % mono_path
    mono = Image.open(mono_path)

    histogram = ImageMath.eval("convert(mono - r, 'RGB')", r=r, mono=mono)
    colorize(histogram)
    histogram.save("out/heatmap.png")

