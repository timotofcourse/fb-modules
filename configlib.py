import configparser
import json

jsondict = {}

# JSON save function

def jsonsave(filename):
    with open(filename, 'w') as f:
        json.dump(jsondict, f)

# JSON load function

def jsonload(filename):
    with open(filename, 'r') as f:
        jsondict.load(f)
        f.close()
    
# Config parser load function

def loadconf(filename, section, conf, config):
    a = configparser.ConfigParser()
    a.read(filename)

    config = a[section][conf]

# Config parser save function

def saveconf(filename, section, conf, config):
    a = configparser.ConfigParser()
    a.read(filename)
    a[section][conf]=config
    with open(filename, "w") as file_object:
        a.write(file_object)

