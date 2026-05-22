import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title=" Sneha",
    page_icon="💖",
    layout="centered"
)

today = datetime.now().strftime("%B %d, %Y")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>

body {{
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #141e30, #243b55);
    font-family: Arial, sans-serif;
    color: white;
}}

.container {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 95vh;
}}

.card {{
    width: 80%;
    max-width: 700px;
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.35);
}}

.small {{
    font-size: 22px;
    margin-bottom: 10px;
}}

.name {{
    font-size: 72px;
    font-weight: bold;
    background: linear-gradient(to right, #ff4d6d, #ff85a1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 25px;
}}

.message {{
    font-size: 20px;
    line-height: 1.8;
    color: #f2f2f2;
}}

.highlight {{
    color: #ff9ecb;
    font-weight: bold;
}}

.button {{
    margin-top: 30px;
    display: inline-block;
    padding: 14px 28px;
    border-radius: 40px;
    background: linear-gradient(to right, #ff4d6d, #ff85a1);
    color: white;
    font-size: 18px;
    font-weight: bold;
}}

.footer {{
    margin-top: 20px;
    font-size: 14px;
    color: rgba(255,255,255,0.7);
}}

</style>
</head>

<body>

<div class="container">

    <div class="card">

        <div class="small">
            💌 A Special Message For
        </div>

        <div class="name">
            Sneha ✨
        </div>

        <div class="message">

            Thank you for trusting me with your project ❤️
            <br><br>

            I've officially
            <span class="highlight">started working on the app</span>,
            and I'm genuinely excited to create something
            <span class="highlight">beautiful, modern, and impressive.</span>
            💫

            <br><br>

            Every detail is being crafted with creativity,
            passion, and dedication because your project deserves nothing less 🌸

        </div>
    </div>

</div>

</body>
</html>
"""

components.html(html_code, height=700)
