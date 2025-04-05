import streamlit as st
import mainfile
from mainfile import bars



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

with st.container(height=220):
    level_bar = st.progress(st.session_state.level, text="Level: %i" % st.session_state.level)
    hunger_bar = st.progress(st.session_state.hunger,text="Hunger: %i" %st.session_state.hunger)
    thirst_bar = st.progress(st.session_state.thirst,text="Thirst: %i" %st.session_state.thirst)
    happiness_bar = st.progress(st.session_state.happiness,text="Happiness: %i" %st.session_state.happiness)
