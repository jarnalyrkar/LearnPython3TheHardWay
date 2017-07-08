# Imports argv module from the sys package
from sys import argv
# Assigns variables to arguments
script, filename = argv

# Opens the file, and assigns it to a variable.
txt = open(filename)

# just some text.. 
print(f"Here's your file {filename}:")
# prints the file
print(txt.read())

# more text
print("Type the filename again:")
# prompt for another input
file_again = input("> ")
# opens whatever file is inputted
txt_again = open(file_again)

# prints that text file
print(txt_again.read())

txt.close()
txt_again.close()
