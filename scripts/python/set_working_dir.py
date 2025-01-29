"""
Use this snippet to set the working directory to the scripts own directory.
This is useful when the code may be ran from anywhere and uses relative file paths.
"""

import os # Import os module to access filesystem info

abspath = os.path.abspath(__file__) # Get absolute path of current file
dname = os.path.dirname(abspath) # Get directory component of current file (using absolute path)
os.chdir(dname) # Change working directory to the directory this file is in
