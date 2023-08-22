import streamlit as st 

st.title("Cauta serial")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Tasteaza numele unui serial", st.session_state["my_input"])
submit = st.button("Cauta")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)