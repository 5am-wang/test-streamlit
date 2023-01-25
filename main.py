import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit for the very beginer")
st.write("Display Progress Bar")
"Start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!"

left_column, right_column = st.columns(2)
button = left_column.button("Display text in the right column")
if button:
    right_column.write("Here is the right column.")

expander1 = st.expander("Inquiry")
expander1.write("Write down the detail of the inquiry1.")
expander2 = st.expander("Inquiry")
expander2.write("Write down the detail of the inquiry2.")
expander3 = st.expander("Inquiry")
expander3.write("Write down the detail of the inquiry3.")

# option = st.text_input("What is your hobby")
# "Your hobby is ", option, " ."

# condition = st.slider("How's your feeling now?", 0, 100, 50)
# "Your condition is ", condition

# if st.checkbox("Show Image"):
#     img = Image.open(".jpg")
#     st.image(img, caption="Immortan Joe", use_column_width = True)

