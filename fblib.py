import time
import os
from PIL import Image
from multiprocess import process, Manager

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
    
    # Multiprocess function

    def multi(var, procs):
        with Manager():
            pros = Manager.list()
            processes = []
            for i in range(5):
                var = process(target=proclist, args=(procs, i,)
                var.start()
                processes.append(p)
            for p in processes:
                p.join()
        
    
        
