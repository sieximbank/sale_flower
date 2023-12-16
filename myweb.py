import streamlit as st
from PIL import Image
#from streamlit_option_menu import option_menu
#st.set_page_config(layout="wide")
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.header("HUYỀN - HƯƠNG FLOWERS SHOP - THE BEST SHOP")

#with st.sidebar:
#    selected = option_menu("Main Menu", ["Home", 'Admin','About'], 
#        icons=['house', 'gear'], menu_icon="cast", default_index=1)
#    selected

   #uploaded_files = st.file_uploader("Choose a jpg file", accept_multiple_files=True)   
   #for uploaded_file in uploaded_files:
      #bytes_data = uploaded_file.read()
      #with col1:
      #   st.write("filename:", uploaded_file.name)
      #   st.image(uploaded_files, caption= "Hoa", width = 800, channels = "RGB")

#tab1, tab2, tab3 = st.tabs(["Home", "Admin", "About"])
#with tab1:

st.sidebar.multiselect("Chọn hoa",['Hoa Hồng','Hoa Lan','Hoa Nhập Khẩu'])
#st.sidebar.multiselect("Chọn Loại",['Nhập khẩu','Trong nước'])
#https://drive.google.com/file/d/1ePE3SQzf1SVip928h70QoYm6JXFqhmHi/view?usp=sharing
#col1,col2,col3 = st.columns(3,gap='small')
container = st.container()
#container.write("Hình nền")   
container.image("https://images.pexels.com/photos/250591/pexels-photo-250591.jpeg")

        
