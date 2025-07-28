"""
Module 4 – Files
This script demonstrates basic file operations: writing to and reading from a text file.
"""

# Define the filename
filename = "sample.txt"

# Write to the file
with open(filename, "w") as f:
    f.write("This is a sample file created for Module 4.\n")

# Read and print the file contents
with open(filename, "r") as f:
    print("File contents:")
    print(f.read())
