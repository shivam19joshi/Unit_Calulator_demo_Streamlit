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
/* Remove scroll everywhere */
html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background-color: #7fd1c7;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

/* Full screen flex center */
.wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
}

/* Medium white card */
#card {
    background-color: white;
    width: 420px;
    padding: 30px 25px;
    border-radius: 22px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    text-align: center;
}

/* Question */
#card h1 {
    color: #ff4b4b;
    font-size: 26px;
    margin-bottom: 12px;
}

/* Image standard size */
#card img {
    width: 230px;
    max-width: 100%;
    height: auto;
    margin: 10px 0 15px 0;
}

/* Button area */
#container {
    position: relative;
    height: 110px;
}

/* Same size buttons */
button {
    font-size: 18px;
    padding: 12px 30px;
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
    const x = Math.random() * 240;
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
            particleCount: 7,
            spread: 80,
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

# Very important: exact viewport height, no scroll
components.html(html_code, height=850)
