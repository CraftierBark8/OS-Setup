# Setup Script

# imports
try:
    from SetupLib.common import *
    from SetupLib.logging import *
except:
    exit("Fatal Error: Unable to import 'SetupLib'")

import sys

# init vars
log_name = ""
temp_answer = ""

# Start Logging
log_name = log_start()

# -Compatability Checks-
# Check for Linux
if not "linux" in sys.platform.lower():
    # If not Linux
    log_warn(log_name, "This computer is not running Linux, things may not work as intended.")
else:
    # If linux, ask if apt
    temp_answer = YN("Does this computer run apt?", "")
    if temp_answer == True:
        log_event(log_name, "User confirmed distro runs apt")
    else:
        log_event(log_name, "User said distro doesn't run apt")
        log_warn(log_name, "This setup should only be used to make configs for other systems that run apt")

# -License and Warning-
print("----------")
# Warning
print("WARNING: This is in-development software and may cause unintended, sometimes permanent, damage to systems")
temp_answer = YN("Have you read and understood the warnings here?")
if temp_answer == False:
    log_exit(log_name, "Please read the printed and LICENSE warnings before continuing")
# LICENSE
print("")
print("You must read the LICENSE (https://github.com/CraftierBark8/OS-Setup/blob/main/LICENSE) before continuing")
temp_answer = YN("Have you read the LICENSE?")
if temp_answer == False:
    log_exit(log_name, "Please read the LICENSE before continuing")
# Log agreement
log_event(log_name, "User accepted & read LICENSE and read & understood warnings")