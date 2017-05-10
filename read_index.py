    

import sys

from indexer import Indexer


def get_line(source_file, index_file, line_num):
    idxr = Indexer(source_file, index_file)
    line = None
    with idxr as i:
        line =  i.read(line_num)
    print line



get_line(sys.argv[1], sys.argv[2], int(sys.argv[3]))

