#!/bin/bash

# Setup my preferred linux config on various distros

# Import Libraries

# Functions

# Determine Package Manager
determine_pm() {
    # init variables
    package_manager="0"

    # List package managers
    package_manager_list=("apt" "yum" "dnf" "zypper" "pacman" "snap" "flatpak")

    # Check for package manager version
    for pm in $package_manager_list; do
        if [ command "$pm" -v == *"command not found"* ]; then 
        else
            package_manager="$pm"
            break
        fi
    done
}