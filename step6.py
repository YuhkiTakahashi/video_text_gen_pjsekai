# Step 6: 各データに名前をつける

import os

def main():

	# 指定ディレクトリ内のファイル名リストを取得
	filename_list = os.listdir(path='./videos')
	# print(filenames)

	# ファイル名ごとに処理を行うループ
	for filename in filename_list:

		# 動画ファイルでなければスキップ
		if not filename.endswith('.mov'): continue
		# print(filename)

		# ファイル名本体を取得する（ファイル名から拡張子を取り除く）
		filename_body = os.path.splitext(filename)[0]
		# print(filename_body)

		# ファイル名から動画投稿用データを取得する（ファイル名本体を指定文字で区切る）
		data = filename_body.split('_')
		print(data)

		# 各データを変数にする
		data_song, data_difficulty, data_singers = data
		print('曲名: '+data_song)
		print('譜面分類: '+data_difficulty)
		print('歌: '+data_singers)

main()