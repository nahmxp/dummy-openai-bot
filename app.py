# pip install streamlit (run on terminal)
import streamlit as st
import pandas as pd
import numpy as np

st.title("🧠 Streamlit Learning Playground")

# Text Input and Button
user_input = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {user_input} 👋")

# Chat Display (Simple Style)
st.subheader("Chat Simulator")
chat = st.chat_input("Say something!")
if chat:
    st.write(f"You: {chat}")
    st.write(f"Bot: Echo - {chat}")

# Show a Chart
st.subheader("Random Chart")
df = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(df)

# Show a Video
st.subheader("Sample Video")
st.video("https://www.youtube.com/watch?v=3jZ5vnv-LZc")

# Show an Audio
st.subheader("Sample Audio")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
