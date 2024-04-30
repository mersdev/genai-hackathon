import streamlit as st

if 'username' not in st.session_state:
    st.session_state['username'] = "none"

if(st.session_state.username != "none" and st.session_state.username != ""):
    st.switch_page("pages/home.py")
else:
    st.switch_page("pages/login.py")

