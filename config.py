
# Turn fastSunday format on or off by setting this value to True, False, or "auto". "auto" will have the script
# automatically  make an educated guess by assuming that the 1st Sunday of each month is "Fast Sunday", which is
# normally the case. 
# See "bulletin_INPUTs.txt" for which user fields this setting affects.
fastSunday = True # True, False, or "auto"

# Paths:
# NB: use forward slashes (/) for path names, NOT back slashes (\)!--Even in Windows!
# For relative paths, use "." for the current directory and ".." for one directory up.
input_odt_filepath = "./ward_bulletin_template.odt"
output_odt_filepath = "../ward_bulletin_template_out_1.odt"
bulletin_inputs_filepath = "./bulletin_INPUTS.txt"
hymns_src_filepath = "./hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt"

# Must be either a ".odt" document with a single image saved in it, OR a ".png", ".jpg", or ".bmp" image????
# TODO: TEST OUT IMAGE CONVERSION WITH PILLOW, AND GET THIS WORKING.
front_cover_image_filepath = "front_cover_image.odt"