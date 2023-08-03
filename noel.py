# -*- coding: utf-8 -*-
"""보안문자 입력 연습용+.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a97WvAUjRhXHr5qBHMC-EHmQAbZznsK4
"""

from os import writev
import random
import streamlit as st

alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','N','Z']

i = 1
alphabet = 0


st.set_page_config(
    layout="wide",
    page_title="보안문자 입력 연습",
    page_icon="🥲",
    )

st.title('보안문자 입력 연습용')

empty1,col1, empty2 = st.columns([1,5,1])

while i != 0 :
  samplelist = random.sample(alphabet_list,6)
  samplestring = ''.join(samplelist)
  print(samplestring)
  text = input('입력 : ')
  check = text.upper()
  with col1 :
    alphabet = st.subheader(samplestring)
    write = st.text_input('입력:')

  if write == samplestring :
    st.success('맞았어용')
    continue
  if write != samplestring :
    st.error('틀렸어용')
    continue