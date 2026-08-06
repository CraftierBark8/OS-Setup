# <ins>Documentation
This page is seperated into sections for the different functions located in OS-Setup. I am new to advanced programming so this documentation will probably be updated many times as I get a better understanding for documentation standards. As of right now this is probably considered technical documentation, describing what the various functions and programs are doing and the architecture behind them.
***

## <ins>Sections
1. Main
    1.1 [setup.py](https://github.com/CraftierBark8/OS-Setup/blob/main/setup.py)
    1.2 [software.json](https://github.com/CraftierBark8/OS-Setup/blob/main/software.json)
2. [SetupLib](https://github.com/CraftierBark8/OS-Setup/blob/main/SetupLib)
    2.1 [common.py](https://github.com/CraftierBark8/OS-Setup/blob/main/SetupLib/common.py)
    2.2 [logging.py](https://github.com/CraftierBark8/OS-Setup/blob/main/SetupLib/logging.py)
3. Config_Files
    3.1 File Structure
4. Misc
    3.1 requirements.txt
    3.1 Software Used
***
## 1. <ins>Main
Documentation for the files in the root of OS-Setup.

### 1.1 setup
The `setup.py` file is the main python program in OS-Setup.

**Arguments**
```
optional:
-h  --help        | Displays the help message and exits
-a  --accept      | Skips the license and warning confirmation (do not use unless already read)
-nl --noLog       | Skips creating a .log file, things will still print to terminal
-d  --distro      | Specifies a distro to use, skipping the question
-de --desk_enviro | Specifies a desktop environment, skipping the question
```
***
## 2. <ins>SetupLib
This section is for the python module I have developed for this program, named `SetupLib`, and the python functions it contains.

### 2.1 common

#### `selector(options)`
The function `selector()` takes the parameter `options` and displays the array as a list to be selected from. It also uses the optional `message` parameter to display a message above the options. The user inputs the requested options and returns the index of the selected option. The function also validates the input is a valid input.
Returns the index of the selected option in the array passed in `options`. Example:

Input:
```
options = ["apt", "yum", "dnf", "zypper", "pacman", "other"]
message = "Please select what package manager you use"
```
Print:
```
Please select what package manager you use
(1) - apt
(2) - yum
(3) - dnf
(4) - zypper
(5) - pacman
(6) - other
Select an option (1-6): 1
```
Returns `0`, this is because the index of the item 'apt' is 0, despite the option selected being 1.

#### `YN(message, default = "")`
The function `YN()` takes the parameter `message` and displays it with a `[y/n]:` message. The parameter `default` changes the behaviour of the prompt if nothing is answered. By default (without any argument passed) it doesn't allow a blank answer. Prompt will change according to the default option selected. 
Returns `True` if `Y` and `False` if `N`. Example:

Input:
```
message = "Have you read the LICENSE?"
default = "Y"
```
Print:
```
Have you read the LICENSE? [Y/n]: n
```
Returns `False`

### 2.2 logging
Note: This logging feature currently only supports .log files that are kept in the same directory as the .py file executing the logging functions.

#### `log_start()`
`log_start()` creates a new .log file with the date and time along with "OS-Setup" being the title. Also adds the starting lines to the log.
Returns the name of the log created so that it can be modified.

#### `log_warn(message, write_term = True)`
`log_warn()` modifies the file .log file started in 'log_start()' by adding a line with the current date & time, plus the message `WARNING: ` and the message. By default it also shows this message in the terminal but without the date and time, but that can be turned off by setting `write_term` to `False`

#### `log_exception(exception, message)`
`log_exception` adds the message (current date and time plus `Exception: ` plus the exception name passed as 'exception' and the message passed as `message`) to a new line in the log, as identified 'log_start()'. It **does not** raise the exception itself, that must be done after logging. It will always write the exception message, minus the date and time, to the terminal.

#### `log_exit(message)`
`log_exit()` makes a new line in the .log file identified by log_start() with the date & time plus the word `Exit:` and the message passed in the `message` parameter. This is different from the `log_exception()` function as it indicates the program has reached an end that was programmed as opposed to exception.'

#### `log_event(message, write_term = False)`
The function `log_event` adds a new line to the .log file started with 'log_start()' with the date & time plus the string `Event:` and the message passed in `message`. By default this does not write the event to the terminal but it can if `write_term` is set to `True`.
***
## <ins>3. Config_Files
This folder contains all the files necessary to setup any particular distro. Any distro to be supported must have the proper config files to support it.

### File Structure
The Config_Files structure is as follows:
- Config_Files/
    - [distro]/
        - [desktop_environment]/
            - software.json
            - [profile_name].json

Notes:
- Brackets denote a placeholder name.
- '[distro]' is a placeholder for the name of your distro, it must be in all lowercase, without the brackets. There can be multiple 'distro' folders but none can have the same name.
- Within '[distro]' you must have at least 1 folder with the name of the desktop environment, called '[desktop_environment]' in the file structure above, also in lowercase. There can be more than 1 desktop environment folder but none can have the same name.
- Every '[desktop_environment]' folder must have a 'software.json' file.
- '[profile_name].json' is to show where you would put a profile. The name of the profile is the file name with the '.json' file type.

## 4. <ins>Misc.
This stuff didn't fit in the other sections so here it is.
### 4.1 requirements.txt
List of requirements to be installed with pip install.
- [distro](https://pypi.org/project/distro/)
### 4.2 Software Used

#### Installed Software:
- [FastFetch](https://github.com/fastfetch-cli/fastfetch) - A cli info tool that acts very similarly to the, now-deprecated, neofetch.
- [Oh My Bash!](https://github.com/ohmybash/oh-my-bash) - A community-driven framework for managing BASH configs.