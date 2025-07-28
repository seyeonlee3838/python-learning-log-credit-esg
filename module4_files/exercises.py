# Module 4 – Files
filename = "sample.txt"
with open(filename, "w") as f:
    f.write("This is a sample file created for Module 4.\n")

with open(filename, "r") as f:
    print("File contents:")
    print(f.read())
