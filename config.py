
# ----------------------------------------------------------------------------------------------------------------------
# USER PARAMETERS
# ----------------------------------------------------------------------------------------------------------------------

# Turn fastSunday format on or off by setting this value to True, False, or "auto". "auto" will have the script
# automatically  make an educated guess by assuming that the 1st Sunday of each month is "Fast Sunday", which is
# normally the case. 
# See "bulletin_INPUTs.txt" for which user fields this setting affects.
fastSunday = True # True, False, or "auto"

# TODO: make this control the date placed on the bulletin. Anything before this time will use today's date, if today is
# Sunday. Anything equal to or after this time will use next Sunday's date on the bulletin, even if today is Sunday.
# This way, if you run the bulletin script before church you'll get today's date on it, but if you run it after church
# (ex: in preparation for the next Sunday), you'll get next Sunday's date on it.
timeToUseNextSundayDate = "12:30pm" # TODO: determine proper format: datetime library vs string?

# Paths:
# NB: use forward slashes (/) for path names, NOT back slashes (\)!--Even in Windows!
# For relative paths, use "." for the current directory and ".." for one directory up.
input_odt_filepath = "./ward_bulletin_template.odt"
output_odt_filepath = "../ward_bulletin_template_out_1.odt"
bulletin_inputs_filepath = "./bulletin_INPUTS.txt"
hymns_src_filepath = "./hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt"

# Must be either a ".odt" document with a single image saved in it, OR a ".png", ".jpg", or ".bmp" image.
# Set to "None" (without the quotes) if you don't want to replace the front cover image.
# ie: `front_cover_image_filepath = None`
# TODO: TEST OUT IMAGE CONVERSION WITH PILLOW, AND GET THIS WORKING.###########
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

# ----------------------------------------------------------------------------------------------------------------------
# PROGRAMMER PARAMETERS (not intended to be changed by user)
# ----------------------------------------------------------------------------------------------------------------------

# Note: use Semantic Versioning (https://semver.org/spec/v2.0.0.html)
VERSION = '0.0.0' # Increment to 0.1.0 and beyond once I have decided to release my first "done" version