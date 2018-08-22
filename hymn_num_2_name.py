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
 1. Files: https://docs.python.org/3/tutorial/inputoutput.html
 2. Strings: https://www.tutorialspoint.com/python/python_strings.htm
 3. Accessing the index in 'for' loops: https://stackoverflow.com/a/28072982/4561887 
 4. https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
 5. *****Split and parse a string in Python - https://stackoverflow.com/a/20985070/4561887
 6. *****+Defining & using a class, incl. class attributes, class instances, etc
    https://python-textbok.readthedocs.io/en/1.0/Classes.html#defining-and-using-a-class 

Notes:
 - 

"""

class Hymns:

    # 1) Class attributes (shared among all objects [instances] of this class):
    # None

    def __init__(self, filename):
        # 2) Instance attributes (unique for each initialized object [instance] of this class):
        #    - See Reference #6 above for help.

        # Object (class instance) initialization:
        self.hymns_list = [] # NB: empty list, so len(hymns_list)==0 here.
        self.readFormattedHymnsFile(filename)

    def printHymnsList(self):
        # only do for non-empty lists
        if (len(self.hymns_list) > 0):
            for index, hymn_name in enumerate(self.hymns_list):
                hymn_num = index + 1
                print(str(hymn_num) + ": " + hymn_name)
        else:
            print("printHymnsList Error: self.hymns_list not yet populated. \n" +
                  "Call readFormattedHymnsFile() first to populate it.")

    def getHymnName(self, hymn_num):
        # only do for non-empty lists
        if (len(self.hymns_list) > 0):
            hymn_name = self.hymns_list[hymn_num - 1]
        else:
            hymn_name = "getHymnName Error"
            print("printHymnsList Error: self.hymns_list not yet populated. \n" +
                  "Call readFormattedHymnsFile() first to populate it.")
        return hymn_name

    def readFormattedHymnsFile(self, filename):
        # Read all lines from the file into a listpython 
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        # Parse all lines
        # Store hymn names into a new list where index = hymn_num - 1.
        self.hymns_list = ['hymn_name']*len(lines)
        for line in lines:
            # remove whitespace & place line into a list of strings
            words = line.split()
            # remove the colon from the hymn_num string, and convert str to int
            hymn_num = int(words[0].replace(':', ''))
            # join the remaining words after the hymn_num into the hymn_name
            hymn_name = ' '.join(words[1:])
            self.hymns_list[hymn_num - 1] = hymn_name

    def getHymnsList(self):
        return self.hymns_list

if __name__ == '__main__':
    hymns = Hymns("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt")
    hymns.printHymnsList()

    # Test
    hymn_num = 330
    hymn_name = hymns.getHymnName(hymn_num)
    print("\nTest:")
    print("hymn_num = " + str(hymn_num) + "; hymn_name = \"" + hymn_name + "\"")

    # print()
    # print(hymns.getHymnsList())


