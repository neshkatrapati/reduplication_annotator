
from bottle import route, run, template
import sys
from indexer import Indexer
import json

source_file = sys.argv[1]
index_file = sys.argv[2]
idxr = Indexer(source_file, index_file)
#i = idxr.__enter__()
i = None 
def get_line(line_num):
	#idxr = Indexer(source_file, index_file)
	line = None
	line =  i.read(line_num)
	return line




@route('/<line_num>')
def index(line_num):
    return get_line(int(line_num))


@route('/m/<line_nums>')
def index(line_nums):
    sents = []
    print line_nums
    for line_num in line_nums.split(";"):
        sents.append(get_line(int(line_num)))
    return json.dumps(sents)



with idxr as i:
	run(host='0.0.0.0', port=8080)
