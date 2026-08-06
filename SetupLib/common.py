'''
OS-Setup - common.py
This program's purpose is to dynamically create a an executable bash script that installs 
    and configures the programs selected. This module provides common functions for main

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

# -Functions-

# Select from options
# Desc: create a list to select from with passed array, returns index of selected array option
def selector(options, message = ""):
    # Print options
    print()
    if not message == "":
        print(message)
    for i in range(len(options)):
        print("(" + str(i + 1) + ") - " + options[i])

    # Ask for input and validate
    while True:
        selection = input("Select an option (1 to " + str(len(options)) + "): ")
        # Validate
        try:
            selection = int(selection)
            selection = selection - 1
            if selection > -1 and selection < (len(options) + 1):
                return selection
            else:
                print("Error - Please select an option between 1 and " + str(len(options)))
        except "InvalidOption":
            print("Error - Please select an option between 1 and " + str(len(options)))

# Do a y/n message
# Desc: make a [y/n] option message which returns a True or False value
def YN(message, default = ""):
    # Select default
    # Default Y
    if default == "Y" or default == "y":
        # Input and validate
        while True:
            print()
            selection = input(message + " [Y/n]: ")
            if selection == "" or selection == "Y" or selection == "y":
                return True
            elif selection == "N" or selection == "n":
                return False
            else:
                print("Error - Invalid selection. Please enter a Y or N")
    # Default N
    elif default == "N" or default == "n":
        # Input and validate
        while True:
            print()
            selection = input(message + " [y/N]: ")
            if selection == "Y" or selection == "y":
                return True
            elif selection == "" or selection == "N" or selection == "n":
                return False
            else:
                print("Error - Invalid selection. Please enter a Y or N")
    # Default none
    else:
        # Input and validate
        while True:
            print()
            selection = input(message + " [y/n]: ")
            if selection == "Y" or selection == "y":
                return True
            elif selection == "N" or selection == "n":
                return False
            else:
                print("Error - Invalid selection. Please enter a Y or N")