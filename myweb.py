import streamlit as st

st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BET SHOP")

options = st.sidebar.multiselect(
    'Bạn thích Hoa nào nè :',
    ['Hồng', 'Cúc', 'Hướng dương', 'Mâm xôi'])
