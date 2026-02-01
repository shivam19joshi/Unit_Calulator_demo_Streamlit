import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="💖 Proposal Game",
    layout="wide"
)

# Remove Streamlit default padding & scroll
st.markdown(
    """
    <style>
    .main {
        padding: 0rem !important;
    }
    iframe {
        overflow: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
/* Lock everything */
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
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

/* Proper medium card */
#card {
    width: 480px;
    padding: 35px;
    background: white;
    border-radius: 25px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.3);
    text-align: center;
}

/* Question */
#card h1 {
    font-size: 28px;
    color: #ff4b4b;
    margin-bottom: 15px;
}

/* Image balanced */
#card img {
    width: 240px;
    height: auto;
    margin: 15px 0 20px 0;
}

/* Button playground (BIG space) */
#container {
    position: relative;
    width: 100%;
    height: 180px;
}

/* Buttons same size */
button {
    font-size: 18px;
    padding: 14px 32px;
    border-radius: 30px;
    border: none;
    cursor: pointer;
}

/* Yes */
#yes {
    background-color: #ff4b4b;
    color: white;
}

/* No */
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
        <h1>💍 Will You Marry Me, XYZ? 💖</h1>

        <img src="https://raw.githubusercontent.com/shivam19joshi/Unit_Calulator_demo_Streamlit/main/cute_cat.jpg">

        <div id="container">
            <button id="yes" onclick="sayYes()">YES ❤️</button>
            <button id="no">NO 💔</button>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
const noBtn = document.getElementById("no");
const container = document.getElementById("container");

noBtn.addEventListener("mouseover", function () {
    const maxX = container.clientWidth - noBtn.offsetWidth;
    const maxY = container.clientHeight - noBtn.offsetHeight;

    const x = Math.random() * maxX;
    const y = Math.random() * maxY;

    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});

function sayYes() {
    document.getElementById("card").innerHTML =
        '<h1 style="color:#ff4b4b;">🎉 YAYYY!!! 💖💍</h1>' +
        '<h2>You just made me the happiest person alive 😭❤️</h2>';

    const duration = 3000;
    const end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 8,
            spread: 90,
            origin: { y: 0.6 }
        });
        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
}
</script>
</body>
</html>
"""

# IMPORTANT: viewport-sized iframe
components.html(html_code, height=1000)
