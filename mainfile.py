import streamlit as st
import state_manager

state_manager.init_session_state()


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Title")


def bars():    
    if 'counter' not in st.session_state:
        st.session_state.level = 0
        st.session_state.hunger = 0
        st.session_state.thirst = 0
        st.session_state.happiness = 0

