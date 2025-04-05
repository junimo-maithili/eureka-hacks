# state_manager.py
import streamlit as st

def init_session_state():
    if 'level' not in st.session_state:
        st.session_state.level = 0
    if 'hunger' not in st.session_state:
        st.session_state.hunger = 30
    if 'thirst' not in st.session_state:
        st.session_state.thirst = 30
    if 'happiness' not in st.session_state:
        st.session_state.happiness = 30
    if 'currency' not in st.session_state:
        st.session_state.currency = 30

