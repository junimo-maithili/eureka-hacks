import streamlit as st
import mainfile
from mainfile import bars



with st.container(height=220):
    level_bar = st.progress(st.session_state.level, text="Level: %i" % st.session_state.level)
    hunger_bar = st.progress(st.session_state.hunger,text="Hunger: %i" %st.session_state.hunger)
    thirst_bar = st.progress(st.session_state.thirst,text="Thirst: %i" %st.session_state.thirst)
    happiness_bar = st.progress(st.session_state.happiness,text="Happiness: %i" %st.session_state.happiness)

def Increment():
    st.session_state.level += 1
    # You can limit the thirst value to a maximum (e.g., 100) for the progress bar
    if st.session_state.level > 100:
        st.session_state.level = 100  # Set maximum value to 100

st.button('Increment Counter', on_click=Increment)

# Optionally, create a button to reset the counter
if st.button('Reset Counter'):
    st.session_state.counter = 0  # Reset the counter
    st.session_state.thirst = 0   # Reset the thirst
