import streamlit as st
import base64

st.markdown("""# Welkom op het dashboard van steam groep 4! 😊\n
               ## Zie aan de linkerkant onze pagina's, en veel plezier.""")
st.sidebar("""# Hoofdpagina""")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Assets/SteamBG.png')
