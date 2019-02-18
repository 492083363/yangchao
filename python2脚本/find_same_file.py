#!/usr/bin/python
#coding=utf-8
#查找重复的文件
from __future__ import print_function
import sys
import hashlib
import os
import fnmatch

CHUNK_SIZE=8192
def is_file_match(filename,patterns):
	for pattern in patterns:
		if fnmatch.fnmatch(filename,pattern):
			return True
	return False

def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
	for root,dirnames,filenames in os.walk(root):
		for filename in filenames:
			if is_file_match(filename,patterns):
				yield os.path.join(root,filename)
				for d in exclude_dirs:
					if d in dirnames:
						dirnames.remove(d)	

def get_chunk(filename):
	with open(filename) as f:
		while True:
			chunk=f.read(CHUNK_SIZE)
			if not chunk:
				break
			else:
				yield chunk


def get_file_checksum(filename):
	h=hashlib.md5()
	for chunk in get_chunk(filename):
		h.update(chunk)
	return h.hexdigest()

def main ():
	sys.argv.append("")
	directory=sys.argv[1]
	if not os.path.isdir(directory):
		raise SystemExit ("{0} is not a directory".format(directory))
		 
	record={}
	for item in find_specific_files(directory):
		checksum=get_file_checksum(item)
		if checksum in record:
			print ('find duplicate files: {0} vs {1}'.format(record[checksum],item))
		else:
			record[checksum]=item

if __name__ == '__main__':
	main()
