
import platform
import subprocess
import os

def install_package(package_name):
    system = platform.system()
    if system == 'Linux':
        dist = platform.linux_distribution()[0]
        if dist in ['Ubuntu', 'Debian']:
            subprocess.run(['sudo', 'apt', 'install', '-y', package_name])
        elif dist in ['Fedora']:
            subprocess.run(['sudo', 'dnf', 'install', '-y', package_name])
        elif dist in ['arch']:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', package_name])
        else:
            print(f"Package manager not supported for {dist}")
    elif system == 'Windows':
        if os.path.exists("C:\\Program Files\\WindowsApps\\Winget\\Winget.exe"):
            subprocess.run(['winget', 'install', '-e', package_name])
        elif os.path.exists("C:\\ProgramData\\chocolatey\\bin\\choco.exe"):
            subprocess.run(['cmd.exe', '/c', 'start', 'cmd.exe', '/k', 'choco', 'install', package_name, '-y'], shell=True)
        else:
            print("Package manager not supported")
    else:
        print(f"Package manager not supported for {system}")

def remove_package(package_name):
    system = platform.system()
    if system == 'Linux':
        dist = platform.linux_distribution()[0]
        if dist in ['Ubuntu', 'Debian']:
            subprocess.run(['sudo', 'apt', 'remove', '-y', package_name])
        elif dist in ['Fedora']:
            subprocess.run(['sudo', 'dnf', 'remove', '-y', package_name])
        elif dist in ['arch']:
            subprocess.run(['sudo', 'pacman', '-R', '--noconfirm', package_name])
        else:
            print(f"Package manager not supported for {dist}")
    elif system == 'Windows':
        if os.path.exists("C:\\Program Files\\WindowsApps\\Winget\\Winget.exe"):
            subprocess.run(['winget', 'remove', '-e', package_name])
        elif os.path.exists("C:\\ProgramData\\chocolatey\\bin\\choco.exe"):
            subprocess.run(['cmd.exe', '/c', 'start', 'cmd.exe', '/k', 'choco', 'uninstall', package_name, '-y'], shell=True)
        elif os.path.exists("C:\\ProgramData\\Scoop\\shim\\scoop.exe"):
            subprocess.run(['scoop', 'uninstall', package_name])
        else:
            print("Package manager not supported")
    else:
        print(f"Package manager not supported for {system}")

def update_system():
    system = platform.system()
    if system == 'Linux':
        dist = platform.linux_distribution()[0]
        if dist in ['Ubuntu', 'Debian']:
            subprocess.run(['sudo', 'apt', 'update'])
            subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
        else:
          if dist in ['Fedora']:
              subprocess.run(['sudo', 'dnf', 'update', '-y'])
          elif dist in ['arch']:
              subprocess.run(['sudo', 'pacman', '-Syu', '--noconfirm'])
          else:
              print(f"Package manager not supported for {dist}")
    elif system == 'Windows':
        if os.path.exists("C:\Program Files\WindowsApps\Winget\Winget.exe"):
            subprocess.run(['winget', 'update'])
        elif os.path.exists("C:\ProgramData\chocolatey\bin\choco.exe"):
            subprocess.run(['cmd.exe', '/c', 'start', 'cmd.exe', '/k', 'choco', 'upgrade', 'all', '-y'], shell=True)
        elif os.path.exists("C:\\ProgramData\\Scoop\\shim\\scoop.exe"):
            subprocess.run(['scoop', 'update', 'all'])
        else:
            print("Package manager not supported")
    else:
        print(f"Package manager not supported for {system}")

def remove_unneeded_dependencies():
  system = platform.system()
  if system == 'Linux':
    dist = platform.linux_distribution()[0]
    if dist in ['Ubuntu', 'Debian']:
        subprocess.run(['sudo', 'apt', 'autoremove', '-y'])
    elif dist in ['Fedora']:
        subprocess.run(['sudo', 'dnf', 'autoremove', '-y'])
    elif dist in ['arch']:
        subprocess.run(['sudo', 'pacman', '-Rns', '--noconfirm', '$(pacman -Qtdq)'])
    else:
        print(f"Package manager not supported for {dist}")
  else:
    print(f"Package manager not supported for {system}")
