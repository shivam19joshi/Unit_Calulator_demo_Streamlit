import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💖 Proposal Game", layout="centered")

# Title
st.markdown(
    """
    <h1 style="text-align:center; color:#ff4b4b;">
        💍 Will You Marry Me, XYZ? 💖
    </h1>
    """,
    unsafe_allow_html=True
)

# Cute image (replace with your GitHub raw image link)
st.markdown(
    """
    <div style="text-align:center;">
        <https://github.com/shivam19joshi/Unit_Calulator_demo_Streamlit/blob/main/cute_cat.jpg"
             width="300">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# HTML + JS Game
html_code = """
<style>
#container {
    text-align: center;
    position: relative;
    height: 200px;
}

button {
    font-size: 20px;
    padding: 10px 25px;
    border-radius: 30px;
    border: none;
    cursor: pointer;
}

#yes {
    background-color: #ff4b4b;
    color: white;
}

#no {
    background-color: #555;
    color: white;
    position: absolute;
}
</style>

<div id="container">
    <button id="yes" onclick="sayYes()">YES ❤️</button>
    <button id="no">NO 💔</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
const noBtn = document.getElementById("no");

noBtn.addEventListener("mouseover", function () {
    const x = Math.random() * 250;
    const y = Math.random() * 120;
    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});

function sayYes() {
    document.body.innerHTML = `
        <h1 style="text-align:center; color:#ff4b4b;">
            🎉 YAYYY!!! 💖💍
        </h1>
        <h2 style="text-align:center;">
            You just made me the happiest person alive 😭❤️
        </h2>
        <div style="text-align:center;">
            <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/celebrate.png"
                 width="300">
        </div>
    `;

    // Party blast
    var duration = 3 * 1000;
    var end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 5,
            angle: 60,
            spread: 55,
            origin: { x: 0 }
        });
        confetti({
            particleCount: 5,
            angle: 120,
            spread: 55,
            origin: { x: 1 }
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
}
</script>
"""

components.html(html_code, height=300)
