# Setup Script

# imports
try:
    from SetupLib.common import *
    from SetupLib.logging import *
except:
    exit("Fatal Error: Unable to import necessary modules from 'SetupLib'")

import sys
import argparse

# -init vars-
# vars
log_name = ""
temp_answer = ""
pac_man = ""

# lists
list_package_managers = ["apt", "yum", "dnf", "zypper", "pacman", "other"]
valid_package_managers = ["apt"]

# -arg parse-
# Set arguments. commented args are args that have not been implemented
parser = argparse.ArgumentParser(prog='setup.py', usage='setup.py [options]')
parser.add_argument("-h", "--help", help="Displays this message and exits")
parser.add_argument("-a", "--accept", help="Skips the license and warning confirmation (do not use unless already read)", action="store_true")
parser.add_argument("-nl", "--noLog", help="Skips logging to file", action="store_true")
# parser.add_argument("-cfg", "--config", help="Specify the path for a pre-made config file and executes")
parser.add_argument("-pm", help="Specifies the package manager, skipping the question", default="")
args = parser.parse_args()

# -Start Logging-
# skip logging if requested
if not args.noLog:
    log_name = log_start()

# -License and Warning-
if args.accept:
    print("----------")
    print("WARNING: This is in development software and may cause unintended, sometimes permanent, damage to systems")
    print("You must read the LICENSE (https://github.com/CraftierBark8/OS-Setup/blob/main/LICENSE) before continuing")
    temp_answer = YN("Have you read the LICENSE and read the warnings?", "Y")
    if temp_answer == False:
        log_exit(log_name, "Please read the LICENSE before continuing")
# Log agreement
log_event(log_name, "User accepted & read LICENSE and read & understood warnings")

# -Compatability Checks-
# Check for Linux
if not "linux" in sys.platform.lower():
    # If not Linux
    log_warn(log_name, "This computer is not running Linux, things may not work as intended.")

# -Ask for package manager-
# if -pm arg was not specified
if args.pm == "":
    pac_man = selector(list_package_managers, "Please select the package manager you use")
    pac_man = list_package_managers[pac_man]
    log_event(log_name, "Package Manager set to: " + pac_man, True)
# if -pm was specified
else:
    pac_man = str(args.pm)
    pac_man = pac_man.lower()
    # check if specifed pm is known
    if not pac_man in list_package_managers:
        log_exit(log_name, "Package manager `" + pac_man + "`is not a recognized package manager")

# -Check if package manager valid-
if not pac_man in valid_package_managers:
    log_exit(log_name, "The package manager `" + pac_man + "` is not supported.")