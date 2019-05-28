<!-- -*- encoding: utf-8 -*- -->

dump_map.py
===========

画像ファイル中の文字に、utf-8 の何番を割り当てるかを指定するリスト(convlist.csv)を作成。

1. chara_conv_map.txt に、画像と対応した文字数・文字種類を、utf-8 で列挙しておく。
2. python dump_map.py を実行。
3. エラーが出なければファイル保存。python dump_map.py > convlist.csv
4. 一つ上のフォルダに convlist.csv をコピー。

Windows10 x64 1809 + Python 2.7.16 32bit で動作確認した。

