import time
import os
from PIL import Image
from pygame import mixer

# First of all this library is for my own use, you can use it too but some things if not all i made for my specific needs

pros = [] # This list if for processes

# This variables i made to use in my own python games

textures = 'assets/textures/' # Location for textures
audio = 'assets/audio/' # Location for audios
images = 'assets/imgs/' # Location for other images that are not textures
models = 'assets/models' # Location for models if i need them

# Initiate the audio mixer

mixer.init()

# Check if a file exists

def find(filename, var):
    var = os.path.exists(filename)

# Load an image

def img(load):
    Image.open(load)

def proclist(proc):
    pros.append(proc)
    
# Audio function for games and other apps that i need to play some audio. I require to pass the mtime because i want to control the time manually instead of getting it from the mp3 files

def gaudio(audiofile, audiovolume, mtime):
    mixer.music.load(audiofile)
    mixer.music.set_volume(audiovolume)
    mixer.music.play()
    time.sleep(mtime)
    mixer.music.stop()