import streamlit as st
from PIL import Image
import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests



html_page = """
<div style="background-color:pink; padding:50px">
<p style="color:white; font-size:50px">Balloons 버튼을 눌러요!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

st.divider()

if st.button("Balloons"):
    st.balloons()

st.markdown("---")
# 이미지 불러오기
from pathlib import Path

BASE_DIR = Path(__file__).parent
img_path = BASE_DIR / 'imgs' / '하마.png'
img = Image.open(img_path)
st.image(img, width=300, caption="나")


# 유튜브 url도 포함 가능
st.video("https://www.youtube.com/watch?v=gnmdTgYaa28&list=RDgnmdTgYaa28&start_radio=1")

st.markdown("---")

html_page = """
<div style="background-color:pink; padding:50px">
<p style="color:white; font-size:50px">Play 버튼을 차례로 눌러요!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

st.markdown("---")

if st.button("Play1"):
    st.text("안녕 지은!")

if st.button("Play2"): # Play2 버튼을 클릭하면
    st.text("수술 후유증에서 회복했나요?")

st.markdown("---")

html_page = """
<div style="background-color:pink; padding:50px">
<p style="color:white; font-size:50px">Checkbox 버튼을 눌러요!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

st.markdown("---")

if st.checkbox("Checkbox"): # 체크박스 버튼을 클릭하면
    st.text("오늘 하고 싶은 일")

radio_but = st.radio("A,B 중 고르세요", ["A", "B"])
if radio_but == "A":
    st.info("점심 같이 먹기") # A 라디오 버튼을 클릭하면. 선택지가 둘 이상 일때
else:
    st.info("영화 같이 보기")



lunch = st.selectbox("먹고 싶은 점심은?", ["칼국수", "짜장면", "냉면"])

movie = st.multiselect("보고 싶은 영화는?(다수 선택 가능)",
                            ["프라다", "마이클", "헤일메리", "살목지"])

st.divider()

title = st.text_input("영화 감상평", "Write something…")
st.text(title)

select_val = st.slider("평점", 1, 10)













