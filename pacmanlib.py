import time
import pacman
import subprocess

if __name__ == '__main__':

    def pacmanager(pm, var, inst, upd, confirm, pkgs, var2, remove, action, var3):
        if pm == 'yay' or 'paru':
            if action == 'install':
                var = subprocess.Popen(pm + inst + confirm)
                var.wait()
            elif action == 'update':
                var = subprocess.Popen(pm  + upd + confirm)
                var.wait()
            elif action == 'remove':
                var = subprocess.Popen(pm + remove + confirm)
                var.wait()
            elif action == 'update and install':
                var2 = subprocess.Popen(pm  + upd + confirm)
                var2.wait()
                var = subprocess.Popen(pm + inst + confirm)
                var.wait()
            else:
                print('Action not supported')
        else :
            if action == 'install':
                var = subprocess.Popen('sudo ' + pm + inst + pkgs + confirm)
                var.wait()
            elif action == 'update':
                var2 = subprocess.Popen('sudo ' + pm + upd + confirm)
                var2.wait()
            elif action == 'remove':
                var = subprocess.Popen('sudo ' + pm + remove + confirm)
                var.wait()
            elif action == 'update and install':
                var2 = subprocess.Popen('sudo ' + pm + upd + confirm)
                var2.wait()
                var = subprocess.Popen('sudo ' + pm + inst + pkgs + confirm)
                var.wait()
            else:
                print('Action not supported')
            
    