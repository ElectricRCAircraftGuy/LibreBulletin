"""
hymn_num_2_name
- Read in the formatted "hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt" file.
Hymns Source: https://www.lds.org/music/library/hymns?lang=eng

Gabriel Staples
Written: 21 Aug. 2018 
Updated: 21 Aug. 2018
https://www.ElectricRCAircraftGuy.com
- Find my email by clicking the "Contact me" link at the top of my website above.

License: LGPL v3 or later 
(open source; can be used for commercial products; you DO have to maintain this code open source, including any changes
or improvements you make to it, but you do NOT have to open source any of your proprietary code which uses this code)

References:
 - Files: https://docs.python.org/3/tutorial/inputoutput.html
 - Strings: https://www.tutorialspoint.com/python/python_strings.htm
 - Accessing the index in 'for' loops: https://stackoverflow.com/a/28072982/4561887 
 - https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
 - *****Split and parse a string in Python - https://stackoverflow.com/a/20985070/4561887

Notes:
 - 

"""

file_has_been_read = False # Set to True once you've read in the formatted hymns file

def printHymnsList():
    for index, hymn_name in enumerate(hymns_list):
        hymn_num = index + 1
        print(str(hymn_num) + ": " + hymn_name)

def getHymnName(hymn_num):
    return hymns_list[hymn_num - 1]

def readFormattedHymnsFile(filename):
    file = open(filename, "r")

    # Read all lines from the file into a list
    lines = file.readlines()
    file.close()

    # Parse all lines
    # Store hymn names into a new list where index = hymn_num - 1.
    hymns_list = ['hymn_name']*len(lines)
    for line in lines:
        # remove whitespace & place line into a list of strings
        words = line.split()
        # remove the colon from the hymn_num string, and convert str to int
        hymn_num = int(words[0].replace(':', ''))

        hymn_name = ' '.join(words[1:])
        hymns_list[hymn_num - 1] = hymn_name

    return hymns_list

if __name__ == '__main__':
    hymns_list = readFormattedHymnsFile("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt")
    printHymnsList()

    # Test
    hymn_num = 330
    print("\nTest:")
    print("hymn_num = " + str(hymn_num) + "; name = \"" + getHymnName(330) + "\"")


