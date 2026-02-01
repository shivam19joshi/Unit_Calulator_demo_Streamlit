import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💖 Proposal Game", layout="centered")

# Page background
st.markdown(
    """
    <style>
    body {
        background-color: #cdeeee;
    }
    </style>
    """,
    unsafe_allow_html=True
)

html_code = """
<style>
body {
    background-color: #cdeeee;
}

#card {
    background-color: white;
    width: 400px;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    margin: auto;
    text-align: center;
}

#card h1 {
    color: #ff4b4b;
}

#container {
    position: relative;
    height: 150px;
    margin-top: 20px;
}

#yes {
    font-size: 28px;
    padding: 20px 50px;
    border-radius: 40px;
    border: none;
    background-color: #ff4b4b;
    color: white;
    cursor: pointer;
}

#no {
    font-size: 14px;
    padding: 6px 12px;
    border-radius: 20px;
    border: none;
    background-color: #777;
    color: white;
    position: abs
