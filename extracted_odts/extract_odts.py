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

        # Do the zip file stuff!
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
    # NB: this recursive glob method requires Python 3.5 or later. 
    # See here (find files recursively with glob): https://stackoverflow.com/a/2186565/4561887
    filepaths_xml = glob.glob('./' + folder + '/**/*.xml', recursive=True)
    # TODO: NOW MAKE THEM PRETTY! See here: https://stackoverflow.com/a/1206856/4561887


    print("Done.\n")

if __name__ == '__main__':
    extractOdts()