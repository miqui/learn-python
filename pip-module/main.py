import pip
import os

# Get a list of installed packages
packages = pip.list_packages()

# Store the package list in a text file
with open("packages.txt", "w") as f:
    f.write("\n".join(["- ", package]) for package in packages]))

# Print the package list
print(open("packages.txt").read())
