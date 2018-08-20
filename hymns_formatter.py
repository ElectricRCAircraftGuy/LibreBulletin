"""
hymns_formatter
- Format the raw "hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt" file into something more usable

Gabriel Staples
20 Aug. 2018 
https://www.electricrcaircraftguy.com

References:
 - Files: https://docs.python.org/3/tutorial/inputoutput.html
 - Strings: https://www.tutorialspoint.com/python/python_strings.htm
 - Accessing the index in 'for' loops: https://stackoverflow.com/a/28072982/4561887 

To Run: 
Linux:
`python3 hymns_formatter.py`
Windows:
`py -3 hymns_formatter.py`


"""

def formatHymns(filename):
    new_filename = filename[:-4] + "_formatted.txt"
    print("new_filename = " + new_filename)
    file_src = open(filename, "r")
    file_dest = open(new_filename, "w")

    # Read all lines from the file into a list
    lines = file_src.readlines()

    # print(repr(lines[907])) # use `repr` to print special chars like \n too

    # process the list of strings
    lines_formatted = list()
    i_read = 0;
    i_write = 0;
    for i in range(len(lines)):

        # print(repr(lines[i]))

        # Collapse multiple spaces into 1; see: https://stackoverflow.com/a/20985070/4561887
        lines[i] = ' '.join(lines[i].split())
        # Split by whitespace back into substrings
        s = lines[i].split()

        if 


    print(len(lines))
    print(repr(lines[907])) # use `repr` to print special chars like \n too
    print(repr(lines[752]))


if __name__ == '__main__':
    formatHymns("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt")


