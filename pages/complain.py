import streamlit as st
import requests
import os
import json
from datetime import datetime
import time

from logics.text import promptToText
from logics.image import imageToText
from logics.sendMessage import sendMessage

image_prompt = """
    Observe the picture given as clear as possible. Use simple English to describe the image.
    Make sure your response is in a single paragraph."""


problem_prompt = """Please read and understand the scenario below. Refactor it into the JSON format below. 
{
    "condition": [Detailed description of the problem],
    "isSmell": [yes/no]
    "need-janitor": [yes/no]
    "quick-clean": [yes/no]
    "big-fix": [yes/no]
}
if the toilet is dirty and need a clean up, please choose [need-janitor] as yes.
if the toilet has a wet floor, please choose [quick-clean] as yes.
if the toliet has any infrastructure issue, please choose [big-fix] as yes.
Choose ONLY the most serious one.

The condition is the detailed description of the problem. Make sure the person in charge can understand
and make some preparation before coming to solve the problem. Use simple English to describe the problem. 

[Scenario]\n
"""


st.set_page_config(page_title="Gripe N Wipe", page_icon="🚽",initial_sidebar_state="collapsed")
st.title("🚽 Gripe N Wipe")
st.write("Snap, Grip, Swipe! Cleans Complaints in a Swipe!")

if "id" not in st.query_params:
    toilet_id = "none"
else:
    toilet_id = st.query_params["id"]

with st.container(border=True):
    st.subheader("Got any gripes about "+toilet_id+"? ")
    uploaded_file = st.file_uploader("Snap a photo", type=['png', 'jpg', 'gif', 'jpeg'])
    smell = st.checkbox("Does the toilet has unpleasant smell? 🤮 ", value = False)
    caption2 = st.text_area('More Feedback', height=150)
    if(st.button('Submit Your Complain',use_container_width=True)):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            with open(uploaded_file.name, "wb") as file:
                file.write(bytes_data) 
            caption  = imageToText(image_prompt, uploaded_file.name)
        else:
            caption = ""
        comment = caption2 if uploaded_file is not None else ""
        if smell:
            comment = "There are unpleasant smell on the toilet."
        problem_prompt += caption+ "/n" +comment+ "/n" + caption2
        response = promptToText(problem_prompt)
        
        st.session_state["response"] = response
        st.session_state["toilet_id"] = toilet_id
        st.session_state["caption"] = caption
        st.session_state["img"] = uploaded_file.name
        
        st.toast("Received! Thank you for your feedback!")
        time.sleep(1)
        st.switch_page("pages/feedback.py")
        
# Widget: Calling to get toilet paper
tissue = st.button("🧻\tSend me the tissue",use_container_width=True)
if(tissue):
    message = "Could you kindly send a roll of toilet paper at "+ toilet_id +" when you have a moment? Thanks!"
    response = sendMessage(message, "SinKwangAngleBot")
    if(response["ok"]):
        st.toast("Be patient! Tissue is OTW")
