import streamlit as st
from mainfile import bars
from PIL import Image




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


def Lose_money(stat_name):
    if st.session_state.currency >=10:
        st.session_state.currency -= 10
        if stat_name == 'hunger':
            st.session_state.hunger +=10
        elif stat_name == 'thirst':
            st.session_state.thirst +=10
        elif stat_name == 'happiness':
            st.session_state.happiness +=10
    else:
        st.warning("Not enough money just yet! Try going outside!")


currency_container = st.container

with currency_container(height=470):
    st.title("%i" %st.session_state.currency)
    st.write("Gain currency by leveling up! Use your currency to buy food, happiness, and thirst. Be wise with your spending...")
    st.write("Hunger: %i" % st.session_state.hunger)
    st.write("Thirst: %i" % st.session_state.thirst)
    st.write("Happiness: %i" % st.session_state.happiness)


    food, thirst, happiness = st.columns(3, vertical_alignment="bottom")


    food = st.button("Food", on_click=lambda: Lose_money('hunger'))
    thirst = st.button("Thirst", on_click=lambda: Lose_money('thirst'))
    happiness = st.button("Happiness", on_click=lambda: Lose_money('happiness'))




left, center, right = st.columns([2, 3, 1])
with center:
    image = Image.open("fox.png")
    st.image(image, use_container_width=False, width=300)
