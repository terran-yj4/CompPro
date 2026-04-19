#!/bin/sh
# 新しいmk.sh > sh mk.shで今日の日付のフォルダを作成してくれる
dir=$(date +%y%m%d)


mkdir -p "./atcoder/$dir" || { echo "ディレクトリ作成に失敗しました: ./atcoder/$dir"; exit 1; }

for f in a.py b.py c.py d.py e.py; do
  file="./atcoder/$dir/$f"
  if [ -f "$file" ]; then
    echo "ファイルがすでに存在します: $file"
    continue
  fi
  cp temp.py "$file"
  chmod +x "$file"
  echo "作成しました: $file"
done
