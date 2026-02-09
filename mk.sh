#!/bin/sh

if [ -z "$1" ]; then
  echo "使用法: sh mk.sh <dir_name>"
  exit 1
fi

dir="$1"


mkdir -p "./atcoder/$dir" || { echo "ディレクトリ作成に失敗しました: ./atcoder/$dir"; exit 1; }

for f in a.py b.py c.py d.py; do
  file="./atcoder/$dir/$f"
  if [ -e "$file" ]; then
    echo "既に存在します: $file"
  else
    : > "$file"
    chmod +x "$file"
    echo "作成しました: $file"
  fi
done
