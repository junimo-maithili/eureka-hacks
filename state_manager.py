# state_manager.py
import streamlit as st

def init_session_state():
    if 'level' not in st.session_state:
        st.session_state.level = 0
    if 'hunger' not in st.session_state:
        st.session_state.hunger = 0
    if 'thirst' not in st.session_state:
        st.session_state.thirst = 0
    if 'happiness' not in st.session_state:
        st.session_state.happiness = 0

def increment_level():
    st.session_state.level += 1
    if st.session_state.level > 100:
        st.session_state.level = 100

def reset_stats():
    st.session_state.level = 0
    st.session_state.hunger = 0
    st.session_state.thirst = 0
    st.session_state.happiness = 0
