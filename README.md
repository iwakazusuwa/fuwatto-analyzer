# fuwatto-analyzer

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


求人票やスカウト文の「ふわっと感」や「本気度」を可視化する Python/Streamlit ツールです。

## 対象者
- Python と Streamlit が使える方
- スカウト文の「ふわっと感」をざっくり把握したい方
- 求人票の具体性や本気度を簡単に可視化したい方
- 辞書を差し替えて、自分オリジナルの判定ルールを作りたい方

## 概要
このツールは、求人票やスカウト文に含まれる「ふわっとした表現」や「本気度」を定量的に評価し、
可視化することを目的としています。
これにより、企業のメッセージの明確さや誠実さを評価し、求職者がより適切な選択をできるよう支援します。

- スカウト文の「ふわっと感」をざっくり把握したい  
- 求人票の具体性や本気度を簡単に可視化したい  
- 辞書を差し替えて、自分オリジナルの判定ルールに対応したい  

---

## 特徴
- 辞書を用いた「ふわっと度」と「本気度」のスコアリング
- CSV形式の辞書をアップロードしてカスタマイズ可能
- 分析結果を棒グラフで可視化（Streamlit対応）
- 単語ごとのスコアも確認可能
---

## インストール

```bash
git clone https://github.com/iwakazusuwa/fuwatto-analyzer.git
cd fuwatto-analyzer
pip install -r requirements.txt
```

## 実行
```
streamlit run fuwatto-analyzer.py
```

## 使い方
1. word_dict_filtered.csv をデフォルト辞書として使用するか、独自CSVをアップロード
2. Streamlit UIのテキストエリアに分析したい文章を貼り付け
3. 「スコア計算」ボタンをクリック
4. 分析結果一覧と棒グラフでふわっと度／本気度を確認

## CSV辞書フォーマット

| 判定   | ワード     | スコア |
| ---- | ------- | --- |
| ふわっと | 夢       | 0.9 |
| ふわっと | 自由      | 0.8 |
| ふわっと | ワクワク    | 0.9 |
| 本気   | Node.js | 0.8 |
| 本気   | テスト自動化  | 0.9 |
| 本気   | 開発プロセス  | 0.8 |

- スコアは 0.1〜1 で数字が大きいほど「ふわっと度／本気度」が強い
- 新しいワードは随時追加可能


## 今後の展望
- 辞書の精度向上による判定精度アップ
- UI改善や自動辞書生成機能
- 分析対象や辞書を自由に拡張できるように進化予定


## 貢献方法
プロジェクトへの貢献は以下の方法で歓迎します：
- バグ報告や機能追加の提案は Issues を通じて行ってください。
- コードの改善や新機能の追加は Pull Request を作成してください。
- ドキュメントの改善や翻訳も歓迎します。

## LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)
