import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💖 Proposal Game", layout="centered")

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
    position: absolute;
    cursor: pointer;
}
</style>

<div id="card">
    <h1>💍 Will You Marry Me, XYZ? 💖</h1>

    <img src="https://raw.githubusercontent.com/shivam19joshi/Unit_Calulator_demo_Streamlit/main/cute_cat.jpg"
         width="250">

    <div id="container">
        <button id="yes" onclick="sayYes()">YES ❤️</button>
        <button id="no">NO 💔</button>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
const noBtn = document.getElementById("no");

noBtn.addEventListener("mouseover", function () {
    const x = Math.random() * 250;
    const y = Math.random() * 100;
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
"""

components.html(html_code, height=520)
