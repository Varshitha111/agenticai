import streamlit as st
st.title("media platform")
login,signup=st.tabs(["login","signup"])
with login:
    st.header("LOGIN")
    with st.form("login_form"):
        
        # st.form("login_form")
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        button=st.form_submit_button("login")

with signup:
    st.header("signup")
    with st.form("signup_form"):
        # st.form("signup_form")
        name=st.text_input("name")
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        button=st.form_submit_button("signup")
        
        
        