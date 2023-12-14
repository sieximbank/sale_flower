import streamlit as st

st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BEST SHOP")
#bg_image="https://images.unsplash.com/photo-1695653421371-cd48246a6200?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=grab-ftRu8P06Z5Y-unsplash.jpg"
#st.image(bg_image, caption= "Hoa Tuoi", width = 800, channels = "RGB")
#st.title("Hoa Tuoi")
tab1, tab2, tab3 = st.tabs(["Trang chủ", "Admin", "About"])

with tab1:
   st.header("HOA HUYEN HUONG FLOWERS SHOP")
   options2 =  st.sidebar.multiselect('Chon :',['Hoa Hong','Hoa Lan'])   

with tab2:
   col1,col2 = st.columns(2,gap='small')
   st.header("Upload files")
   uploaded_files = st.file_uploader("Choose a jpg file", accept_multiple_files=True)   
   for uploaded_file in uploaded_files:
      #bytes_data = uploaded_file.read()
      with col1:
         st.write("filename:", uploaded_file.name)
         st.image(uploaded_files, caption= "Hoa", width = 800, channels = "RGB")
