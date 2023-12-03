import streamlit as st

st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BET SHOP")
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.header("HOA NHẬP KHẨU")
    with col2:
        st.header("HOA TRONG NƯỚC")
options = st.sidebar.multiselect(
    'Bạn thích Hoa nào nè :',
    ['Hồng', 'Cúc', 'Hướng dương', 'Mâm xôi'])
