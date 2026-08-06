'''
OS-Setup - logging.py
This program's purpose is to dynamically create a an executable bash script that installs 
    and configures the programs selected. This module provides logging functions for main

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

(c) 2026 CraftierBark8 on GitHub
Contact me via GitHub or email at h3xl5hs1@duck.com
'''

# import
import datetime
from pathlib import Path

# Start new log and log folder
def log_start():
    # Try to create log
    try:
        current_time = str(datetime.datetime.now())
        global log_name
        log_name = str(current_time + " - OS-Setup.log")
        log_name = log_name.replace(":", ".")
        active_log = open(log_name, "a+")
        starting_lines = "---------- OS-Setup Log ---------- \n" + current_time + " - Log Start \n"
        active_log.write(starting_lines)
    except:
        print("WARNING: Unable to start and/or write to log, logging will be unavailable")
    finally:
        active_log.close()
    return(log_name)

# Add warning to log
# Desc: Adds a warning to the log, optionally writes to terminal (default True)
def log_warn(message, write_term = True):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - WARNING: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        if write_term == True:
            print("WARNING: " + message)

# Exit with error and log
# Desc: Exit with a fatal error, incl. log_name and message, always writes to terminal
def log_exception(exception, message):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - " + exception + ": " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()

# Log event
# Desc: Adds an event to the log, optionally writes event to terminal (default false)
def log_event(message, write_term = False):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - Event: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        # Print to terminal if selected
        if write_term == True:
            print("Event: " + message)

# Log exit
# Desc: Logs an intended exit of the program, always writes to terminal
def log_exit(message):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - Exit: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        exit("Exit: " + message)