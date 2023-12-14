import streamlit as st
from streamlit-option-menu import option_menu

st.header("HUYỀN - HƯƠNG FLOWERS SHOP - THE BEST SHOP")

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Admin','About'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

   #uploaded_files = st.file_uploader("Choose a jpg file", accept_multiple_files=True)   
   #for uploaded_file in uploaded_files:
      #bytes_data = uploaded_file.read()
      #with col1:
      #   st.write("filename:", uploaded_file.name)
      #   st.image(uploaded_files, caption= "Hoa", width = 800, channels = "RGB")
