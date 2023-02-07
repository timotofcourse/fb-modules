import time
import os
from PIL import Image

# First of all this library is for my own use, you can use it too but some things if not all i made for my specific needs

pros = [] # This list if for processes

# This variables i made to use in my own python games

textures = 'assets/textures/' # Location for textures
audio = 'assets/audio/' # Location for audios
images = 'assets/imgs/' # Location for other images that are not textures


# Check if a file exists

def find(filename, var):
    var = os.path.exists(filename)

# Load an image

def img(load):
    Image.open(load)

def proclist(proc):
    pros.append(proc)
    
