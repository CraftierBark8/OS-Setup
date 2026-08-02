# A list of common functions for setup

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
        selection = input("Please Select an option (1 to " + str(len(options)) + "): ")
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