#!/bin/sh

if [ -z "$1" ]; then
  echo "使用法: sh mk.sh <dir_name>"
  exit 1
fi

dir="$1"


mkdir -p "~/dev/comppro/$dir" || { echo "ディレクトリ作成に失敗しました: ~/dev/comppro/$dir"; exit 1; }

for f in a.py b.py c.py; do
  file="~/dev/atcoder/$dir/$f"
  if [ -e "$file" ]; then
    echo "既に存在します: $file"
  else
    : > "$file"
    chmod +x "$file"
    echo "作成しました: $file"
  fi
done
