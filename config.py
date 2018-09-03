
# ----------------------------------------------------------------------------------------------------------------------
# USER PARAMETERS
# Update these parameters to customize your bulletin!
# ----------------------------------------------------------------------------------------------------------------------

# Set to True to demonstrate this library with example input files, or set to False to use your real input files
# (which are, in my case for generating the real bulletin for my ward, written below)
# demo = True
demo = False

# Fast Sunday formatting:
# Turn fastSunday format on or off by setting this value to True, False, or "auto". "auto" will have the script
# automatically  make an educated guess by assuming that the 1st Sunday of each month is "Fast Sunday", which is
# normally the case. 
# See "bulletin_INPUTs.txt" for which user fields this setting affects.
fastSunday = False # True, False, or "auto"

# TODO: make this control the date placed on the bulletin. Anything before this time will use today's date, if today is
# Sunday. Anything equal to or after this time will use next Sunday's date on the bulletin, even if today is Sunday.
# This way, if you run the bulletin script before church you'll get today's date on it, but if you run it after church
# (ex: in preparation for the next Sunday), you'll get next Sunday's date on it.
timeToUseNextSundayDate = "12:30pm" # TODO: determine proper format: datetime library vs string?

# Bulletin Input Template, Output File, & Hymns Paths:
# NB: use forward slashes (/) for path names, NOT back slashes (\)!--Even in Windows!
# For relative paths, use "." for the current directory and ".." for one directory up.
hymns_src_filepath = "./hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt"
if (demo == True):  
    # Demonstration input files to see this code function
    input_odt_filepath = "./ward_bulletin_template.odt"
    output_odt_filepath = "../ward_bulletin_template_out_1.odt"
    bulletin_inputs_filepath = "./bulletin_INPUTS.txt"
else: 
    # My real input files to generate my bulletin
    input_odt_filepath = "./PERSONAL_INFO_NOT_FOR_REPO/20180909#1--Ward Bulletin Template.odt"
    output_odt_filepath = "./PERSONAL_INFO_NOT_FOR_REPO/20180909#1--Ward Bulletin.odt"
    bulletin_inputs_filepath = "./PERSONAL_INFO_NOT_FOR_REPO/20180909#1--bulletin_INPUTS.txt"

# Cleaning assignments:
# The cleaning assignments list must be a "csv" (Comma-Separated Variable) type file. You can easily export this 
# file type from Microsoft Excel, LibreOffice Calc, or Google docs spreadsheets. 
# - NB: "this year" and "next year" are relative to the *upcoming Sunday's date*, NOT to *today's* date (whatever date
# "today" may be)! That means if this upcoming Sunday is the first Sunday in 2019, then the file for "this year"
# ("cleaning_assignments_csv_filepath_this_yr") better be set to a file for *2019*, NOT 2018! Otherwise, the table will
# be filled wrong since it has no way of identifying from the data which year the data is for. It can simply
# detect where the data *transitions* from one year to another is all.
# - Set the paths below to "None" (without the quotes) to disable automatic filling of this table in the bulletin, or 
# you can simply remove the cleaning assignments table and its associated "Special Fields" from the bulletin.
if (demo == True):
    # Demonstration input files to see this code function   
    # - Ex: uncomment the below 2 lines, and comment out the 2 lines below that to disable this feature.
    # cleaning_assignments_csv_filepath_this_yr = None 
    # cleaning_assignments_csv_filepath_next_yr = None
    cleaning_assignments_csv_filepath_this_yr = "./cleaning_assignments_2018.csv"
    cleaning_assignments_csv_filepath_next_yr = "./cleaning_assignments_2019.csv"
    cleaning_assignments_num_header_rows = 1 # Number of rows in the .csv files which contain header names instead of data
else: 
    # My real input files to generate my bulletin
    cleaning_assignments_csv_filepath_this_yr = "./PERSONAL_INFO_NOT_FOR_REPO/20180909#1--Cleaning Assignments - 2018.csv"
    cleaning_assignments_csv_filepath_next_yr = None
    cleaning_assignments_num_header_rows = 1 # Number of rows in the .csv files which contain header names instead of data

# Front cover image:
# Must be either a ".odt" document with a single image saved in it, OR a ".png", ".jpg", or ".bmp" image.
# TODO: IMPLEMENT THE ability to read image in from another .odt file. This shouldn't be that hard. 
# Also, test Pillow's ability to use/convert png and bmp files (I've already tested .jpg to .png and it works fine).
# Set to "None" (without the quotes) if you don't want to replace the front cover image.
# ie: `front_cover_image_filepath = None`
if (demo == True):
    # For demonstration purposes to see this code function:
    # front_cover_image_filepath = None # Uncomment this, and comment out the line below to disable image replacement.
    front_cover_image_filepath = "pics/the-second-coming-39621-print.jpg"
    # For scaling & positioning the image:
    # - These are the max x/y sizes, as the image will be scaled proportionally to its original x/y dimensions, but not
    #   to exceed these max image sizes below.
    max_image_size_x_in = 4.5 # inches; default: 4.5 in
    max_image_size_y_in = 4.65 # inches; default: 4.65 in

    # frame sizes (ie: the x/y area on the page where the image needs to fit)
    # - these parameters are required separately from the max_image_size x/y above so that image centering calcs
    #   still work even if you shrink the image (via the max_image_size x/y parameters above) to be smaller than 
    #   the frame size
    frame_size_x_in = 4.5 # inches
    frame_size_y_in = 4.65 # inches
    # frame position
    frame_left_x_pos_in = 6 # inches; from left side of entire page
    frame_top_y_pos_in = 0.25 # inches; from top of entire page
else:
    front_cover_image_filepath = "pics/the-second-coming-39621-print.jpg"
    max_image_size_x_in = 4.5 # inches; default: 4.5 in
    max_image_size_y_in = 4.65 # inches; default: 4.65 in
    frame_size_x_in = 4.5 # inches
    frame_size_y_in = 4.65 # inches
    frame_left_x_pos_in = 6 # inches; from left side of entire page
    frame_top_y_pos_in = 0.25 # inches; from top of entire page

# TODO: In the distant future in the far-away land of Distasia (ie: someday--not important right now), I need to do a
# better job of automatically vertically-centering the contents of the front cover when I do the automatic front cover
# image replacement. Currently, I only take into account the "frame size" above, which is simply the size of the
# imaginary box that I'd like the front cover image to fit into, above the text box below the image, and below some
# reasonable location near the top of the page. This does a pretty good job of vertically centering the image, but since
# it doesn't also shift the text box below the image around, it can't do it perfectly.  So, **add vertical centering of
# the text box below the image** as part of the process when vertically centering the image. This will require
# identifying it, looking up its x, y, width, height parameters in contents.xml, calculating new values, and doing the
# replacement, but will allow perfect vertical centering of both the new front cover image and the text box each time a
# new image is added.
# CURRENT WORKAROUND: just manually bump the image up or down and the text box up or down with the arrow keys before
# printing and after doing the automatic image replacement/bulletin generation each week. Done! Good enough for now!


# ----------------------------------------------------------------------------------------------------------------------
# PROGRAMMER PARAMETERS (not intended to be changed by user)
# ----------------------------------------------------------------------------------------------------------------------

# Note: use Semantic Versioning (https://semver.org/spec/v2.0.0.html)
VERSION = '0.0.0' # Increment to 0.1.0 and beyond once I have decided to release my first "done" version