import streamlit as st
import pandas as pd

df = pd.DataFrame(data={"col1":[100,200,300],
                   "col2":['aa','bb','cc']})

st.write(df)
st.dataframe(df)
st.table(df)

# JSON 데이터 출력
st.json({'name':'홍길동', 'age':22, 'gender':'male'})

# Metric() 함수를 이용한 데이터 출력(변화가 있는 데이터)
st.metric(label='온도', value='13℃', delta='3℃')
st.metric(label='카카오뱅크', value='55,000', delta='-1,000')

# 이미지 데이터
st.image("cat.jpg", width=400)