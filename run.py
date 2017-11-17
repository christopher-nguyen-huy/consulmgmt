from __future__  import print_function, unicode_literals, absolute_import, with_statement, generators, nested_scopes, division
from collections import OrderedDict
from base64 import b64decode, b64encode
import fileinput
import json
import re
import os

def createexportd(item,old_item=None):
	d = OrderedDict()
	d['key'] = item['key']
	d['value'] = b64decode(item['value']).decode('utf-8')
	if old_item and 'comment' in old_item:
		d['comment'] = old_item[comment]
	return d

def createimportd(item):
	d = OrderedDict()
	d['key'] = item['key']
	d['flags'] = 0
	d['value'] = b64encode(item['value'].encode()).decode('utf-8')
	return d

def export_data(outfile):
	old_data = {}
	if os.path.isfile(outfile):
		with open(outfile, 'r', encoding='utf-8') as outf:
			old_data = {item['key']:{k:v for k,v in item.items() if k != 'key'} for item in json.loads(outf.read())}
	data = [createexportd(d,old_data.get(d['key'])) for d in json.loads(''.join(line.strip() for line in fileinput.input()))]
	jsonstr = json.dumps(data, indent=4)
	print(re.sub('    ', r'\t', jsonstr))

def import_data(file):
	with open(file, 'r', encoding='utf-8') as inf:
		data = json.loads(inf.read())
	data = [createimportd(item) for item in data]
	jsonstr = json.dumps(data, indent=4)
	jsonstr = re.sub('    ', r'\t', jsonstr)
	print(jsonstr)

def main():
	import_data('outfile.json')

if __name__ == '__main__':
	main()