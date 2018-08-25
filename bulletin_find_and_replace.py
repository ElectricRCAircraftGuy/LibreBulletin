"""
bulletin_find_and_replace
- perform the automated find-and-replace process in "ward_bulletin_template.odt", replacing strings
  in the document as specified by the user in "bulletin_INPUTS.txt"

Gabriel Staples
Started: 22 Aug. 2018 
Last Updated: See `git log`
https://www.ElectricRCAircraftGuy.com
- Find my email by clicking the "Contact me" link at the top of my website above.

License: LGPL v3 or later 
(open source; can be used for commercial products; you DO have to maintain this code open source, including any changes
or improvements you make to it, but you do NOT have to open source any of your proprietary code which uses this code)

References:
 1. Files: https://docs.python.org/3/tutorial/inputoutput.html
 2. Strings: 
   - https://www.tutorialspoint.com/python/python_strings.htm
   - str.count() & str.replace() - https://docs.python.org/3.3/library/stdtypes.html#str.replace 
 3. Accessing the index in 'for' loops: https://stackoverflow.com/a/28072982/4561887 
 4. https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
 5. *****Split and parse a string in Python - https://stackoverflow.com/a/20985070/4561887
 6. *****+Defining & using a class, incl. class attributes, class instances, etc
    https://python-textbok.readthedocs.io/en/1.0/Classes.html#defining-and-using-a-class 
 7. Zip file manipulation:
   1. https://stackoverflow.com/questions/3451111/unzipping-files-in-python
   2. zipfile module official documentation: https://docs.python.org/3.5/library/zipfile.html
   3. zip a folder in Python (using shutil): https://stackoverflow.com/a/25650295/4561887
 8. Example usage of "os" to determine operating system [my own ans] - https://stackoverflow.com/a/38319607/4561887
 9. Info. on backslashes vs forward slashes for paths in Windows/Linux
   - Best practice: for both, just use forward slashes (/), NOT back-slashes! (\\)
   - https://stackoverflow.com/a/18776536/4561887 
   - https://stackoverflow.com/a/501197/4561887
 10. *****Search & replace text in file: https://stackoverflow.com/a/17141572/4561887
 11. Rename files w/os.rename(): https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python

Notes:
 - 

"""

import hymn_num_2_name # For obtaining hymn names from hymn numbers
import zipfile
import os # https://docs.python.org/dev/library/os.path.html#os.path.isdir
import shutil # High-level file/folder manipulation - https://docs.python.org/3/library/shutil.html#shutil.rmtree
import subprocess
import datetime

VERSION = '0.1.0'

class Bulletin:

    # 1) Class attributes (shared among all objects [instances] of this class):
    # None

    def __init__(self, input_odt_filepath, output_odt_filepath, bulletin_inputs_filepath, hymns_src_filepath):
        # Object (class instance) initialization:
        # 2) Instance attributes (unique for each initialized object [instance] of this class):
        #    - See Reference #6 above for help.
        self.input_odt_filepath = input_odt_filepath
        self.output_odt_filepath = output_odt_filepath
        # Extract output_odt_filename from output_odt_filepath
        self.output_odt_filename = output_odt_filepath.split('/')[-1]
        self.bulletin_inputs_filepath = bulletin_inputs_filepath
        self.hymns = hymn_num_2_name.Hymns(hymns_src_filepath) # Hymns class object; use to call getHymnName(), for instance

        self.loadFields()

    def escapeXMLChars(self, str):
        """
        Convert chars not allowed in XML as text to chars allowed in XML as text
        See: 
         - https://stackoverflow.com/a/28703510/4561887
         - https://wiki.python.org/moin/EscapingXml
        """
        str = str.replace("&", "&amp;")
        str = str.replace("<", "&lt;")
        str = str.replace(">", "&gt;")
        str = str.replace("'", "&apos;")
        str = str.replace('"', "&quot;")
        return str

    def loadFields(self):
        """
        Load field name and value pairs from the bulletin_inputs_filepath document into a class instance variable for
        use by the class.
        """

        # 1. USER FIELDS
        # Parse bulletin fields from the user input document
        # Read in the file
        file = open(bulletin_inputs_filepath, "r")
        lines = file.readlines()
        file.close()
        # Parse lines
        self.fields = [] # empty list
        self.fields_dict = {} # empty dictionary
        for line in lines:
            save_line = True # set to false to discard this line
            # remove whitespace & place line into a list of strings
            words = line.split()
            # discard empty lines
            if (not words):
                # words is an empty list ("[]")
                save_line = False
            else: # Words exist
                # discard comments (lines beginning with "//")  
                first_word = words[0]
                if (len(first_word) >= 2 and first_word[0:2]=='//'):
                    save_line = False
            if (save_line==True):
                # field_name is the first word, minus the ":" character at the end (note: don't use the string
                # "replace()" function to perform this operation, as I only want to replace the ":" char if it is the
                # *last* char of the word!)
                field_name = first_word
                if (field_name[-1] == ':'):
                    field_name = field_name[:-1]
                # field_value is all the rest of the words combined (separate words w/a space), but remember that the 
                # field_value could be blank
                num_words = len(words)
                if (num_words >= 2):
                    field_value = ' '.join(words[1:])
                else:
                    field_value = ''

                # ensure all field names and values are valid in XML files since we will be reading field names and 
                # writing field values into an XML file (stored inside the compressed .odt archive)
                field_name = self.escapeXMLChars(field_name)
                field_value = self.escapeXMLChars(field_value)
                
                # Save lines in list (for general use) as [field_name, field_value], where both are strings
                self.fields.append([field_name, field_value])
                # Save lines in dict (for key-value-lookup use) as {field_name: field_value}, where both are strings
                # TODO: consider getting rid of the self.fields list in the future and using the dictionary only, so as 
                # to avoid redundantly storing the data twice.
                self.fields_dict[field_name] = field_value

        # 2. SPECIAL FIELDS
        # Now load in the "Special Fields" which we need to auto-populate
        # NB: if you update these field names here then they must be updated in the bulletin inputs doc too to 
        # communicate that change to the user.

        # A. Sunday's date
        # Find the date of this coming Sunday, or today's date if today is Sunday
        # Source: https://stackoverflow.com/a/8801540/4561887
        # and: https://stackoverflow.com/a/41056161/4561887
        today = datetime.date.today()
        sunday = today + datetime.timedelta((6 - today.weekday()) % 7)
        month_str = sunday.strftime("%B") # See: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        sunday_date_str = month_str + " " + str(sunday.day) + ", " + str(sunday.year) # Ex. Format: "August 26, 2018"
        self.fields.append(["D_UPCOMING_SUNDAY_DATE", sunday_date_str])

        # B. Hymn names
        # hymn_field_names (tuple of tuples) format = ((HYMN_NAME_FIELDNAME, HYMN_NUM_FIELDNAME))
        hymn_field_names = (
            ("SM_OPENING_HYMN_NAME", "SM_OPENING_HYMN_NUM"),
            ("SM_SACRAMENT_HYMN_NAME", "SM_SACRAMENT_HYMN_NUM"),
            ("SM_INTERMEDIATE_HYMN_NAME", "SM_INTERMEDIATE_HYMN_NUM"),
            ("SM_CLOSING_HYMN_NAME", "SM_CLOSING_HYMN_NUM"),
        )
        # For all elements in the hymn_field_names tuple just above, append the hymn_name field name and 
        # value to "self.fields"
        for hymn_tuple in hymn_field_names:
            # Look up the hymn number using the hymn number field, from the fields dictionary (fields_dict)
            hymn_num_field_name = hymn_tuple[1]
            hymn_num_str = self.fields_dict[hymn_num_field_name]
            if (hymn_num_str.isdigit()):
                hymn_num = int(hymn_num_str)
                # now use the hymn number to look up the hymn name string
                hymn_name = self.hymns.getHymnName(hymn_num)
            else:
                # no hymn_num was input by the user, so just indicate that
                hymn_name = "--NO VALID HYMN NUMBER INPUT BY USER--"

            # now append this special field to the fields list
            hymn_name_field_name = hymn_tuple[0]
            self.fields.append([hymn_name_field_name, hymn_name])

    def printFields(self):
        bulletin_inputs_filename = self.bulletin_inputs_filepath.split('/')[-1]
        print("Printing input fields from \"" + bulletin_inputs_filename + "\":\n" +
              "Format: ['field_name', 'field_value']")
        for field in self.fields:
            print(field)

    def openOutputOdtFile(self):
        """
        Open up the output .odt file in your system's default editor for it (should be LibreOffice)
        Source: https://stackoverflow.com/a/435669/4561887
        """
        if (os.name == 'nt'): # For Windows
            os.startfile(self.output_odt_filepath)
        elif (os.name == 'posix'): # For Linux, Mac, etc.
            subprocess.call(('xdg-open', self.output_odt_filepath))

    def replaceFields(self):
        # 1. Uncompress (unzip) the .odt file
        zip_ref = zipfile.ZipFile(self.input_odt_filepath, 'r')
        dir_to_extract_to = "../tmp/" + self.output_odt_filename
        # Delete this temporary dir if it already exists
        if (os.path.isdir(dir_to_extract_to)):
            shutil.rmtree(dir_to_extract_to)
        # Extract to the temporary dir
        zip_ref.extractall(dir_to_extract_to)
        zip_ref.close()

        # 2. Load "content.xml" from the extracted .odt file, and do the find and replace inside it
        # Example from: https://stackoverflow.com/a/17141572/4561887

        # Read in the "content.xml" file extracted from the .odt file
        contentxml_path = dir_to_extract_to + "/content.xml"
        file = open(contentxml_path, 'r')
        filedata = file.read()
        file.close()
        
        # Replace the target strings (fields)
        # NB: you must do the replacement in the order of the field_names being *reverse-sorted*, so that longer string
        # replacement occur before short ones. Ex: if field names & values are: ['AA', 'hello'] and ['A', 'goodbye'],
        # then you need to find and replace field "AA" with "hello" *before* finding and replacing "A" with
        # "goodbye". Otherwise, "AA" will get replaced by "goodbyegoodbye" instead of "hello" due to 
        # the "A" field replacement occuring before "AA" is even searched. 
        fields_rev_sorted = self.fields.copy()
        fields_rev_sorted.sort(reverse = True)
        fields_num_replacements = {} # dictionary to store the # of replacements for each field
        for index, field in enumerate(fields_rev_sorted):
            field_name = field[0]
            field_value = field[1]
            num_replacements = filedata.count(field_name) # Number of times the field_name occurs inside the file
            fields_num_replacements[field_name] = num_replacements
            filedata = filedata.replace(field_name, field_value)

        # Print the log in the format above now, but in the order it was read from the user's input file:
        print("\nReplacing fields\n" +
              "Log format: `index: # replacements, ['field_name', 'field_value']`")
        for index, field in enumerate(self.fields):
            field_name = field[0]
            field_value = field[1]
            num_replacements = fields_num_replacements[field_name]
            print(str(index) + ": " + str(num_replacements) + ", [\'" + field_name + "\', \'" + field_value + "\']")

        # Write the file out again
        file = open(contentxml_path, 'w')
        file.write(filedata)
        file.close()

        # 3. Rezip up the .odt file
        dir_to_zip = dir_to_extract_to
        shutil.make_archive(self.output_odt_filepath, 'zip', dir_to_zip)
        # the output archive name is now "self.output_odt_filepath.zip", so rename the file by removing the ".zip"
        os.rename(self.output_odt_filepath + ".zip", self.output_odt_filepath)

if __name__ == '__main__':

    # NB: use forward slashes (/) for path names, NOT back slashes (\)!--Even in Windows!
    input_odt_filepath = "./ward_bulletin_template.odt"
    output_odt_filepath = "../ward_bulletin_template_out_1.odt"
    bulletin_inputs_filepath = "./bulletin_INPUTS.txt"
    hymns_src_filepath = "./hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt"

    bulletin = Bulletin(input_odt_filepath, output_odt_filepath, bulletin_inputs_filepath, hymns_src_filepath)

    # Test
    hymn_num = 330
    hymn_name = bulletin.hymns.getHymnName(hymn_num)
    print("\nTest:")
    print("hymn_num = " + str(hymn_num) + "; hymn_name = \"" + hymn_name + "\"")

    # print()
    # print(hymns.getHymnsList())

    bulletin.printFields()
    bulletin.replaceFields()
    bulletin.openOutputOdtFile()
