"""
hymns_formatter
- Format the raw "hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt" file into something more usable
Hymns Source: https://www.lds.org/music/library/hymns?lang=eng

Gabriel Staples
Written: 20 Aug. 2018 
Updated: 20 Aug. 2018
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
 - `print(repr(lines[907]))` # use `repr` to print special chars like \n too

To Run: 
Linux:
`python3 hymns_formatter.py`
Windows:
`py -3 hymns_formatter.py`


"""

def printHymnsList(hymns_list):
    for index, hymn_name in enumerate(hymns_list):
        hymn_num = index + 1
        print(str(hymn_num) + ": " + hymn_name)

def formatHymns(filename):
    new_filename = filename[:-4] + "_formatted.txt"
    print("new_filename = " + new_filename)
    file_src = open(filename, "r")
    file_dest = open(new_filename, "w")

    # Read all lines from the file into a list
    lines = file_src.readlines()
    file_src.close()

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
    max_hymn_num_found = 0
    for line in lines:
        save_line = True # set to false to discard this line
        
        # remove asterisks
        line = line.replace("*", "")
        # remove whitespace & place line into a list of strings
        words = line.split()
        # discard empty lines
        if (not words):
            # words is an empty list ("[]")
            save_line = False
        else: # Words exist
            first_word = words[0]
            num_words = len(words)
            last_word = words[-1]

            if (len(first_word) >= 2):
                # discard comments (lines beginning with "//"), and lines containing only the word "Play"
                if (first_word[0:2]=='//' or (num_words==1 and first_word=='Play')):
                    save_line = False 

            # Remove last word if it is "DOWNLOAD"
            if (last_word=="DOWNLOAD"):
                words.pop() # remove last word

            # Verify the last word is a number (ie: the hymn number)
            last_word = words[-1]
            if (last_word.isdigit()==False):
                save_line = False

        if (save_line==True):
            # Save lines as [hymn_num, "hymn_name"]
            hymn_num = int(last_word)
            if (hymn_num > max_hymn_num_found):
                max_hymn_num_found = hymn_num
            words.pop() # remove last word
            hymn_name = ' '.join(words)
            lines_formatted.append([hymn_num, hymn_name])

    print("\nmax_hymn_num_found = " + str(max_hymn_num_found))
    print("lines_formatted:")
    for line in lines_formatted:
        print(line)

    # Now that we have lines_formatted, let's sort it into a new list where index = hymn_num - 1.
    hymns_list = ['hymn_name']*max_hymn_num_found

    # print this new "hymns_list" before filling it with real data, to ensure it looks right
    printHymnsList(hymns_list)

    # Copy data into it (thereby also sorting any hymns which may be out of their sorted order)
    for hymn in lines_formatted:
        hymn_num = hymn[0]
        hymn_name = hymn[1]
        hymns_list[hymn_num-1] = hymn_name

    # Now print them all out:
    printHymnsList(hymns_list)

    # Now store them in a file:
    for index, hymn_name in enumerate(hymns_list):
        hymn_num = index + 1
        file_dest.write(str(hymn_num) + ": " + hymn_name)
        # Only add a new-line char if it is NOT the last line!
        if (hymn_num < len(hymns_list)):
            file_dest.write("\n")
    file_dest.close()

if __name__ == '__main__':
    formatHymns("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt")


