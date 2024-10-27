import sys
import json
import nbformat
from pathlib import Path

def translate_notebook(input_path):
    # 入力ファイルのパスから出力ファイルのパスを生成
    input_path = Path(input_path)
    output_path = input_path.parent / f"{input_path.stem}_ja{input_path.suffix}"
    
    # ノートブックを読み込む
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # 各セルの内容を翻訳
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            # ここでDeepLなどの翻訳APIを使用して翻訳する代わりに
            # 今回は日本語訳のためのコメントを追加
            cell.source = f"""[Japanese translation needed]
Original text:
{cell.source}"""
    
    # 翻訳したノートブックを保存
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    return output_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translate_notebook.py <input_notebook_path>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = translate_notebook(input_path)
    print(f"Created Japanese version: {output_path}")