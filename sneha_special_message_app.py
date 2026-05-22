import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="For Sneha ✨",
    page_icon="💖",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Main Glass Card */
.card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    padding: 45px;
    border-radius: 28px;
    text-align: center;
    margin-top: 40px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0px 8px 35px rgba(0,0,0,0.35);
    animation: fadeIn 1s ease-in-out;
}

/* Small Heading */
.top-text {
    font-size: 22px;
    color: #f5f5f5;
    margin-bottom: 15px;
}

/* Name Styling */
.name {
    font-size: 78px;
    font-weight: bold;
    background: linear-gradient(90deg, #ff4d6d, #ff85a1, #ffd6e0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

/* Message */
.message {
    font-size: 20px;
    line-height: 1.9;
    color: #f1f1f1;
}

/* Highlighted Words */
.highlight {
    color: #ff9ecb;
    font-weight: bold;
}

/* Button */
.button {
    display: inline-block;
    margin-top: 30px;
    padding: 14px 30px;
    border-radius: 50px;
    background: linear-gradient(90deg, #ff4d6d, #ff85a1);
    color: white;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    box-shadow: 0px 5px 18px rgba(255,77,109,0.45);
}

/* Footer */
.footer {
    margin-top: 25px;
    color: rgba(255,255,255,0.7);
    font-size: 14px;
}

/* Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(25px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTENT ---------------- #

today = datetime.now().strftime("%B %d, %Y")

st.markdown(f"""
<div class="card">

    <div class="top-text">
        💌 A Special Message For
    </div>

    <div class="name">
        Sneha ✨
    </div>

    <div class="message">

        Thank you for trusting me with your project. ❤️ <br><br>

        I’ve officially 
        <span class="highlight">started working on the app</span>, 
        and I’m genuinely excited to transform your vision into something 
        <span class="highlight">beautiful, modern, and impressive.</span> 💫 <br><br>

        Every detail is being crafted with creativity, passion,
        and dedication because your project deserves nothing less. 🌸

    </div>

    <div class="button">
        🚀 Work In Progress
    </div>

    <div class="footer">
        Started on • {today}
    </div>

</div>
""", unsafe_allow_html=True)

# ---------------- EFFECTS ---------------- #

st.balloons()

st.success("✨ The project journey has officially begun!")
