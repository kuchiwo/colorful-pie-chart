import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("カラフル円グラフジェネレーター")

st.write("以下のスライダーで項目数を選んでください")

num_sections = st.slider("項目数", min_value=2, max_value=10, value=5)

# ランダムな割合とラベルを作成
values = np.random.rand(num_sections)
values /= values.sum()
labels = [f"case {i+1}" for i in range(num_sections)]

# グラフ描画
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")

st.pyplot(fig)
