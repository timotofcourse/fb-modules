from os import system, getlogin
from ruamel.yaml import YAML
import shutil

# Enable Windows Feature

def enable_windows_feature(feature_name):
    system(f'dism /Online /Enable-Feature /{feature_name}')
    
# Disable Windows Feature

def enable_windows_feature(feature_name):
    system(f'dism /Online /Disable-Feature /{feature_name}')

# Enable Windows Hibernation

def enable_windows_hibernation():
    system('powercfg /hibernate on')

# Disable Windows Hibernation

def disable__windows_hibernation():
    system('powercfg /hibernate off')
    
# Load Yaml

def load_yaml(file):
    yaml = YAML(typ='safe')
    with open(file, 'r', encoding='utf-8') as yaml_file:
        yaml_data = yaml.load(yaml_file)
    return yaml_data

# Run command

def run_command(command):
    system(command)
    
# Change owner

def change_owner(path, user=None, group=None):
    shutil.chown(path, user, group)
    
# get current user

def get_current_user():
    getlogin()
    
