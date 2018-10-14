THIS_FILENAME = 'log.py'

# local imports
import config_master
import date

# external imports
import sys
import os
import errno

# # TO BE DONE LATER, IF STILL NEEDED.
# # If log file < this many lines, append to log file, otherwise we will create a new one.
# MAX_LINES_IN_LOG_FILE = 10000
# def getNumLinesInFile(filepath):
#     """
#     Return the number of lines in a file.
#     References:
#     - Question where this code comes from: https://stackoverflow.com/q/845058/4561887.
#     - enumerate() documentation: https://docs.python.org/3/library/functions.html#enumerate
#     - enumerate: better documentation: http://book.pythontips.com/en/latest/enumerate.html
#     - enumerate: a few basic examples: https://python-reference.readthedocs.io/en/latest/docs/functions/enumerate.html
#     """
#     # TODO: HANDLE THE CASE WHERE THE FILE DOESN'T EXIST, OR IS EMPTY!
#     with open(filepath) as f:
#         for i, line in enumerate(f):
#             pass
#     return i + 1
# # count the number of lines in the log file if it already exists.
# num_lines = None
# if os.path.isfile(log_filepath):
#     num_lines = getNumLinesInFile(log_filepath)
# print('num_lines in "{}" = {}.'.format(log_filepath, num_lines))

class Log:

    def __init__(self):
        pass

    def open(self):
        """
        Open log file
        """

        # get log directory
        if config_master.demo == True:
            log_dir = "./logs"
        elif config_master.demo == False:
            log_dir = "./MY_PERSONAL_WARD_INFO"
        else:
            print('ERROR in "{}": invalid config_master.demo value of "{}". Must be "True" or "False" only.'.format(
                  THIS_FILENAME, config_master.demo))
            sys.exit()

        # get log filename and filepath
        log_filename = date.getLogFilename()
        log_filepath = log_dir + '/' + log_filename
        
        # ensure this folder exists
        # See: https://stackoverflow.com/a/12517490/4561887
        # And https://docs.python.org/3.7/library/errno.html
        if not os.path.exists(os.path.dirname(log_filepath)):
            try:
                os.makedirs(os.path.dirname(log_filepath))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    # If the error is anything but "File Exists" (https://docs.python.org/3.7/library/errno.html), raise
                    # the current exception up to a higher level
                    raise

        self.file = open(log_filepath, 'a')

    def close(self):
        self.file.close()
        print('log closed')

    def print(self, formatted_str):
        print(formatted_str)
        ######## log to file too

if __name__ == '__main__':
    log = Log()
    log.open()
    log.print("Log Opened")
    log.close()