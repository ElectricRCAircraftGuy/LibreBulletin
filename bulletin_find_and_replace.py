"""
bulletin_find_and_replace
- perform the automated find-and-replace process in "ward_bulletin_template.odt", replacing strings
  in the document as specified by the user in "bulletin_INPUTS.txt"

Gabriel Staples
Started: 22 Aug. 2018 
Last Updated: See `git log` and/or `git blame`
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
 12. stdtypes (esp. see the "str." functions, such as "str.find()", or "str.replace()"!) - https://docs.python.org/3/library/stdtypes.html
 13. *****Python regular expression (RE) operations & searches - https://docs.python.org/3/library/re.html
 14. Force expression continuation onto next line: https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python

Notes:
 - 

"""

import config # config.py, for paths and stuff
import hymn_num_2_name # For obtaining hymn names from hymn numbers
import zipfile
import os # https://docs.python.org/dev/library/os.path.html#os.path.isdir
import shutil # High-level file/folder manipulation - https://docs.python.org/3/library/shutil.html#shutil.rmtree
import subprocess
import datetime
# import fnmatch # See https://docs.python.org/3/library/fnmatch.html and https://stackoverflow.com/a/11427183/4561887
import re # Regular Expression operations; see: https://docs.python.org/3/library/re.html
import glob # For determining files in directories; see here: https://stackoverflow.com/a/3215392/4561887
from PIL import Image # Pillow (Python Image Library); req. for image conversion
                      # Install: https://stackoverflow.com/a/20061019/4561887
                      # Usage: https://stackoverflow.com/a/10759132/4561887

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
        file = open(self.bulletin_inputs_filepath, "r")
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
        self.special_fields_start_i = len(self.fields) # starting index of the special fields

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
        print("\nReplacing fields...")

        # 1. Uncompress (unzip) the .odt file
        zip_ref = zipfile.ZipFile(self.input_odt_filepath, 'r')
        dir_to_extract_to = "../tmp/" + self.output_odt_filename
        # Delete this temporary dir if it already exists
        if (os.path.isdir(dir_to_extract_to)):
            shutil.rmtree(dir_to_extract_to)
        # Extract to the temporary dir
        zip_ref.extractall(dir_to_extract_to)
        zip_ref.close()

        # 2. Load "content.xml" from the extracted .odt file so I can do the find and replace inside it
        # Example from: https://stackoverflow.com/a/17141572/4561887
        # Read in the "content.xml" file extracted from the .odt file
        contentxml_path = dir_to_extract_to + "/content.xml"
        file = open(contentxml_path, 'r')
        filedata = file.read()
        file.close()
        
        # 3. Replace the Sacrament Meeting portion of the bulletin with the appropriate XML content in case it is 
        # "Fast Sunday"

        # Steps (General Idea): 
        # KEY: (Note: d = 'd'one; m = I 'm'odified this step instead; n = I decided 'n'ot to do this one)
        #
        # d- search content.xml until you find the "START_OF_DELETE_FOR_FAST_SUNDAY" marker string
        # m- search backwards to find the P__ number (paragraph style number) just in front of it, indicating its 
        # formatting style
        # n- jump to the beginning of the document and update its formatting (for this paragraph style number) to be
        # *normal* font color now instead of white
        # d  - Also ensure you have made this style *centered* (now in the xml, or previously, manually in the 
        #  .odt template), since we are about to use it 
        # m- search to the delete start marker again, and replace that string with "FAST AND TESTIMONY MEETING"
        # m- Add a return line just in front of it (look in the xml file for examples of what this looks like)
        # m  - You now have "Administration & Passing of the Sacrament", followed by 2 return lines, followed by 
        #   "FAST AND TESTIMONY MEETING". This is good.
        # m- Add 2 return lines just after "FAST AND TESTIMONY MEETING"
        # m- Delete everything from just after these 2 return lines to the "END_OF_DELETE_FOR_FAST_SUNDAY" marker string,
        # including that marker string itself
        # d- You now have:
        #     Administration and Passing of the Sacrament 
        #     [new line]
        #     [new line]
        #     FAST AND TESTIMONY MEETING [centered, normal black font color]
        #     [new line]
        #     [new line]
        #     Closing Hymn......hymn_hum
        #           hymn_name 
        #     Benediction.....etc etc.
        # d- DONE!
        start_delete_marker = "START_OF_DELETE_FOR_FAST_SUNDAY"
        end_delete_marker = "END_OF_DELETE_FOR_FAST_SUNDAY"

        if (config.fastSunday == True):
            print("fastSunday == True, so converting bulletin to Fast Sunday format.")
            markers_found = True
            # First, ensure the string markers are even present in the filedata string
            if (start_delete_marker not in filedata):
                markers_found = False 
                print("ERROR: start_delete_marker string (\"" + start_delete_marker + "\") NOT FOUND in filedata.")
            if (end_delete_marker not in filedata):
                markers_found = False 
                print("ERROR: end_delete_marker string (\"" + end_delete_marker + "\") NOT FOUND in filedata.")
            if (markers_found == False):
                print("If you are sure the string(s) is/are in the .odt template, ensure the entire string has\n"
                      "consistent formatting by clicking the string in the LibreOffice Writer template,\n"
                      "selecting the \"Clone Formatting\" tool at the top of LibreOffice Writer, then\n"
                      "highlighting the entire string with the tool. This ensures the entire string\n"
                      "has consitent formatting and can now be found contiguously in the compressed,\n"
                      "internal .xml file.")
            else: # markers_found == True
                """
                For the following code, reference this sample content from "content.xml". Note that "=>" indicates
                the deletion start point (`i_delete_start` index below), and "<=" indicates the deletion end point
                (`i_delete_end` index below):
                    <text:p text:style-name="P56">Administration and Passing of the Sacrament</text:p>
                    <text:p text:style-name="P52"/>
                =>  <text:p text:style-name="P57">START_OF_DELETE_FOR_FAST_SUNDAY</text:p>
                    .
                    .
                    .
                    <text:p text:style-name="P57">END_OF_DELETE_FOR_FAST_SUNDAY</text:p>  <=
                """

                # find index to the start of start_delete_marker in filedata
                i = filedata.find(start_delete_marker)
                # print(i) # debugging
                # search backwards to find the end of the *previous* style (ie: the ">" after "P52" above)
                i = filedata.rfind(">", i-1000, i-1)
                # print(i) # debugging
                i_delete_start = i + 1
                # Now find the preceding P number (ie: decipher that it is "P52" just before this point)
                # Regular Expression help: https://docs.python.org/3/library/re.html
                regex_search_pattern = r'"P.{0,5}"' # 'r' for 'r'aw string
                str_found = re.search(regex_search_pattern, filedata[i-10:i]).group(0)
                # strip off the first and last chars since they are the double quotes above
                p_num = str_found[1:-1]
                # print(p_num) # debugging: results in 'P52' for the data as written above
                # Since this paragraph style should be centered and the proper formatting in the .odt template, we 
                # can now use this p number to generate an appropriate "blank line" string.
                # Format: '<text:p text:style-name="P52"/>'
                p_line_str_blanknewline = '<text:p text:style-name="' + p_num + '"/>'
                # We can also determine the beginning and end p_line strings to place before and after text we want
                # formatted with this paragraph style
                p_line_str_beg = '<text:p text:style-name="' + p_num + '">'
                p_line_str_end = '</text:p>'

                # find the index to the end_delete_marker in filedata
                i = filedata.find(end_delete_marker)
                # find the next '>' AFTER this string
                i = filedata.find(">", i+len(end_delete_marker), i+100)
                i_delete_end = i + 1

                # Now delete from i_delete_start to i_delete_end by using the slice operator
                first_half = filedata[:i_delete_start]
                last_half = filedata[i_delete_end:]

                # Now, just before the "Closing Hymn", insert the following:
                """
                    [new line]
                    FAST AND TESTIMONY MEETING [centered, normal black font color]
                    [new line]
                    [new line]
                """
                first_half = (first_half
                              + p_line_str_blanknewline 
                              + p_line_str_beg + "FAST AND TESTIMONY MEETING" + p_line_str_end
                              + p_line_str_blanknewline
                              + p_line_str_blanknewline)

                # re-unite the 2 xml document halfs into one
                filedata = first_half + last_half

        else: # config.fastSunday == False
            print("fastSunday == False, so continuing on withOUT converting to Fast Sunday format.")
            print("Adding the start and end delete markers to the fields list with an empty replace\n" +
                  "string (field_value), so as to force the deletion below.")
            self.fields.append([start_delete_marker, ''])
            self.fields.append([end_delete_marker, ''])

        # 4. Replace the target strings (fields)
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

        # 5. Print the log in the format above now, but in the order it was read from the user's input file:
        print("\nReplacing fields complete.\n" +
              "Field replacement log:\n" + 
              "-Log format: `index: # replacements, ['field_name', 'field_value']`\n" + 
              "---------------------\n" +
              "Start of USER FIELDS:\n" + 
              "---------------------")
        for index, field in enumerate(self.fields):
            field_name = field[0]
            field_value = field[1]
            num_replacements = fields_num_replacements[field_name]
            if (index == self.special_fields_start_i):
                print("------------------------\n" +
                      "Start of SPECIAL FIELDS:\n" + 
                      "------------------------")
            print(str(index) + ": " + str(num_replacements) + ", [\'" + field_name + "\', \'" + field_value + "\']")

        # 6. Replace the document's front cover image
        if (config.front_cover_image_filepath != None):
            print("\nReplacing front cover image...")
            # Get the current font cover image's name and extension, then convert the new image to the same extension 
            # (file type) and name, and make the replacement
            
            pics_dir = dir_to_extract_to + "/Pictures"
            file_list = glob.glob(pics_dir + "/*") # Source: https://stackoverflow.com/a/3215392/4561887
            # assume the front cover image is the first file returned
            # TODO: if this ever isn't the case (ex: if the user ever puts multiple images into their bulletin and
            # this assumption ever becomes wrong), then come up with a more sure solution to find out which image
            # from the "file_list" list is the front cover image (ex: perhaps determine it by which page it's on, 
            # using the 'text:anchor-page-number="1"' tag in the xml file?).
            dest_im_filepath = file_list[0] 
            print("dest_im_filepath = \"" + dest_im_filepath + "\"")
           
            # Convert source image format to destination image format, saving in destination location inside the 
            # extracted .odt directory; see: https://stackoverflow.com/a/10759132/4561887
            source_im = Image.open(config.front_cover_image_filepath)
            source_im.save(dest_im_filepath)

            # TODO: Scale and position the new image as appropriate


        # 7. Write the file out again
        file = open(contentxml_path, 'w')
        file.write(filedata)
        file.close()

        # 8. Rezip up the .odt file
        dir_to_zip = dir_to_extract_to
        shutil.make_archive(self.output_odt_filepath, 'zip', dir_to_zip)
        # the output archive name is now "self.output_odt_filepath.zip", so rename the file by removing the ".zip"
        os.rename(self.output_odt_filepath + ".zip", self.output_odt_filepath)

if __name__ == '__main__':

    bulletin = Bulletin(
        config.input_odt_filepath, config.output_odt_filepath, 
        config.bulletin_inputs_filepath, config.hymns_src_filepath
    )
    bulletin.replaceFields()
    bulletin.openOutputOdtFile()






    # bulletin.printFields()

    # # Test
    # hymn_num = 330
    # hymn_name = bulletin.hymns.getHymnName(hymn_num)
    # print("\nTest:")
    # print("hymn_num = " + str(hymn_num) + "; hymn_name = \"" + hymn_name + "\"")

    # print()
    # print(hymns.getHymnsList())

