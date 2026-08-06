'''
OS-Setup - setup.py
This program's purpose is to dynamically create a an executable bash script that installs 
    and configures the programs selected

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

(c) 2026 CraftierBark8 on GitHub
Contact me via GitHub or email at h3xl5hs1@duck.com
'''

# -imports-
# SetupLib
try:
    from SetupLib.common import *
    from SetupLib.logging import *
except:
    raise ImportError("Unable to import necessary modules from 'SetupLib'")

# 3rd party dependencies
try:
    import distro
except:
    raise ImportError("Unable to import necessary 3rd party dependencies, make sure you have installed all dependencies in README.md")

# From python
import sys
import argparse
import os
from pathlib import *

# -arg parse-
# Set arguments. commented args are args that have not been implemented
parser = argparse.ArgumentParser(prog='setup.py', usage='setup.py [options]')
parser.add_argument("-a", "--accept", help="Skips the license and warning confirmation (do not use unless already read)", action="store_true")
parser.add_argument("-nl", "--noLog", help="Skips logging to file", action="store_true")
# parser.add_argument("-cfg", "--config", help="Specify the path for a pre-made config file and executes")
parser.add_argument("-d", "--distro", help="Specifies the distro, skipping the question", default="")
parser.add_argument("-de", "--desk_enviro", help="Specifies the desktop environment, skipping the question", default="")
args = parser.parse_args()

# -Start Logging-
# skip logging if requested
if not args.noLog:
    log_name = log_start()

# -License and Warning-
'''
# If -a not passed:
if args.accept:
    # Print warning
    print("----------")
    print("WARNING: This is in development software and may cause unintended, sometimes permanent, damage to systems")
    print("You must read the LICENSE (https://github.com/CraftierBark8/OS-Setup/blob/main/LICENSE) before continuing")
    temp_answer = YN("Have you read the LICENSE and read the warnings?", "Y")
    # If declined
    if temp_answer == False:
        log_exit("Please read the LICENSE before continuing")
# If accepted, log agreement
log_event("User accepted & read LICENSE and read & understood warnings")
'''

# -Compatability Checks-
# Check for Linux
if not "linux" in sys.platform.lower():
    # If not Linux
    log_exception('RuntimeError', "System is not Linux, only Linux is supported")
    raise RuntimeError("System is not Linux, only Linux is supported")

# -Get Distro Info-
# Get directories
base_dir = os.path.dirname(sys.argv[0])
base_dir = Path(base_dir)
config_dir = base_dir / 'Config_Files'

# Check if config folder exists
if not config_dir.is_dir() or not config_dir.exists():

    # Doesn't exist: log and raise exception
    log_exception("NotADirectory", "'Config_Files' directory is not found")
    raise NotADirectoryError("'Config_Files' directory is not found")

# Config folder exists: Get names of folders (distros)
distro_list = []
for sub_dir in config_dir.iterdir():
    if sub_dir.is_dir():
        sub_dir = str(sub_dir).split('Config_Files/')
        distro_list.append(sub_dir[1])
        
# Log detected distros
log_event("Detected distros: " + str(distro_list), True)

# Check if distro specified in args
if not args.distro == "":
    
    # Distro specifed: Set as current and log
    current_distro = str(args.distro).lower()
    log_event("Got current distro from argument as '" + current_distro + "'", True)

    # Check if distro has config
    if not current_distro in distro_list:
        
        # Not in list:
        log_exception('ValueError', "Distro specified in arguments doesn't seem to have a config folder")
        raise ValueError("Distro specified in arguments doesn't seem to have a config folder")
    # Distro in list: continue

else:
    # Distro not specified: get distro and log
    current_distro = (distro.id()).lower()
    log_event("Detected distro '" + current_distro + "' as current distro", True)

    # Check if in list
    if not current_distro in distro_list:
        # Not in list: log and ask for distro from list
        log_event("Detected distro '" + current_distro + "' is not found in config files", True)
        temp_answer = distro_list[selector(distro_list.append('other / unknown'), "Please select your distro from these options:")]
        if temp_answer == len(distro_list) - 1:

            # If 'other' selected: log and raise error
            log_exception('RuntimeError', "User selected 'other / unknown' as distro, " \
            "indicating that their distro was not detected in 'Config_Files' or they do not know it")
            raise RuntimeError("User selected 'other' as distro, indicating that their distro was not detected in 'Config_Files'")
        else:

            # 'other' not selected:
            current_distro = distro_list[temp_answer]
            log_event("Selected '" + current_distro + "' as distro", True)

# -Get Desktop Environment-
# Check if distro folder exists
distro_dir = Path(config_dir / current_distro)
if not distro_dir.is_dir() or not distro_dir.exists():
    # Doesn't exist, log and raise error
    log_exception("RuntimeError", "Directory for distro doesn't exist but has been validated by previous. " \
    "Something is wrong with distro selection")
    raise RuntimeError("Directory for distro doesn't exist but has been validated by previous. " \
    "Something is wrong with distro selection")
# Does exist:

# Get the names of folders in distro_dir and add to list
temp_list = []
for sub_dir in distro_dir.iterdir():
    if sub_dir.is_dir():
        temp_list.append(sub_dir)
# Check if any de detected
if not len(temp_list) > 0:
    log_exception('NotADirectoryError', "No folder detected in " + str(distro_dir))
    raise NotADirectoryError("No folder detected in " + str(distro_dir))
# Check every de for .json files
de_list = []
for de in temp_list:
    # Check if current de has .json files
    json_list = list(Path(de).rglob('*.json'))
    if len(json_list) > 0:
        # Has .json files, append de to de_list
        de = str(de).split(str(current_distro) + "/")
        de_list.append(de[1])

# Check if any valid de found
if len(de_list) > 0:
    log_event("Found valid desktop environment(s): " + str(de_list))
else:
    # No valid DE, log and raise
    log_exception("FileNotFoundError", "No .json found in any folder in selected distro. " \
    "Make sure the desktop environment folder has a '.json' file for configs")
    raise FileNotFoundError("No .json found in any folder in selected distro. " \
    "Make sure the desktop environment folder has a '.json' file for configs")

# Check if de specified
if not args.desk_enviro == "":
    # DE specified, set as current and log
    current_de = str(args.desk_enviro).lower()
    log_event("Got desktop environment from argument as '" + current_de + "'")
    # Check if DE has config
    if not current_de in de_list:
        # Not in list
        log_exception("ValueError", "Desktop environment specified in argument doesn't seem to have a config")
        raise ValueError("Desktop environment specified in argument doesn't seem to have a config")
    # DE in list: continue
else:
    # DE not in args: check if only 1 de
    if not len(de_list) > 1:
        # if only 1, check if de
        temp_answer = YN("Is '" + str(de_list[0]) + "' your desktop environment?", "Y")
        # Check answer
        if temp_answer == True:
            # log and continue
            current_de = str(de_list[0])
            log_event("User confirmed '" + current_de + "' as current desktop environment")
        else:
            # Not correct de
            log_exception('RuntimeError', "User indicated that the only desktop environment detected is not theirs")
            raise RuntimeError("User indicated that the only desktop environment detected is not theirs")
    else:
        # Multiple de: ask which de
        temp_answer = selector(de_list.append("other / unknown"), "Select your current desktop environment:")
        if temp_answer == len(de_list) - 1:
            # if 'other / unknown' selected: log and raise error
            log_exception('RuntimeError', "User selected 'other / unknown' indicating either their desktop environment is" \
            " not an option or they don't understand the question")
            raise RuntimeError("User selected 'other / unknown' indicating either their desktop environment is" \
            " not an option or they don't understand the question")
        else:
            # if 'other' not selected: Set choice as current_de and log
            current_de = de_list[temp_answer]
            log_event("User selected '" + current_de + "' as current desktop environment")