"""

GS
21 Aug. 2018

"""

import hymn_num_2_name as h

hymns = h.Hymns("hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt")
hymns.printHymnsList()

# Test
hymn_num = 330
hymn_name = hymns.getHymnName(hymn_num)
print("\nTest:")
print("hymn_num = " + str(hymn_num) + "; hymn_name = \"" + hymn_name + "\"")

print()
print(hymns.getHymnsList())