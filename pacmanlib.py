import pacman
import subprocess
import time

def pacmanager(pm, inst, upd, confirm, pkgs, remove, action):
    if pm == 'yay' or 'paru':
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
            print('Action not supported')
    elif pm == pacman:
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
            print('Action not supported')
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
            print('Action not supported')
            
def installwinpm(pmname):
    if pmname == 'scoop':
        install = subprocess.Popen('irm get.scoop.sh | iex', shell=True)
        install.wait()
    elif pmname == 'chocolatey' or 'choco':
        install = subprocess.Popen("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))", shell=True)
        install.wait()
    elif pmname == 'winget':
        print('Update windows and winget will be installed')
    else:
        time.sleep()
            
def winpm(pm, action, pkgs, args, var, var2):
    var = pm + ' ' + action + ' ' + pkgs  + ' ' + args
    var2 = subprocess.Popen(var, shell=True)
    var2.wait()
    