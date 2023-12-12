import streamlit as st

#st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BET SHOP")
st.header('LONG QUAN')

options = st.sidebar.multiselect(
    'Bạn thích Hoa nào nè :',
    ['Hồng', 'Cúc', 'Hướng dương', 'Mâm xôi'])
