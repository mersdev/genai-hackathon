import time
import streamlit as st

st.set_page_config(page_title="ToiletTale", page_icon="🚽",initial_sidebar_state="collapsed")
st.title("🚽 ToiletTale: Kopi O Outcry")
st.write("Clock in and smell the beans at ToiletTale!")

with st.form(key='login_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    onLogin = st.form_submit_button('Login',use_container_width=True)

if(onLogin and username and password):
    with st.spinner(text='In progress'):
        time.sleep(1)
    st.session_state['username'] = username
    st.success("Login Successfully. Welcome "+username)
    time.sleep(1)
    st.switch_page("app.py")
