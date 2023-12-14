import streamlit as st

st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BEST SHOP")
#bg_image="https://images.unsplash.com/photo-1695653421371-cd48246a6200?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=grab-ftRu8P06Z5Y-unsplash.jpg"
#st.image(bg_image, caption= "Hoa Tuoi", width = 800, channels = "RGB")
#st.title("Hoa Tuoi")
tab1, tab2, tab3 = st.tabs(["Trang chủ", "Admin", "About"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
