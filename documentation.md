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
***
## <ins>2. Main
Documentation for the files in the root of OS-Setup.

### 1.1 setup
The `setup.py` file is the main python program in OS-Setup.

**Arguments**
```
optional:
-h   --help   | Displays the help message and exits
-a   --accept | Skips the license and warning confirmation (do not use unless already read)
-nl  --noLog  | Skips creating a .log file, things will still print to terminal
-pm           | Specifies a package manager to use, skipping the question
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

#### `log_warn(log_name, message, write_term = True)`
`log_warn()` modifies the file passed as `log_name` by adding a line with the current date & time, plus the message `WARNING: ` and the message. By default it also shows this message in the terminal but without the date and time, but that can be turned off by setting `write_term` to `False`

#### `log_fatal(log_name, message)`
`log_fatal` adds the message (current date and time plus `Fatal Error:` plus the passed `message`) to a new line in the log, as identified by the `log_name` parameter. It also exits the program. It will always write the fatal error message, minus the date and time, to the terminal.

#### `log_exit(log_name, message)`
`log_exit()` makes a new line in the .log file identified in the parameter `log_name` with the date & time plus the word `Exit:` and the message passed in the `message` parameter. This is different from the `log_fatal()` function as it indicates the program has reached an end that was programmed as opposed to error.'

#### `log_event(log_name, message, write_term = False)`
The function `log_event` adds a new line to the .log file passed in `log_name` with the date & time plus the string `Event:` and the message passed in `message`. By default this does not write the event to the terminal but it can if `write_term` is set to `True`.
***