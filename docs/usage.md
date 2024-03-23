# Usage

To use this package the first step is [install it](install.md) of course.
Then is import the package

```python

import fbmodules

```

## Enable / Disables Windows Features

Enable Windows Features and Disable Windows Features use DISM to do that so they need the feature name passed as argument
the feature_name argument is a string, for the next example i'll use the Hypervisor Platform feature

```python

# Enable Hypervisor Platform
fbmodules.enable_windows_features(feature_name='HypervisorPlatform')

# Disable Hypervisor Platform
fbmodules.disable_windows_features(feature_name='HypervisorPlatform')

```

This features can also be used to enable/disable a list of feature but they can't be passed as a list they must be in a for loop. For the next example i'll use the Hypervisor Platform and the Microsoft-Hyper-V-All

```python

# List of Features

list_of_features = ['HypervisorPlatform', 'Microsoft-Hyper-V-All']

# For loop

for feature in list_of_features:
    # Enable Features
    fbmodules.enable_windows_features(featurename=feature)
    # Disable Features
    fbmodules.disable_windows_features(featurename=feature)

```

## Enable / Disable Windows Hibernation

Since the Enable / Disable Windows Hibernation features use the Powercfg built-in Windows they don't require or support arguments as shown in the next example

```python

# Enable Windows Hibernation
fbmodules.enable_windows_hibernation()
# Disable Windows Hibernation
fbmodules.disable_windows_hibernation()

```

## Load Yaml

This function loads a yaml file and return the yaml data as a string to the user, it accepts the file argument as a string which can use relative path.
it uses UTF-8 encoding and it ignores comments

## Run Command

This function runs a command on the operating system and it accepts the command argument as a a string as shown in the next example with the echo command for windows

```python

fbmodules.run_command(command='echo hello from fbmodules')

```

Note: Some commands may only work on a specific operating system

## Change Owner

This function changes the ownership of a file or folder and it accepts the path, user and group arguments as strings as shown in the next example with the 'C:\Windows' folder (DO NOT DO THIS ON WINDOWS IT WILL BREAK YOUR WINDOWS INSTALLATION. This is just an example), the user 'your_user' it should represent the user you wanna use on this function (You can get this with fbmodules.get_current_user), and the group 'your_group' which refers to your user group.

```python

fbmodules.change_owner(path='C:\\Windows', user='your_name', group='your_group')

```

## Get Current User

This function returns the current user that is logged on the operating system

## Help Dialog

This function uses the Windows Shared Library Shell32.dll to open an help dialog and it requires a title, text and icon arguments as strings as show in the next example

```python

fbmodules.help_dialog(title='Help Dialog Title', text='Help Dialog Text', icon='assets/icon.ico')

```

## Check if Internet is Offline

This function uses the Windows Shared Library Shell32.dll to check for internet access

```python

internet_access = fbmodules.is_offline()

```

## Windows Messagebox

This feature is still Work in Progress

## Windows Notifications

This feature is used to send Windows notifications and it accepts the app_id, title, text, and icon(optional) as strings as shown in the next example

```python

fbmodules.windows_notifications(appd_id='You Add Name', title='Your Notification Title', text='Your Notification Text', icon='assets/icon.ico')

```

## Download File

The Download File function accepts the link argument as a string as shown in the next example

```python

fbmodules.download_file(link='https://example.com/downloads/file.e')

```

## Open Link

This function opens a link in a new tab and of course it accepts the link argument as a string as show in the next example

```python

fbmodules.open_link(link='https://example.com/')

```

## Open Steam Link

This function open the steam install prompt for an app or game which is on steam, it only works for games that the user own or free to play games, for the paid games that the user do not have it will give you a steam no license error, it accepts the games argument as a list as show in the next examples with the CS2 (id 730) and Aimlabs (id 714010)

One Game:

```python

# Game List
game_list = ['730']

# Open Steam Link
fbmodules.open_steam_link(games=game_list)

```

Multiple Games:

```python

# Game List
game_list = ['730', '714010']

# Open Steam Link
fbmodules.open_steam_link(games=game_list)

```

### Notes

icons: Note that all examples that have icon use the 'assets/icon.ico' this refers to a icon on the assets folder on your project
downloads: Note that the download file function uses an example domain that may not have the file specified on the download link, '.e' is not a file extension