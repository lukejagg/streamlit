import streamlit as st

# Tab title and icon
# st.set_page_config(page_title="Amazing", page_icon="🤓")

# Document content
st.title("Amazing")
st.write("Hello world")

# Side bar
st.sidebar.title("Sidebar")
st.sidebar.write("Nice, a sidebar.")
st.sidebar.button("Click me")