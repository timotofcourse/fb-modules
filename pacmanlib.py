import pacman
import subprocess
import time

def pacmanager(pm, var, inst, upd, confirm, pkgs, var2, remove, action):
    if pm == 'yay' or 'paru':
        if action == 'install':
            var = subprocess.Popen(pm + ' ' + inst + ' ' + confirm)
            var.wait()
        elif action == 'update':
            var = subprocess.Popen(pm + ' ' + upd + ' ' + confirm)
            var.wait()
        elif action == 'remove':
            var = subprocess.Popen(pm + ' ' + remove + ' ' + confirm)
            var.wait()
        elif action == 'update and install':
            var2 = subprocess.Popen(pm + ' ' + upd + ' ' + confirm)
            var2.wait()
            var = subprocess.Popen(pm + ' ' + inst + ' ' + confirm)
            var.wait()
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
            var2 = subprocess.Popen(pm + ' ' + upd + ' ' + confirm)
            var2.wait()
            var = subprocess.Popen(pm + ' ' + inst + ' ' + confirm)
            var.wait()
        else:
            print('Action not supported')
    else :
        if action == 'install':
            var = subprocess.Popen('sudo ' + pm + ' ' + inst + ' ' + pkgs + ' ' + confirm)
            var.wait()
        elif action == 'update':
            var2 = subprocess.Popen('sudo ' + pm + ' ' + upd + ' ' + confirm)
            var2.wait()
        elif action == 'remove':
            var = subprocess.Popen('sudo ' + pm + ' ' + remove + ' ' + confirm)
            var.wait()
        elif action == 'update and install':
            var2 = subprocess.Popen('sudo ' + pm + ' ' + upd + ' ' + confirm)
            var2.wait()
            var = subprocess.Popen('sudo ' + pm + ' ' + inst + ' ' + pkgs + ' ' + confirm)
            var.wait()
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
    