# LibreBulletin
A bulletin for Sunday meetings of the Church of Jesus Christ of Latter-day Saints\*, using automated Python scripting.

# Details
The automated scripting includes text replacement and automatic hymn name lookup and placement into a [LibreOffice](https://www.libreoffice.org/) Writer `.odt` text document. This means that you input content in the form of "fields" and "values" into a standard `.txt` text document as an input file, and the script will parse your input and perform automatic replacement of text "fields" within the `.odt` dcoument with "values" from your input `.txt` document, by matching field names in both documents and doing a find/replace on the raw (extracted) `.odt` content. It also will do hymn name lookup, looking up hymn numbers and automatically placing their corresponding hymn names into the bulletin. 

I'm hoping that semi-automating the bulletin like this will reduce my time required to edit the bulletin document each week from ~45 to ~15 minutes.

## TODO: Gif Demo

TODO: Add a gif demo "video" here, showing how easy it is to use this tool, and how the process works: `.txt` --> `.odt`.

## TODO: Screenshots

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





