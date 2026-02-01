import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="💖 Proposal Game",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
/* Force full viewport teal background */
html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background-color: #7fd1c7;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

/* Center card vertically + horizontally */
.wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* White card */
#card {
    background-color: white;
    width: 380px;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    text-align: center;
}

/* Title */
#card h1 {
    color: #ff4b4b;
    font-size: 26px;
    margin-bottom: 10px;
}

/* Image fix */
#card img {
    width: 200px;
    max-width: 100%;
    height: auto;
    margin: 15px 0;
}

/* Button container */
#container {
    position: relative;
    height: 120px;
    margin-top: 15px;
}

/* Same size buttons */
button {
    font-size: 18px;
    padding: 12px 28px;
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

noBtn.addEventListener("mouseover", function () {
    const x = Math.random() * 220;
    const y = Math.random() * 80;
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});

function sayYes() {
    document.getElementById("card").innerHTML =
        '<h1 style="color:#ff4b4b;">🎉 YAYYY!!! 💖💍</h1>' +
        '<h2>You just made me the happiest person alive 😭❤️</h2>';

    var duration = 3000;
    var end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 6,
            spread: 70,
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

# IMPORTANT: Big height to avoid black area
components.html(html_code, height=1200)
