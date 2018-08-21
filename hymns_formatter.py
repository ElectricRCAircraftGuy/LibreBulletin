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

    print(repr(lines[907])) # use `repr` to print special chars like \n too

    # process the list of strings:
    # - remove whitespace
    # - remove asterisks ("*"); see replace chars: https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
    # - ignore strings beginning with "//" (these are comments)
    # - ignore blank lines (containing only "" after removing whitespace)
    # - ignore lines containing only the word "Play"
    # - remove the word "DOWNLOAD" at the end of each string
    # - All remaining lines at this point should contain just the hymn name followed by the hymn number, so verify 
    #   that the last substring (after calling str.split()) is a number, then, if so, store each line into a new list
    #   in this format: [hymn_num, 'hymn_name'].
    # (Assume you didn't necessarily get the hymn list in order, and that there may be some missing hymn numbers, so 
    #  now do the following):
    # 1. Iterate through this new list, finding the maximum hymn_num present.
    # 2. Create a new list of this size, called hymn_names, initialzing each element as simply "hymn name". The 
    #    index of this list will correspond to hymn_num - 1. 
    # 3. Now read through the last list, copying each hymn name into its corresponding index number in the new list, 
    #    based on the hymn number.
    # - Print the index + 1 and hymn_names to ensure it looks right.
    # - Store the index + 1 and hymn_names into an output file.
    # - Done!
    lines_formatted = list()
    i_read = 0;
    i_write = 0;
    for line in lines:

        # print(repr(lines[i]))

        # For advanced string manipulation help, such as is used below, see: see: https://stackoverflow.com/a/20985070/4561887.
        # Collapse multiple spaces into 1; see: https://stackoverflow.com/a/20985070/4561887
        lines[i_read] = ' '.join(lines[i_read].split())
        # Split by whitespace back into substrings
        s = lines[i_read].split()

        i_read += 1
        # if 


    print(len(lines))
    print(repr(lines[907])) # use `repr` to print special chars like \n too
    print(repr(lines[752]))
    print(repr(lines[709].split()))



if __name__ == '__main__':
    formatHymns("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt")


