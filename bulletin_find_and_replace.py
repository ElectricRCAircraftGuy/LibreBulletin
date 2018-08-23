"""
bulletin_find_and_replace
- perform the automated find-and-replace process in "ward_bulletin_template.odt", replacing strings
  in the document as specified by the user in "bulletin_INPUTS.txt"

Gabriel Staples
Written: 22 Aug. 2018 
Updated: 22 Aug. 2018
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
 7. Zip file manipulation:
   1. https://stackoverflow.com/questions/3451111/unzipping-files-in-python
   2. zipfile module official documentation: https://docs.python.org/3.5/library/zipfile.html
 8. Example usage of "os" to determine operating system - https://stackoverflow.com/a/38319607/4561887
 9. Info. on backslashes vs forward slashes for paths in Windows/Linux
   - Best practice: for both, just use forward slashes (/), NOT back-slashes! (\\)
   - https://stackoverflow.com/a/18776536/4561887 
   - https://stackoverflow.com/a/501197/4561887

Notes:
 - 

"""

import hymn_num_2_name # For obtaining hymn names from hymn numbers
import zipfile
import os # https://docs.python.org/dev/library/os.path.html#os.path.isdir
import shutil # High-level file/folder manipulation - https://docs.python.org/3/library/shutil.html#shutil.rmtree

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

    def loadFields(self):
        """
        Load field name and value pairs from the bulletin_inputs_filepath document.
        """

        # Parse bulletin fields from input document
        # Read in the file
        file = open(bulletin_inputs_filepath, "r")
        lines = file.readlines()
        file.close()
        # Parse lines
        self.fields = []
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
                # field_name is the first word, minus the ":" character
                field_name = first_word.replace(':','')
                # field_value is all the rest of the words combined (separate words w/a space), but remember that the 
                # field_value could be blank
                num_words = len(words)
                if (num_words >= 2):
                    field_value = ' '.join(words[1:])
                else:
                    field_value = ' '

                # Save lines as [field_name, field_value]
                self.fields.append([field_name, field_value])
        
    def printFields(self):
        bulletin_inputs_filename = self.bulletin_inputs_filepath.split('/')[-1]
        print("Printing input fields from \"" + bulletin_inputs_filename + "\":\n" +
              "Format: ['field_name', 'field_value']")
        for field in self.fields:
            print(field)

    def replaceFields(self):
        # 1. Uncompress (unzip) the .odt file
        zip_ref = zipfile.ZipFile(self.input_odt_filepath, 'r')
        dir_to_extract_to = "../tmp/" + self.output_odt_filename
        # Delete this dir if it already exists
        if (os.path.isdir(dir_to_extract_to)):
            shutil.rmtree(dir_to_extract_to)
        # Extract
        zip_ref.extractall(dir_to_extract_to)
        zip_ref.close()

        # 2. 

    

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
    # bulletin.replaceFields()

