import streamlit as st
import datetime

st.title("日期时间选择器示例")

# 日期时间选择器
date = st.date_input("请选择日期", datetime.date.today())

time = st.time_input("请选择时间")

# 提交按钮
if st.button("提交"):
    st.write(f"您选择的日期为：{date}")
    st.write(f"您选择的时间为：{time}")
