"""

GS
21 Aug. 2018

"""

import hymn_num_2_name as h

h.readFormattedHymnsFile("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt")
# h.printHymnsList()

hymn_num = 330
hymn_name = h.getHymnName(hymn_num)
print(hymn_name)

# print(h.hymns_list)