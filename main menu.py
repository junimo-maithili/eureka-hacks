import streamlit as st

st.markdown('''<div style="text-align: center; font-size: 36px; font-weight: bold; color: #FFFFFF; font-family: 'Tahoma', cursive;">「touch-grass.exe｣</div>''', unsafe_allow_html=True)
page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://i.redd.it/rjq8tvxntq3c1.jpeg");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

#put a backed up version of the table here

# Custom styling for a clean Tahoma button
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #00FFAA;
        color: black;
        font-size: 24px;
        padding: 15px 50px;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        font-family: 'Tahoma', sans-serif;
        cursor: pointer;
        transition: 0.2s ease-in-out;
        margin-top: 100px;
    }

    div.stButton > button:hover {
        background-color: #00dd99;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Center the actual Streamlit button using columns
col1, col2, col3 = st.columns([2, 2 ,1])
with col2:
    if st.button("ENTER"):
        st.success("Launching game... 🚀") #make this switch the state instead of this prompt

