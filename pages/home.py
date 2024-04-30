import streamlit as st

st.set_page_config(page_title="Gripe N Wipe", page_icon="🚽",initial_sidebar_state="collapsed")
st.title("🚽 Gripe N Wipe")
st.write("Here, Complaints Get Scrubbed, Not Shrugged!")


if(st.button("Logout",use_container_width=True)):
    st.session_state['username'] = "none"
    st.success('Logout Successful')
    st.switch_page("app.py")