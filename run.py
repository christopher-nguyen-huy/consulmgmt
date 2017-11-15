from __future__  import print_function, unicode_literals, absolute_import, with_statement, generators, nested_scopes
from collections import OrderedDict
from base64 import b64decode
import fileinput
import json
import re

def createOrderedDict(item):
	d = OrderedDict()
	for key in ('key', 'value'):
		d[key] = b64decode(item[key]) if key == 'value' else item[key]
	return d
	

def export_data():
	data = [createOrderedDict(d) for d in json.loads(''.join(line.strip() for line in fileinput.input()))]
	print(data)
	jsonstr = json.dumps(data,indent=4)
	# print(re.sub('    ', r'\t', jsonstr))

def main():
	export_data()
	

if __name__ == '__main__':
	main()