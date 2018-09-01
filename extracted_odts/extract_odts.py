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
import sys

def extractOdts():
    print('Running Python script "{}".'.format(sys.argv[0]))

    # TODO: WRITE CODE TO HAVE IT SCAN THE DIRECTORY AND AUTOMATICALLY IDENTIFY ALL .ODT FILES
    filepaths_src = [
        './ward_bulletin_template.odt', 
        './automated ward bulletin scripts - what to work on next - Gabriel.odt'
    ]

    # print('Extracting these .odt files for easier version control:') 
    # for filepath in filepaths_src:
    #     print('  "{}"'.format(filepath))

    paths_dest = []
    # print('Destination paths:')
    for path in filepaths_src:
        # Get the destination path name, which is the last element after splitting by '/', minus
        # the last 4 chars, which are the extension ('.odt')
        path_dest = path.split('/')[-1][:-4]
        # add './' to front of path
        path_dest = './extracted_odts/' + path_dest
        paths_dest.append(path_dest)
        # print('  "{}"'.format(path_dest))

    # Extract (AKA uncompress, or unzip) the .odt "zip" files from source to destination
    for i in range(len(filepaths_src)):
        source_file = filepaths_src[i]
        dest_dir = paths_dest[i]

        print(('Extracting file "{}"\n' +
               '  to dir "{}"').format(source_file, dest_dir))

        zip_ref = zipfile.ZipFile(source_file, 'r')
        # Delete the destination dir if it already exists
        if (os.path.isdir(dest_dir)):
            shutil.rmtree(dest_dir)
        # Extract to the destination dir
        zip_ref.extractall(dest_dir)
        zip_ref.close()

    print("Done.\n")

if __name__ == '__main__':
    extractOdts()