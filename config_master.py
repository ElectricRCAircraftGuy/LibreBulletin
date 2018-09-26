"""
# config_master.py
- the master configuration file

LibreBulletin automated bulletin generation
By Gabriel Staples
https://github.com/ElectricRCAircraftGuy/LibreBulletin
"""

# ----------------------------------------------------------------------------------------------------------------------
# USER PARAMETERS
# Update these parameters to customize your bulletin!
# ----------------------------------------------------------------------------------------------------------------------

# Set to True to demonstrate this library with example input files I have already provided, or set to False to use your
# real input files (which are, in my case for generating the real bulletin for my ward, written below)
demo = True
# demo = False

# In case you use `demo = False` above, pull the bulletin inputs from this bulletin_INPUTS file:
# - Set it to "auto" to force the program to automatically choose the bulletin_INPUTS file for you!
# - It will do this by scanning for all relevant files in the "auto_search_folder", set below, ensuring their names
# match the "auto_search_pattern" regular expression set below, alphabetizing them, then choosing the *last* one in the
# list! This way you can name them chronologically, for instance, as "YYYYMMDDn--filename.txt"  (Ex: "20180930#1--
# myWardBulletinInputs.txt", for your bulletin inputs for 30 Sept. 2018). Now, by simply using the "auto" setting below,
# with the correct "auto_search_pattern", you can manually copy and paste your .txt file each new week, then increment
# the date at the front of its name, and the script will automatically pull this, the latest file when  auto-building
# the bulletin!
# bulletin_INPUTS = "./MY_PERSONAL_WARD_INFO/20180930#1--2bulletin_INPUTS.txt"
bulletin_INPUTS = "auto" # Uncomment to automatically use your latest bulletin_INPUTS file instead, as described above.

# Only used if `bulletin_INPUTS = "auto"`:
# Automatically search for the last-alphabetically-listed *.txt file in this folder, to be used as your bulletin inputs
# file:
auto_search_folder = "./MY_PERSONAL_WARD_INFO"
# Only search for files whose names match this *regular expression* search pattern.
# See: 1) https://en.wikipedia.org/wiki/Regular_expression.
#      2) Regex tester: https://regex101.com/
# Ex: "[0-9]{8}.?.?--.*\.txt" will match any file names that look like "20180930#1--myWardBulletinInputs.txt", or 
# "20180930--myWardBulletinInputs.txt", etc.
auto_search_pattern = "[0-9]{8}.?.?--.*\.txt"

# ----------------------------------------------------------------------------------------------------------------------
# PROGRAMMER PARAMETERS (not intended to be changed by user)
# ----------------------------------------------------------------------------------------------------------------------

# LibreBulletin version
# Note: use Semantic Versioning (https://semver.org/spec/v2.0.0.html)
VERSION = '0.2.0'

# This demonstration user inputs file is used when demo is set to True above.
bulletin_INPUTS_default = "./bulletin_INPUTS.txt"


