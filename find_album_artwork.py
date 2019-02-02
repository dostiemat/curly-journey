#!/usr/bin/env python3

import urllib.parse

BEGIN_SEPARATOR = '“'
MIDDLE_SEPARATOR = ' - '
END_SEPARATOR = '”'
SCRIPT_FILENAME = 'AlbumCoverFinder.scpt'

class string(str):
	def url(self):
		return urllib.parse.quote_plus(self)


with open(SCRIPT_FILENAME, 'w+') as out_file:
	out_file.write('tell application \"Safari\"\n')

with open('iTunes.txt', 'r') as file:
	for line in file:
		if BEGIN_SEPARATOR in line:
			info = line.split(BEGIN_SEPARATOR)[1].split(END_SEPARATOR)[0].split(MIDDLE_SEPARATOR)
			artist = string(info[0])
			album = string(info[1])
			with open(SCRIPT_FILENAME, 'a') as out_file:
				out_file.write(f"\topen location (\"https://www.google.com/search?tbm=isch&q={artist.url()}+{album.url()}\")\n")

with open(SCRIPT_FILENAME, 'a') as out_file:
	out_file.write('end tell\n')

print(f"Please run 'osascript {SCRIPT_FILENAME}'")
