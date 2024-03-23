# Documentation

This is a simples module that makes it a bit easier to make some things i and a few more people may need to use

for install instructions [Click Here](install.md)

## List of functions

This are the current features of this package for the usage [Click Here](usage.md)

- Enable Windows Features
- Disable Windows Features
- Enable Windows Hibernation
- Disable Windows Hibernation
- Load Yaml
- Run Command
- Change Owner
- Get Current User
- Check for Admin
- Get Admin
- Help Dialog
- Check if Internet is Offline
- Windows Messagebox
- Windows Notifications
- Download File
- Open Link
- Open Steam Link

## Used tools

This packages uses [cURL](https://curl.se) for downloads since cURL is present on most Operating Systems, it uses safe load from ruamel.yaml to load yaml files to make sure yaml files with comments don't break the user scripts, for Windows specific features it uses the build in features on Windows such as [DISM](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/dism-image-management-command-line-options-s14?view=windows-11) and [Powercfg](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options) and it interfaces with libraries for admin access, Windows messageboxes and Help Dialog, for steam links it's just the steam protocol.