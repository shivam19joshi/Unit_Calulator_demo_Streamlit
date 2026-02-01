import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="areyouserious", layout="wide")

# Remove Streamlit padding
st.markdown(
    """
    <style>
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background-color: #7fd1c7;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

/* Full screen center */
.wrapper {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* White card */
#card {
    width: 460px;
    max-width: 90%;
    padding: 32px;
    background: white;
    border-radius: 26px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.3);
    text-align: center;
}

/* Question */
#card h1 {
    font-size: 26px;
    color: #ff4b4b;
    margin-bottom: 12px;
}

/* Image */
#card img {
    width: 230px;
    max-width: 100%;
    height: auto;
    margin: 10px 0 18px 0;
}

/* Button playground */
#container {
    position: relative;
    width: 100%;
    height: 200px;
}

/* Buttons */
button {
    font-size: 18px;
    padding: 14px 34px;
    border-radius: 30px;
    border: none;
    cursor: pointer;
}

/* YES */
#yes {
    background-color: #ff4b4b;
    color: white;
}

/* NO */
#no {
    background-color: #777;
    color: white;
    position: absolute;
}
</style>
</head>

<body>
<div class="wrapper">
    <div id="card">
        <h1>💍 Will You Marry Me, Purvi? 💍</h1>

        <img src="https://raw.githubusercontent.com/shivam19joshi/Unit_Calulator_demo_Streamlit/main/cute_cat.jpg">

        <div id="container">
            <button id="yes" onclick="sayYes()">YES ❤️</button>
            <button id="no">NO </button>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
const noBtn = document.getElementById("no");
const container = document.getElementById("container");

function moveNo() {
    const maxX = container.clientWidth - noBtn.offsetWidth;
    const maxY = container.clientHeight - noBtn.offsetHeight;

    noBtn.style.left = Math.random() * maxX + "px";
    noBtn.style.top = Math.random() * maxY + "px";
}

/* Desktop */
noBtn.addEventListener("mouseover", moveNo);

/* Mobile */
noBtn.addEventListener("touchstart", function(e) {
    e.preventDefault();
    moveNo();
});

noBtn.addEventListener("touchmove", function(e) {
    e.preventDefault();
    moveNo();
});

function sayYes() {
    document.getElementById("card").innerHTML =
        '<h1 style="color:#ff4b4b;">🎉 YAYYY!!! 💖💍</h1>' +
        '<h2>You just made me the happiest person alive 😭❤️</h2>';

    const end = Date.now() + 3000;
    (function frame() {
        confetti({
            particleCount: 8,
            spread: 90,
            origin: { y: 0.6 }
        });
        if (Date.now() < end) requestAnimationFrame(frame);
    })();
}
</script>
</body>
</html>
"""

# Critical: disable iframe scroll
components.html(html_code, height=800, scrolling=False)
