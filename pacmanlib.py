import pacman
import subprocess
import os

# Home 
home = os.path.expanduser( '~' )

def pacmanager(pm, inst, upd, confirm, pkgs, remove, action):
    if pm == 'yay' or 'paru': # Yay or Paru AUR Helpers. I Could add more but i'm lazy and i can add them later anyway
        if action == 'install':
            subprocess.Popen(pm + ' ' + inst + ' ' + confirm).wait()
        elif action == 'update':
            subprocess.Popen(pm + ' ' + upd + ' ' + confirm).wait()
        elif action == 'remove':
            subprocess.Popen(pm + ' ' + remove + ' ' + confirm).wait()
        elif action == 'update and install':
            subprocess.Popen(pm + ' ' + upd + ' ' + confirm).wait()
            subprocess.Popen(pm + ' ' + inst + ' ' + confirm).wait()
        else:
            print('Action not supported') # Code for Debug purposes
    elif pm == pacman: # If Pacman use the python-pacman module to do this actions
        if action == 'install':
            pacman.install(pkgs)
        elif action == 'update':
            pacman.upgrade()
        elif action == 'remove':
            pacman.remove(pkgs)
            pacman.needs_for(pkgs)
        elif action == 'update and install':
            subprocess.Popen(pm + ' ' + upd + ' ' + confirm).wait()
            subprocess.Popen(pm + ' ' + inst + ' ' + confirm).wait()
        else:
            print('Action not supported') # Code for Debug purposes
    else :
        if action == 'install':
            subprocess.Popen('sudo ' + pm + ' ' + inst + ' ' + pkgs + ' ' + confirm).wait()
        elif action == 'update':
            subprocess.Popen('sudo ' + pm + ' ' + upd + ' ' + confirm).wait()
        elif action == 'remove':
            subprocess.Popen('sudo ' + pm + ' ' + remove + ' ' + confirm).wait()
        elif action == 'update and install':
            subprocess.Popen('sudo ' + pm + ' ' + upd + ' ' + confirm).wait()
            subprocess.Popen('sudo ' + pm + ' ' + inst + ' ' + pkgs + ' ' + confirm).wait()
        else:
            print('Action not supported') # Code for Debug purposes
          
# Windows Package Managers Path

scoop_path = '/scoop'
choco_path = 'C:/ProgramData/chocolatey/bin'
            
def checkwindowspm(): # Check if windows package managers are installed
    os.path.exists()

if checkwindowspm(scoop_path):
    print('Scoop Installed')
else:
    subprocess.Popen('irm get.scoop.sh | iex', shell=True).wait()

if checkwindowspm(choco_path):
    print('Chocolatey Installed')
else:
    subprocess.Popen("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))", shell=True).wait()

            
def winpm(pm, action, pkgs, args):
    subprocess.Popen(pm + ' ' + action + '' + pkgs + '' + args, shell=True).wait()
    