import time
import os
from PIL import Image

pros = []
textures = 'assets/textures/'
audio = 'assets/audio/'
images = 'assets/imgs/'


if __name__ == '__main__':

    # Check if a file exists

    def find(filename, var):
        var = os.path.exists(filename)

    # Load an image

    def img(load):
        Image.open(load)

    def proclist(proc):
        pros.append(proc)
    
