# Step 9: 歌手データから歌手リストを作る

# 譜面分類辞書
DICT_DIFFICULTIES = {
	'E': 'EASY',
	'N': 'NORMAL',
	'H': 'HARD',
	'X': 'EXPERT',
	'M': 'MASTER',
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
			print(data_singers_sliced)

			## スライスの先頭が 'Mik' であれば、歌手リストに 'ミク' を加える
			# if data_singers_sliced.startswith('Mik'):
			# 	print('* MIKU IN SINGERS')
			# 	singer_list.append('ミク')

			## 歌手辞書のすべてのキーのforループ
			for singer_key in DICT_SINGERS.keys():
				## スライスの先頭がキーと一致していれば、歌手リストに歌手辞書の対応する値を加える
				if data_singers_sliced.startswith(singer_key):
					print(f'* {DICT_SINGERS[singer_key]} IN SINGERS')
					singer_list.append(DICT_SINGERS[singer_key])

		## 完成した歌手リスト
		print('歌手リスト:', singer_list)

		# print('曲名: '+data_song)
		# print('譜面分類: '+difficulty)
		# print('歌: '+data_singers)

main()