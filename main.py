import os, csv, difflib

from setting import *
from dicts import *
from templates import *

def main():

	# Load songs CSV
	with open(FILE_CSV_SONGS) as songs_csv:
		song_dict_list = [song_dict for song_dict in csv.DictReader(songs_csv)]

	# Get filenames in video directory
	filename_list = os.listdir(path=DIR_VIDEOS)

	# Loop for each files
	for filename in filename_list:
		print('========================================')
		print('Loding:', filename)

		# Skip if file is not .mov
		if not filename.endswith('.mov'):
			print('Skipped: This file is not .mov')
			continue

		# Get body filename by remove extension from filename
		filename_body = os.path.splitext(filename)[0]

		# Get data by splitted body filename
		data = filename_body.split('_')

		# Skip if number of data is less than 3
		if len(data) < 3:
			print('Skipped: Data from filename is less than 3')
			continue

		# Data to named variables
		data_song, data_level, data_singers = data

		# Skip if level initial is not in dictionary
		if not data_level in DICT_LEVELS.keys():
			print('Skipped: Level initial is not in dictionary')
			continue

		# Get level label
		level = DICT_LEVELS[data_level]

		# Make singer list
		singer_list = []
		for index in range(len(data_singers)):
			data_singers_sliced = data_singers[index:]
			for singer_key in DICT_SINGERS.keys():
				if data_singers_sliced.startswith(singer_key):
					singer_list.append(DICT_SINGERS[singer_key])
		
		# Join singer list to one string
		singers = '、'.join(singer_list)

		# Get difficulty
		difficulty = 0
		for song_dict in song_dict_list:
			song_diffratio = difflib.SequenceMatcher(a=data_song, b=song_dict['title']).ratio()
			if song_diffratio > .5:
				difficulty = song_dict[DICT_LEVELS_KEY[data_level]]
				break

		print('Song:', data_song)
		print('Level:', level)
		print('Difficulty:', difficulty)
		print('Singer(s):', singers)

		# Name new filename
		filename_renamed = TEMPLATE_FILENAME
		filename_renamed = filename_renamed.replace('{SONG}', data_song)
		filename_renamed = filename_renamed.replace('{LEVEL}', level)
		filename_renamed = filename_renamed + '.mov'

		# Make description text
		descriptions = TEMPLATE_DESCRIPTIONS
		descriptions = descriptions.replace('{SONG}', data_song)
		descriptions = descriptions.replace('{LEVEL}', level)
		descriptions = descriptions.replace('{DIFFICULTY}', difficulty)
		descriptions = descriptions.replace('{SINGERS}', singers)

		# Write textfile
		textfile_name = filename_body+'.txt'
		textfile_path = os.path.join(DIR_TEXTS, textfile_name)
		textfile = open(textfile_path, 'w')
		textfile.write(descriptions)
		textfile.close()
		print('Saved:', textfile_path)

		# Rename video file
		target_file_path = os.path.join(DIR_VIDEOS, filename)
		rename_file_path = os.path.join(DIR_VIDEOS, filename_renamed)
		os.rename(target_file_path, rename_file_path)
		print('Renamed:', rename_file_path)

main()

# Code: ©︎ Yuhki Takahashi