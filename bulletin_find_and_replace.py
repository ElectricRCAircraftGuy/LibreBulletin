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

Notes:
 - 

"""

import hymn_num_2_name


class Bulletin:

    # 1) Class attributes (shared among all objects [instances] of this class):
    # None

    def __init__(self, input_odt_file, output_odt_file, bulletin_inputs_file, hymns_src_file):
        # 2) Instance attributes (unique for each initialized object [instance] of this class):
        #    - See Reference #6 above for help.

        # Object (class instance) initialization:
        self.hymns = hymn_num_2_name.Hymns(hymns_src_file)

    

if __name__ == '__main__':
    input_odt_file = "./ward_bulletin_template.odt"
    output_odt_file = "../ward_bulletin_template_out_1.odt"
    bulletin_inputs_file = "./bulletin_INPUTS.txt"
    hymns_src_file = "./hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt"

    bulletin = Bulletin(input_odt_file, output_odt_file, bulletin_inputs_file, hymns_src_file)

    # Test
    hymn_num = 330
    hymn_name = bulletin.hymns.getHymnName(hymn_num)
    print("\nTest:")
    print("hymn_num = " + str(hymn_num) + "; hymn_name = \"" + hymn_name + "\"")

    # print()
    # print(hymns.getHymnsList())


