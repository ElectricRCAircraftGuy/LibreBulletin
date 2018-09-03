"""
LibreBulletin.py
- This is the main script to run!

LibreBulletin automated bulletin generation
By Gabriel Staples
https://github.com/ElectricRCAircraftGuy/LibreBulletin
"""

# Set "demo" to True to demonstrate this library with example input files which I provide, or set to False to use your
# real input files. My input files for generating the real bulletin for my ward are stored in a subfolder here called
# "PERSONAL_INFO_NOT_FOR_REPO". Since this subfolder also has an empty file in it called "__init__.py", it is also
# considerd a Python "Package", and hence "PERSONAL_INFO_NOT_FOR_REPO/filename.py" type Python "modules" can be imported
# using import statements as shown below.
# For more on Python import statements and packages, see:
# - *****+https://docs.python.org/3/tutorial/modules.html#packages
# - *****+https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory/1260846#1260846
# - *****https://stackoverflow.com/questions/8953844/import-module-from-subfolder/8954533

# demo = True
demo = False

if (demo == True):
    # Import the demonstration config.py file
    import config
else:
    # Import my personal (not shared) config.py file for my ward specifically
    from PERSONAL_INFO_NOT_FOR_REPO import config

import bulletin_find_and_replace