# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import streamlit as st
import pandas as pd
import re
import time
import altair as alt

# -----------------------------
# 1️⃣ CSV辞書読み込み or アップロード
# -----------------------------
st.set_page_config(layout="wide")
st.title("ふわっと判定くん")

st.markdown("""
- 複数文章は空行で区切って貼り付けてください  
- 単語ごとのスコア内訳と棒グラフも表示します  
- スコア計算ボタンで明示的に分析開始
""")

uploaded_file = st.file_uploader("辞書CSVをアップロード", type="csv")

if uploaded_file is not None:
    df_dict = pd.read_csv(uploaded_file, encoding="utf-8-sig", dtype={'ワード': str})
else:
    df_dict = pd.read_csv("word_dict_filtered.csv", encoding="utf-8-sig", dtype={'ワード': str})

fuwatto_dict = dict(zip(df_dict[df_dict['判定']=='ふわっと']['ワード'],
                        df_dict[df_dict['判定']=='ふわっと']['スコア']))
honki_dict = dict(zip(df_dict[df_dict['判定']=='本気']['ワード'],
                      df_dict[df_dict['判定']=='本気']['スコア']))

# -----------------------------
# 2️⃣ 文章分析関数
# -----------------------------
def analyze_text_whole(text):
    text_lower = text.lower()
    f_score = sum(score for word, score in fuwatto_dict.items() if word.lower() in text_lower)
    g_score = sum(score for word, score in honki_dict.items() if word.lower() in text_lower)
    total = f_score + g_score
    if total < 0.1:
        f_ratio = 0
        g_ratio = 0
    else:
        f_ratio = f_score / total
        g_ratio = g_score / total
    return f_ratio, g_ratio, f_score, g_score

def word_score_breakdown_whole(text):
    text_lower = text.lower()
    f_words = [(word, fuwatto_dict[word]) for word in fuwatto_dict if word.lower() in text_lower]
    g_words = [(word, honki_dict[word]) for word in honki_dict if word.lower() in text_lower]
    return f_words, g_words

# -----------------------------
# 3️⃣ Streamlit UI
# -----------------------------
user_text = st.text_area("分析したい文章を貼り付けてください", height=200)

if st.button("スコア計算"):
    if user_text.strip() == "":
        st.warning("文章を入力してください")
    else:
        texts = re.split(r'\n{2,}', user_text)
        results = []
        total_f = 0
        total_g = 0

        progress_bar = st.progress(0)
        status_text = st.empty()
        status_text.text("分析中です…少々お待ちください")

        for i, t in enumerate(texts):
            f_ratio, g_ratio, f_score, g_score = analyze_text_whole(t)
            f_words, g_words = word_score_breakdown_whole(t)

            # 累計スコアが0.1未満の文章は非表示
            if f_score + g_score < 0.1:
                continue

            results.append({
                "文章": t,
                "ふわっと比率": f"{f_ratio*100:.1f}%",
                "本気比率": f"{g_ratio*100:.1f}%",
                "ふわっと累計": f_score,
                "本気累計": g_score,
                "ふわっと単語": ", ".join([f"{w}({s})" for w, s in f_words]),
                "本気単語": ", ".join([f"{w}({s})" for w, s in g_words])
            })
            total_f += f_score
            total_g += g_score

            progress_bar.progress((i+1)/len(texts))
            time.sleep(0.05)

        status_text.text("分析完了 ✅")

        df_results = pd.DataFrame(results)
        st.subheader("分析結果一覧（比率＆累計スコア）")
        st.dataframe(df_results)

        st.subheader("全文章合計スコア")
        st.write(f"ふわっと累計スコア: {total_f:.2f}")
        st.write(f"本気累計スコア: {total_g:.2f}")


