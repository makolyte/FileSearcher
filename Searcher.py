import os
def Searcher(directory, keywords):
    """
    Searches through directory inside all files for the keywords.
    Outputs a list of the files that the keywords is contained in

    Note: I use this to search for references in Dynamics GP source code, much faster than searching from Dexterity
    """

    for fileName in os.listdir(directory):
        with open(os.path.join(directory, fileName), 'r') as f:
            if keywords in f.read():
                print "Found in file {0}".format(fileName)


Searcher(r"D:\Temp\GP14 Source Export", "RM Cash Posting Journal")