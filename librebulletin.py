import config_master

# import log
# log.open()
#########replace all print()s with log.logPrint()

print("Running Librebulletin Version {}.".format(config_master.VERSION))
print("See project at https://github.com/ElectricRCAircraftGuy/LibreBulletin for more info.\n")

import bulletin_find_and_replace
bulletin_find_and_replace.main()

# log.close()