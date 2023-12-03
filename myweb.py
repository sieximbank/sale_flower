import streamlit as st

with st.sidebar:
    selected = option_menu("Main Menu", ["Trang chủ", 'Giới thiệu'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    #selected
        
#st.write("HƯƠNG - HUYỀN FLOWERS SHOP")
#        # app = st.sidebar(
