# LibreBulletin
A bulletin for Sunday meetings of the Church of Jesus Christ of Latter-day Saints\*, using automated Python scripting to find and replace text "fields" inside a LibreOffice Writer `.odt` file.

Cross-platform! LibreBulletin relies on Python 3 and LibreOffice, both of which are free and open source, and work on virtually all major operating systems, including Windows, Mac, and Linux.

## TODO: Gif Demo

TODO: Add a gif demo "video" here, showing how easy it is to use this tool, and how the process works: `.txt` --> `.odt`.

# Features
- User-editable LibreOffice Writer `.odt` template
- Customizable user fields within `.odt` template
- Automated replacement of user fields in template with fields typed by user into easy-to-edit `.txt` file
- Automated insertion of hymn names into template, using hymn-number-to-hymn-name lookup
  - No more time wasted typing in hymn names!
  - No more misspellings or incorrect punctuation on hymn names! 
  - No more having to go to https://www.lds.org/music/library/hymns?lang=eng every week to verify hymn names and numbers!
  - You just get the hymn *number* right, and LibreBulletin will get the hymn *name* right for you!
- Automated replacement of front cover image in template (just give it a file name), including automatic scaling and positioning of new image
- Automated insertion of tabulated "Cleaning Assignment" information into a table in the template
- Automated date insertion of the date of the upcoming Sunday
- Automated conversion of the sacrament meeting schedule to "Fast Sunday" format (user can select "auto" to have the script assume the first Sunday of every month is Fast Sunday, or they can manually override this setting to force it on or off for any given Sunday)

# Details

The automated scripting includes text replacement and automatic hymn name lookup and placement into a [LibreOffice](https://www.libreoffice.org/) Writer `.odt` text document, as well as automated front cover image replacement, date insertion, Cleaning Assignment table insertion, and "Fast Sunday" format conversion. This means that you input content in the form of "fields" and "values" into a standard `.txt` text document as an input file, and the script will parse your input and perform automatic replacement of text "fields" within the `.odt` dcoument with "values" from your input `.txt` document, by matching field names in both documents and doing a find/replace on the raw (extracted) `.odt` content. It also will do hymn name lookup, looking up hymn numbers and automatically placing their corresponding hymn names into the bulletin. Parameters for the settings, including featuers such as front cover image replacement, can be found in the `config.py` file.

I'm hoping that semi-automating the bulletin like this will reduce my time required to edit the bulletin document each week from ~45 to ~15 minutes (since typing in announcements will still be done manually in the `.odt` template file).

## TODO: Screenshots

TODO: Add a few screenshots of input --> output bulletin relations (ex: image of: .odt image in + .txt inputs image = .odt image out).

# Programs
Note: for Windows, use `py -3` in place of `python3` in the commands below. For Linux, use `python3`.

## Main Code Instructions (Using & Running)
Run `python3 bulletin_find_and_replace.py` to generate a new bulletin from the `.odt` file template.  

### Instructions
 1. Open and manually format the "**ward_bulletin_template.odt**" document as desired:
   1. Insert any textual strings you'd like to become "fields".
   2. Manually update any announcements, formatting, or other non-automated parts of the template.
 2. Insert all field names and values in "**bulletin_INPUTS.txt**". Also read the instructions at the top of this document.
 3. Update "**config.py**" with paths and other variables, as required by the document.
 4. Then run `python3 bulletin_find_and_replace.py`.
 5. Your new, finalized and converted, ready-to-go LibreOffice Writer `.odt`-format bulletin will automatically open.
 6. Manually print it or export it to PDF, as desired.
 7. Done!

## Utilities

Run `python3 hymns_formatter.py` to format the "hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt" file (as manually copied from the church website) to "hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints_formatted.txt". Read the top of the "hymns_of_the_Church_of_Jesus_Christ_of_Latter-day_Saints.txt" file for instructions.

## Dependencies
To use this software, you must have:  
 * [Python 3](https://www.python.org/downloads/)
 * [Pillow](https://pillow.readthedocs.io/en/latest/installation.html) (a fork of the original "Python Image Library", or PIL)
   * Install in python3 with `python3 -m pip install Pillow`. See [here](https://stackoverflow.com/a/20061019/4561887).
   * Note: if you receive any "Permission denied" errors you may need to use "sudo": `sudo python3 -m pip install Pillow`.

# \*Disclaimer & Background
This project is not officially affiliated with the Church of Jesus Christ of Latter-day Saints. Rather, I was asked by the bishop of my local congregation (AKA: "ward") if I would be willing to make the bulletin each week for our ward as my voluntary assignment, or "calling".  After doing it for a few months, I decided that I was tired of the tedious nature of retyping information into the formatted bulletin, as it required jumping around all over the document, taking great care not to mess up formatting in the process, and having to meticulously look up the hymn numbers each week on the church website in order to be sure I type the corresponding hymn name exactly, with correct capitalization and formatting. Therefore, I decided to try to automate the process, and this is simply the result of this project I began originally for myself to speed up the weekly bulletin-creation process. 

**Once I came up with the idea, however, of using Python scripts to automate the process by treating Libre Office `.odt` docs as zip files, I realized this was something novel and unique and useful and I wanted to share it. Hence, this project was born.**

# Future Work
1. TODO: Extract out the core of the "extract .odt, read fields input text file, find, replace, rezip, open in LibreOffice" code into a new stand-alone repo, and then base this project (LibreBulletin) on that repo. Call the new repo *LibreReplace*, for instance. 
  * The benefit will be that it will get a lot more visibility and impact a lot more people that way. Think about it. LibreBulletin might only apply to 0.01% of 1% of the world (if that), but LibreReplace might eventually apply to 1% of the world. That’s a 100~1000 fold increase!
2. TODO: Eventually add an interface to interact with the Google Docs API and scrape bulletin information straight out of Google Docs! The ward uses Google Docs spreadsheets to track information, and although it would still require proofreading for spelling, grammar, capitalization, etc, it would be super nice to have automate the process of scraping information out of the doc and into a standard `.txt` file. Then, I could manually review and edit the `.txt` file, and run my script as normal to copy that `.txt` file information into the `.odt` bulletin document. Potential resources:
  * Google search for "[python read from google docs spreadsheets](https://www.google.com/search?q=python+read+from+google+docs+spreadsheets&oq=python+read+from+google+docs+spreadsheets&aqs=chrome..69i57.10710j1j4&sourceid=chrome&ie=UTF-8)"
  * Looks super useful: https://www.makeuseof.com/tag/read-write-google-sheets-python/
  * Official Google Sheets "Python Quickstart" guide: https://developers.google.com/sheets/api/quickstart/python

# Author
By Gabriel Staples  
https://www.ElectricRCAircraftGuy.com  

# License
See "LICENSE.txt"

# Version History
**Description**
* The version number is stored in the variable `VERSION` in "config.py".
* Use Semantic Versioning (https://semver.org/spec/v2.0.0.html).
* Follow a version format similar to this project's: https://github.com/NicoHood/HID/blob/master/Readme.md.
* Format: `Major.Minor.Patch (yearMonthDay)`; Date example: `20180905` is 5 Sept. 2018.

**0.2.0 (20180905)**
* First release; the code works! But if you have more than one image/photo inside the bulletin template, the automatic replacement of the photo is buggy and inconsistent.
* Many features are still left to implement. 
* However, at this point I'm starting to use this code in my actual weekly bulletin generation, and it works and definitely speeds up the process!

**0.1.0 (Skipped--not released)**





