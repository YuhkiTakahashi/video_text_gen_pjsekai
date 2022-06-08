# Step 3: 動画ファイルのみ処理を行うようにする

import os

def main():

	# 指定ディレクトリ内のファイル名リストを取得
	filename_list = os.listdir(path='./videos')
	# print(filenames)

	# ファイル名ごとに処理を行うループ
	for filename in filename_list:
		
		# 動画ファイルでなければスキップ
		if not filename.endswith('.mov'): continue
		print(filename)

main()