import streamlit as st

st.write("HUYỀN - HƯƠNG FLOWERS SHOP - THE BEST SHOP")
#bg_image="https://images.unsplash.com/photo-1695653421371-cd48246a6200?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=grab-ftRu8P06Z5Y-unsplash.jpg"
#st.image(bg_image, caption= "Hoa Tuoi", width = 800, channels = "RGB")
#st.title("Hoa Tuoi")
with st.sidebar:
	selected = option_menu("Main Menu", ["Home", "Admin"], 
	    icons=['house','gear'], 
	    menu_icon="cast", default_index=0,
	    styles={
	        "container": {"padding": "0!important", "background-color": "#fafafa"},
	        "icon": {"color": "blue", "font-size": "14px"}, 
	        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
	        "nav-link-selected": {"background-color": "green"},})
