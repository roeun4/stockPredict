import streamlit as st
import pandas as pd

# 버튼
# st.button('클릭')
# st.button('클릭') # 같은 버튼은 에러

# 같은 버튼 생성시 key로 구분
st.button('클릭', key=1)
st.button('클릭', key=2)
st.button('클릭', key=3, help=":red[tooltip]")

def myFunc(*args):
    res = 0
    for x in args:
        res += x
    st.write(f'계산 결과 = {res}')
    
st.button('이벤트', key=4, on_click=myFunc, args=[1,2,3])

aa = st.button('클릭', key=5)
# aa는 버튼 클릭이 안된 경우 false
if aa:
   st.write(":smile:")
else:
   st.write(":sleepy:")
''
'---'
''
x = st.checkbox('위 내용에 동의합니다')
if x:
   st.write("좋아요")

y = st.radio("메뉴 선택", ["짜장면", "짬뽕"])
st.write(f'선택메뉴 = {y}')

z = st.selectbox('선택하세요', ["짜장면", "짬뽕"])
st.write(f'선택메뉴 = {z}')

# multiselect
m = st.multiselect('후식 선택', ['커피', '아이스크림', '과일'])
st.write(f'후식 = {m}')
''
'---'
''
xx = st.select_slider("만족도?", ['매우 안좋음', '안좋음', '보통', '좋음', '매우좋음'])
st.write(f'만족도 = {xx}')

yy = st.slider("만족도?", min_value=0, max_value=10, value=5, step=1)
st.write(f'만족도 = {yy}')

zz = st.number_input("점수?", min_value=0, max_value=10, value=10, step=2)
st.write(f'점수 = {zz}')
''
'---'
''
n = st.text_input('당신의 이름은?')
d = st.date_input('약속 날짜는?')
t = st.time_input('시간은?')
st.write(f'이름 = {n}, 약속일={d}, 시간={t}')