import streamlit as st

st.set_page_config(page_title="DeepMed AI", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
        background-color: #f9fbfc;
        color: #1e293b;
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 8vh 2rem 6vh;
        background: radial-gradient(circle at top left, #e0f2fe, #f9fbfc);
        border-radius: 20px;
    }
    .hero h1 {
        font-size: 3.5rem;
        font-weight: 700;
        color: #0284c7;
        margin-bottom: 0.5rem;
    }
    .hero p {
        font-size: 1.25rem;
        color: #475569;
        margin-bottom: 3rem;
    }

    /* Card Layout */
    .card-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        max-width: 1200px;
        margin: 3rem auto 0;
    }

    .card {
        flex: 1 1 400px;  /* flexible width, min 400px */
        max-width: 500px;  /* max width for large screens */
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
        backdrop-filter: blur(10px);
        transition: all 0.4s ease;
        border: 1px solid rgba(0,0,0,0.05);
    }

    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 32px rgba(2,132,199,0.15);
    }

    .card h3 {
        color: #0284c7;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }

    .card p {
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }

    .card a {
        background: linear-gradient(90deg, #0ea5e9, #38bdf8);
        color: white;
        padding: 0.8rem 2rem;  /* wider button */
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        transition: 0.3s ease;
    }

    .card a:hover {
        background: linear-gradient(90deg, #0284c7, #0ea5e9);
        transform: scale(1.05);
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 6vh;
        color: #94a3b8;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Hero Section ----------
st.markdown("""
<div class="hero">
    <h1>DeepMed AI</h1>
    <p>Empowering medical professionals with advanced AI-driven diagnostics and insights.</p>
</div>
""", unsafe_allow_html=True)

# ---------- Card Section ----------
st.markdown("""
<div class="card-container">
    <div class="card">
        <h3>🩻 X-Ray Analysis</h3>
        <p>Upload X-rays and generate precise AI-powered diagnostic reports in seconds.</p>
        <a href="https://deepmed-hsrof9mciqy2fwfdzhv3dh.streamlit.app/" target="_blank">Launch</a>
    </div>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="card-container">
    <div class="card">
        <h3>💬 Medical Chatbot</h3>
        <p>Ask clinical questions and receive evidence-based answers from DeepMed’s AI assistant.</p>
        <a href="https://deepmed-8xqgfsgzjzeraawfgp4y55.streamlit.app/" target="_blank">Launch</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
    © 2025 DeepMed AI — Transforming Radiology through Intelligence
</div>
""", unsafe_allow_html=True)
