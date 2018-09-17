"""
extract_odts.py
- when doing `git diff` or `git difftool` with meld it would be nice to be able to diff my .odt document changes.
So, this script will extract them to this folder so they are "git diffable". It will be callable via my `git s` or 
`git statuss` local git project aliases (see ".git/config").
"""

# Internal modules
# None

# External Modules
import zipfile
import os # https://docs.python.org/dev/library/os.path.html#os.path.isdir
import shutil # High-level file/folder manipulation - https://docs.python.org/3/library/shutil.html#shutil.rmtree
import sys # for getting the system argument vector
import glob # For determining files in directories; see here: https://stackoverflow.com/a/3215392/4561887
            # Find files recursively with glob: https://stackoverflow.com/a/2186565/4561887
import xml.dom.minidom # for prettifying xml files; see my ans here: https://stackoverflow.com/a/52125645/4561887

folder = 'extracted_odts'

def extractOdts():
    print('Running Python script "{}".'.format(sys.argv[0]))
    print('Scanning current directory for .odt and .ods files...')

    # Get a list of all files in the current directory ending in .odt or .ods
    filepaths_src = glob.glob("./*.odt")
    filepaths_src += glob.glob("./*.ods")

    print('{} files found.'.format(len(filepaths_src)))

    # print('Extracting these .odt files for easier version control:') 
    # for filepath in filepaths_src:
    #     print('  "{}"'.format(filepath))

    paths_dest = []
    # print('Destination paths:')
    for path in filepaths_src:
        # Get the destination path name, which is the last element after splitting by '/', followed by replacing the 
        # "." in the extension with "_". Ex: "myfile.odt" --> "myfile_odt"
        path_dest = path.split('/')[-1]
        path_dest = path_dest[:-4] + '_' + path_dest[-3:]

        # add path prefix to front of path
        path_dest = './' + folder + '/' + path_dest
        paths_dest.append(path_dest)
        # print('  "{}"'.format(path_dest))

    # Extract (AKA uncompress, or unzip) the .odt "zip" files from source to destination
    for i in range(len(filepaths_src)):
        source_file = filepaths_src[i]
        dest_dir = paths_dest[i]

        print(('Extracting file {}: "{}"\n' +
               '  to dir "{}"').format(i+1, source_file, dest_dir))

        zip_ref = zipfile.ZipFile(source_file, 'r')
        # Delete the destination dir if it already exists
        if (os.path.isdir(dest_dir)):
            shutil.rmtree(dest_dir)
        # Extract to the destination dir
        zip_ref.extractall(dest_dir)
        zip_ref.close()

    # Re-write the XML to pretty-print it, since LibreOffice by default stores it as literally one single line in 
    # the file.
    # For all .xml files in the extracted folders, rewrite them in pretty format.

    # First, recursively find all *.xml files in "folder".
    # NB: this recursive glob method requires Python 3.5 or later. If this becomes a problem, the example at the link
    # below also offers a nice Python 2.2 to 3.4 solution which I can use instead.
    # See here (find files recursively with glob): https://stackoverflow.com/a/2186565/4561887
    filepaths_xml = glob.glob('./' + folder + '/**/*.xml', recursive=True)
    # Print & prettify all .xml files found.
    print('"Prettifying" .xml files:')
    for index, path in enumerate(filepaths_xml):
        # 1) print 
        filenum = index + 1
        if (filenum < 10):
            spaces = ' '*2
        else:
            spaces = ' '*1
        print(('  {}.' + spaces + '{}').format(filenum, path))
        
        # 2) prettify
        # Only prettify the xml if the file isn't empty (ie: its size > 0)
        # - See: https://stackoverflow.com/a/2507871/4561887 and https://docs.python.org/3/library/os.html#os.stat
        filesize_bytes = os.stat(path).st_size
        if (filesize_bytes == 0):
            spaces = ' '*6
            print(spaces + '- Skipping this file since filesize == 0 bytes...')
        else:
            # See my ans here: https://stackoverflow.com/a/52125645/4561887
            file = open(path, 'r')
            xml_string = file.read()
            file.close()
            xml_string = xml.dom.minidom.parseString(xml_string)
            xml_string_pretty = xml_string.toprettyxml()
            file = open(path, 'w') # overwrite existing file
            file.write(xml_string_pretty)
            file.close()

    print("END of custom script.\n")

if __name__ == '__main__':
    extractOdts()