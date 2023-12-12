import streamlit as st

st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BEST SHOP")

page_bg_image = """
<style>
[data-testid="stAppViewContainer"]{
background_image: url("https://unsplash.com/photos/I2UR7wEftf4"
}
</style>
"""
st.markdown(page_bg_image, unsafe_allow_html=True)
st.title("Flower Shop")
