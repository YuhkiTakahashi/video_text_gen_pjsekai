# Step 1: 動画フォルダ内のファイル名を読み取る

import os

def main():
	
	# 指定ディレクトリ内のファイル名リストを取得
	filename_list = os.listdir(path='./videos')
	print(filename_list)

main()