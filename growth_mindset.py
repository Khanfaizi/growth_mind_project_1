#streamlit
import streamlit as st

st.set_page_config(page_title="Growth mindset project", page_icon="★")
st.title("Growth Mindset Project")

st.header("☀ Welcome to Out Project Journey!")
st.write("Learn From Challenges Unleash Your Potential")

#qoute section

st.header("Todays Growth Mindset Qoute")
st.write("Accept the challenges so that you can feel the exhilaration of victory.")

st.header("Whats Your Challenge Today")
user_input = st.text_input("Describe a Challenge Your Are Facing")

#condition 
if user_input:
    st.success(f"you are facing {user_input}. keep pushing forward")
else :    
    st.warning("Tell us about your challenge to get started")

#reflection
st.header("Reflect on Your Working")
reflection = st.text_area("Write Your Reflection Here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your reflection")

#achievment
st.header("Celebrate Your Wins!") 
acheivment = st.text_input("Share something you recently accoplished:")

if acheivment:
    st.success(f"Amazing! You Acheived: {acheivment} ")
else: 
    st.info("Big or small , every acheivment counts! share one now! ")

 #footer 
st.write("- - -")       
st.write("Keep Beleiving on your self, Growth is a Journey, not a destination")
st.write("**Created By Faiz Khan**")