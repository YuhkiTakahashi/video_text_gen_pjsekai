# Step 15: 概要欄用テキストをtxtファイルに保存

# 譜面分類辞書
DICT_DIFFICULTIES = {
	'E': 'EASY',
	'N': 'NORMAL',
	'H': 'HARD',
	'X': 'EXPERT',
	'M': 'MASTER',
}

# 譜面分類キー辞書
DICT_DIFFICULTIES_KEY = {
	'E': 'level_easy',
	'N': 'level_normal',
	'H': 'level_hard',
	'X': 'level_expert',
	'M': 'level_master',
}

# 歌手辞書
DICT_SINGERS = {
	'Mik': 'ミク',   'Rin': 'リン',   'Len': 'レン',
	'Luk': 'ルカ',   'Mei': 'MEIKO',  'Kai': 'KAITO',

	'Ich': '一歌',   'Sak': '咲希',   'Hon': '穂波',   'Sih': '志歩',
	'Min': 'みのり', 'Har': '遥',     'Air': '愛莉',   'Siz': '雫',
	'Koh': 'こはね', 'Ann': '杏',     'Aki': '彰人',   'Toy': '冬弥',
	'Tsu': '司',     'Emu': 'えむ',   'Nen': '寧々',   'Rui': '類',
	'Kan': '奏',     'Maf': 'まふゆ', 'Ena': '絵名',   'Miz': '瑞希',

	'Ins': '-',      'Gum': 'GUMI',   'Flo': 'flower',
}

# ファイル名テンプレート
TEMPLATE_FILENAME = '【#プロセカ】{SONG} 🎼{DIFFICULTY}【Project SEKAI: COLORFUL STAGE!】プレイ映像'

# 概要欄用テキストテンプレート
TEMPLATE_DESCRIPTIONS = '''🎮Project SEKAI: COLORFUL STAGE! feat. 初音ミク
💿{SONG} 🎼{DIFFICULTY} (Lv. {LEVEL}) 🎤{SINGERS}

《プロジェクトセカイ カラフルステージ！ feat. 初音ミク》
© SEGA / © Colorful Palette Inc. / © Crypton Future Media, INC. www.piapro.net piapro All rights reserved.'''

import os, csv, difflib

def main():

	# 楽曲情報CSVから楽曲情報辞書リストを作る
	with open('./songs.csv') as songs_csv:
		song_dict_list = [song_dict for song_dict in csv.DictReader(songs_csv)]

	# for song_dict in song_dict_list: print(song_dict)

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
		# print(data)

		# 各データを変数にする
		data_song, data_difficulty, data_singers = data
		# print('曲名:', data_song)
		# print('譜面分類:', data_difficulty)
		# print('歌:', data_singers)

		# 譜面分類データと譜面分類辞書から名詞を呼び出す
		difficulty = DICT_DIFFICULTIES[data_difficulty]

		# 歌手データを読み取り歌手リストを作る
		singer_list = []
		
		## 歌手データの文字数と等しい回数のループ（rangeを使用）
		# print('歌手データ文字数:', len(data_singers))
		# print('歌手データ文字数 range:', range(len(data_singers)))
		# print('歌手データ文字数 range list:', list(range(len(data_singers))))

		for index in range(len(data_singers)):

			## 歌手データ文字列の、指定indexから末尾までのスライスを作る
			data_singers_sliced = data_singers[index:]
			# print(data_singers_sliced)

			## スライスの先頭が 'Mik' であれば、歌手リストに 'ミク' を加える
			# if data_singers_sliced.startswith('Mik'):
			# 	print('* MIKU IN SINGERS')
			# 	singer_list.append('ミク')

			## 歌手辞書のすべてのキーのforループ
			for singer_key in DICT_SINGERS.keys():
				## スライスの先頭がキーと一致していれば、歌手リストに歌手辞書の対応する値を加える
				if data_singers_sliced.startswith(singer_key):
					# print(f'* {DICT_SINGERS[singer_key]} IN SINGERS')
					singer_list.append(DICT_SINGERS[singer_key])

		## 完成した歌手リスト
		# print('歌手リスト:', singer_list)

		# 歌手リストの各文字列をひとつの文字列に連結する
		singers = '、'.join(singer_list)

		# 難易度を取得
		## 一致がなかった場合の値を設定
		level = 0
		for song_dict in song_dict_list:
			## 曲名データと楽曲情報辞書内の曲名の近似値が一定以上か判定
			song_diffratio = difflib.SequenceMatcher(a=data_song, b=song_dict['title']).ratio()
			if song_diffratio > .5:
				# level = song_dict['level_master'] # 仮にMASTERの難易度を取得
				# 楽曲情報辞書内の対象の難易度を取得
				level = song_dict[DICT_DIFFICULTIES_KEY[data_difficulty]]
				break

		# print('曲名:', data_song)
		# print('譜面分類:', difficulty)
		# print('譜面難易度:', level)
		# print('歌:', singers)

		# 変更後の動画ファイル名を作る
		## ファイル名テンプレートを呼び出し
		filename_renamed = TEMPLATE_FILENAME
		## テンプレート内の対象部分を各種文字列に置き換え、末尾に拡張子を付与
		filename_renamed = filename_renamed.replace('{SONG}', data_song)
		filename_renamed = filename_renamed.replace('{DIFFICULTY}', difficulty)
		filename_renamed = filename_renamed + '.mov'
		## 完成したファイル名
		# print(filename_renamed)

		# 概要欄用テキストを作る
		## 概要欄用テキストテンプレートを呼び出し
		descriptions = TEMPLATE_DESCRIPTIONS
		## テンプレート内の対象部分を各種文字列に置き換える
		descriptions = descriptions.replace('{SONG}', data_song)
		descriptions = descriptions.replace('{DIFFICULTY}', difficulty)
		descriptions = descriptions.replace('{LEVEL}', level)
		descriptions = descriptions.replace('{SINGERS}', singers)
		## 完成したテキスト
		# print(descriptions)

		# テキストファイルを書き出す
		## 元の動画ファイル名をテキストファイル名にする
		textfile_name = filename_body+'.txt'
		## ディレクトリパスを含めたファイルパスを作る
		textfile_path = './texts/'+textfile_name
		## ファイルを生成し、開き、テキストを書き込み、閉じる
		textfile = open(textfile_path, 'w')
		textfile.write(descriptions)
		textfile.close()
		print('保存完了:', textfile_path)

main()