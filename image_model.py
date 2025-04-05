import tensorflow as tf
import streamlit as st
import time

from keras.api.layers import DepthwiseConv2D
from keras.api import layers
from keras.api.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np



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


cooldown = False


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)


# Custom layers dictionary
custom_objects = {
    'DepthwiseConv2D': DepthwiseConv2D
}


# Define a custom wrapper for DepthwiseConv2D
class CustomDepthwiseConv2D(layers.DepthwiseConv2D):
    def __init__(self, **kwargs):
        # Remove unsupported `groups` argument if it exists
        if 'groups' in kwargs:
            if kwargs:
                kwargs.pop('groups')
        super().__init__(**kwargs)


# Register custom layer
custom_objects = {
    'DepthwiseConv2D': CustomDepthwiseConv2D
}

# Load the model with custom layer handling
model = load_model("converted_keras/keras_Model.h5", compile=False, custom_objects=custom_objects)

# Load the labels
class_names = open("converted_keras/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(1)

img_file_buffer = st.camera_input(f"Take a picture!")




while True:

    if img_file_buffer is not None: 
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        image = cv2.resize(cv2_img, (224, 224), interpolation=cv2.INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1
        probabilities = model.predict(image)

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        if np.round(confidence_score * 100) > 80:
            if cooldown == False:
                # Print prediction
                st.write("Class:" + str(class_name[2:]))
                print(str(class_name[2:]) + "AAAAAAA")
                result = str(class_name[2:])
                if result == "trees\n":
                    st.session_state.hunger += 20
                    st.write("You found some food in the trees! +20 hunger")
                if result == "leaves\n":
                    st.session_state.happiness += 20
                    st.write("You had some fun in the leaves! +20 fun")
                if result == "grass\n":
                    st.session_state.thirst += 20
                    st.write("You found some food in the trees! +20 thirst")
                #st.session_state.level+=1
                ph = st.empty()
                N = 5*60
                for secs in range(N,0,-1):
                    mm, ss = secs//60, secs%60
                    ph.metric("Spend some time with your pet! Image will resume in...", f"{mm:02d}:{ss:02d}")
                    time.sleep(1)


        else:
            st.write("Couldn't identify the image. Take a clearer picture!")
                
        #st.write("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)

        # 27 is the ASCII for the esc key on your keyboard.
        if keyboard_input == 27:
            break


camera.release()
cv2.destroyAllWindows()


# Function to identify element
def image_giver():
    pass


with st.container(height=220):
    level_bar = st.progress(st.session_state.level, text="Level: %i" % st.session_state.level)
    hunger_bar = st.progress(st.session_state.hunger,text="Hunger: %i" %st.session_state.hunger)
    thirst_bar = st.progress(st.session_state.thirst,text="Thirst: %i" %st.session_state.thirst)
    happiness_bar = st.progress(st.session_state.happiness,text="Happiness: %i" %st.session_state.happiness)

