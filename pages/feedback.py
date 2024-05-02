import streamlit as st
import json
from logics.text import promptToText
from logics.sendMessage import sendMessage
from datetime import datetime

if "img" not in st.session_state:
    st.switch_page("pages/complain.py")

uploaded_file = st.session_state["img"]
response = st.session_state["response"]
toilet_id = st.session_state["toilet_id"]



def generateWorkingMessage(toilet_id, condition, target):
    action_prompt = """
    Imagine you are the person in charge as """ + target + """.
    Think what you need to prepare to fix the situation and fill it inside the preparation. 
    Please use your knowledge base to suggest the best solutions to solve the problem and fill
    it in the suggested solution. Remove any bolds and italics.
    
    Create a message in the format below. 
    Preparation: [Any tools needed before coming in to fix the problem.]
    Suggested Solution: [Any suggested solution to solve the problem.] """
    response = promptToText(action_prompt)
    message = "[Complaint No.1 @ " + toilet_id + "]\n"
    message += "Received Date: "+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+"\n\n"
    message += "Condition:\n" + condition + "\n\n"
    message += response.replace("\n\n", "\n").replace("Suggested Solution:", "\nSuggested Solution:")
    return message.replace("**", "")



st.set_page_config(page_title="Gripe N Wipe", page_icon="🚽",initial_sidebar_state="collapsed")
st.title("🚽 Gripe N Wipe")
st.write("Here, Complaints Get Scrubbed, Not Shrugged!")

uploaded_file = st.session_state["img"]
response = st.session_state["response"]
 
with st.container(border=True):
    st.subheader("Feedback Received: ")
    data = json.loads(response)
    st.image(uploaded_file, caption = data["condition"], use_column_width=True)
    st.subheader("Action Taken: ")
    st.success("Receive the complaint. Start brainstorming the action plan.")
    if(data["need-janitor"] == "yes"):
        message = generateWorkingMessage(toilet_id, data["condition"], "Janitor")
        response = sendMessage(message, "GW_Janitorbot")
        if(response["ok"]):
            st.success("Heads up! Janitor on the way to perform some royal restroom renovations.")
    elif(data["quick-clean"] == "yes"):
        message = generateWorkingMessage(toilet_id, data["condition"], "Shopkeeper")
        response = sendMessage(message, "SinKwangAngleBot")
        if(response["ok"]):
            st.success("Shopkeeper on patrol to make things sparkle")
    if(data["big-fix"]  == "yes"):
        plumber_message = generateWorkingMessage(toilet_id, data["condition"], "Plumbers")
        shopkeeper_message = "Just a heads up that the toilet in "+toilet_id
        shopkeeper_message += " is currently out of order due to some plumbing problems. \n"
        shopkeeper_message += "To avoid any messy surprises, could you please shut the door and put a sign up saying 'Toilet Out of Order'?\n"
        shopkeeper_message += "We've already booked a plumber to come fix it asap, so hopefully it won't be down for long.\n"
        shopkeeper_message += "Thanks for your help!"
        shopkeeper_response = sendMessage(shopkeeper_message, "SinKwangAngleBot")
        plumber_response = sendMessage(plumber_message, "CanteenWasteBot")
        if(shopkeeper_response["ok"]):
            st.success("[Employee] Gotta shut down the throne room before things get out of hand!")
        if(plumber_response["ok"]):
            st.success("[External Parties] A plumbing knight is en route to slay your bathroom woes!")