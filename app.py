import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="VANTAGE | FUTURE OF WORK", page_icon="⚡", layout="wide")

# --- FUTURISTIC GLASS-MORPHIC CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    
    /* 1. FUTURISTIC GLOBAL STYLE */
    .stApp {
        background-color: #ffffff !important;
        background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
        background-size: 40px 40px; /* Subtle futuristic grid */
    }

    html, body, [class*="st-"], .stMarkdown, p, div {
        font-family: 'Space Grotesk', sans-serif;
        color: #0f172a !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 2. NEON NAVIGATION BUTTONS */
    .stButton > button {
        border: 1px solid #000000 !important;
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(10px);
        color: #000000 !important;
        border-radius: 0px !important; /* Sharp corners for futuristic look */
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s;
        width: 100% !important;
        box-shadow: 4px 4px 0px #000000;
    }
    .stButton > button:hover {
        background-color: #000000 !important;
        color: #ffffff !important;
        box-shadow: 0px 0px 20px rgba(59, 130, 246, 0.5); /* Blue neon glow */
        transform: translate(2px, 2px);
    }

    /* 3. HERO SECTION - CYBERPUNK WHITE */
    .hero-container {
        padding: 80px 20px;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #000000;
        backdrop-filter: blur(5px);
        margin-bottom: 50px;
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: "SYSTEM READY";
        position: absolute;
        top: 10px;
        left: 10px;
        font-size: 10px;
        letter-spacing: 3px;
        opacity: 0.5;
    }

    .hero-container h1 {
        font-size: 4.5rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: -2px;
        line-height: 0.9;
        margin-bottom: 20px !important;
    }

    /* 4. FUTURISTIC TRACK CARDS */
    .category-card {
        background: rgba(255, 255, 255, 0.5);
        padding: 40px;
        border: 1px solid #e2e8f0;
        min-height: 350px;
        transition: 0.4s;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
    }
    
    .category-card:hover {
        border-color: #3b82f6;
        background: #ffffff;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.1);
    }

    .category-card h3 {
        letter-spacing: 1px;
        text-transform: uppercase;
        font-weight: 700 !important;
        color: #3b82f6 !important;
    }

    /* 5. RANK BADGE - GLOWING NEON */
    .rank-badge {
        background: #000000 !important;
        color: #ffffff !important;
        padding: 15px;
        font-weight: 700;
        text-align: center;
        letter-spacing: 4px;
        border: 1px solid #3b82f6;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.6);
        margin-top: 20px;
    }

    /* 6. BOUNTY BOX */
    .bounty-box {
        background: #ffffff;
        padding: 30px;
        border-left: 5px solid #3b82f6;
        border-top: 1px solid #000000;
        border-right: 1px solid #000000;
        border-bottom: 1px solid #000000;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAV LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate(page_name):
    st.session_state.page = page_name

# --- FUTURISTIC HEADER ---
col_logo, col_n1, col_n2, col_n3, col_n4 = st.columns([2.5, 1, 1, 1, 1])

with col_logo:
    st.markdown("<h1 style='margin:0; font-weight:700; font-size: 32px; letter-spacing: 5px;'>VANTAGE //</h1>", unsafe_allow_html=True)

with col_n1:
    if st.button("01. HOME", key="nav_h"): navigate('Home')
with col_n2:
    if st.button("02. BOUNTIES", key="nav_b"): navigate('Bounties')
with col_n3:
    if st.button("03. MISSION", key="nav_m"): navigate('About')
with col_n4:
    if st.button("04. PROFILE", key="nav_p"): navigate('Portfolio')

st.markdown("<div style='height: 2px; background: #000; width: 100%; margin: 10px 0;'></div>", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-container">
            <h1>FORGE THE <br>FUTURE.</h1>
            <p>The traditional resume is dead. Prove your capability through technical bounties. Get verified by the world's fastest growing startups.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='letter-spacing: 4px; text-align:center;'>AVAILABLE SECTORS</h4>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="category-card">
            <div>
                <p style='font-size: 10px; opacity: 0.5;'>SECTOR_01</p>
                <h3>STEM + DATA</h3>
                <p>Execute Python automation, data cleanup, and algorithmic QA for AI labs.</p>
            </div>
            <p style='font-size: 12px; font-weight: 700;'>[ STATUS: ACTIVE ]</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE TECH", key="btn_s")

    with c2:
        st.markdown("""<div class="category-card">
            <div>
                <p style='font-size: 10px; opacity: 0.5;'>SECTOR_02</p>
                <h3>MARKETING</h3>
                <p>SEO architectural audits, social engine strategy, and brand growth loops.</p>
            </div>
            <p style='font-size: 12px; font-weight: 700;'>[ STATUS: ACTIVE ]</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE GROWTH", key="btn_m")

    with c3:
        st.markdown("""<div class="category-card">
            <div>
                <p style='font-size: 10px; opacity: 0.5;'>SECTOR_03</p>
                <h3>BUSINESS OPS</h3>
                <p>Competitor intelligence, lead-gen architecture, and venture-ready research.</p>
            </div>
            <p style='font-size: 12px; font-weight: 700;'>[ STATUS: ACTIVE ]</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE BIZ", key="btn_b")

# --- MISSION PAGE ---
elif st.session_state.page == 'About':
    st.markdown("<h1 style='text-align:center; letter-spacing: 10px;'>MISSION DATA</h1>", unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 1], gap="large")
    with col_img:
        st.image("https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&q=80&w=800")
    with col_txt:
        st.markdown("""
        <h2 style='letter-spacing: -1px;'>Bridging the Human-Capital Gap</h2>
        <p style='font-size:1.1rem; opacity: 0.8;'>Vantage is an experiential learning engine designed to bypass legacy networking barriers.</p>
        <p style='font-size:1.1rem; opacity: 0.8;'>We provide a direct channel for underrepresented talent to earn <b>Verified Proof of Work</b>. No referrals needed. Just skill.</p>
        <div style='background: #f1f5f9; padding: 20px; border-left: 4px solid #000;'>
            <p style='margin:0; font-weight: 700;'>CORE PROTOCOL: Work > Credentials.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.markdown("<h1 style='text-align:center; letter-spacing: 5px;'>USER PROFILE</h1>", unsafe_allow_html=True)
    p_col1, p_col2 = st.columns([1, 1.5], gap="large")
    with p_col1:
        st.markdown("""<div style='border: 1px solid #000; padding:40px; text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/875/875512.png' width='120' style='filter: grayscale(1);'>
            <h2 style='margin-top:20px;'>ALEX RIVERA</h2>
            <p style='letter-spacing: 2px;'>OAKLAND // CA</p>
            <div class="rank-badge">
                GLOBAL RANK: TOP 10%
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("EXPORT CREDENTIALS", key="share_btn")
    with p_col2:
        st.subheader("VERIFIED BOUNTY LOG")
        st.markdown("""
            <div style='border: 1px solid #e2e8f0; padding:20px; margin-bottom:15px;'>
                <h4 style='margin:0;'>Python Automation Script</h4>
                <p style='margin:5px 0; opacity: 0.6;'>Node: TechFlow AI • [VERIFIED_2024]</p>
            </div>
            <div style='border: 1px solid #e2e8f0; padding:20px; margin-bottom:15px;'>
                <h4 style='margin:0;'>SEO Content Audit</h4>
                <p style='margin:5px 0; opacity: 0.6;'>Node: SmartBites Bakery • [VERIFIED_2024]</p>
            </div>
        """, unsafe_allow_html=True)

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.markdown("<h1 style='letter-spacing: 5px;'>BOUNTY_TERMINAL</h1>", unsafe_allow_html=True)
    st.text_input("QUERY SKILLS / NODES / TRACKS")
    st.markdown("""
        <div class="bounty-box">
            <div style='display:flex; justify-content:space-between;'>
                <div>
                    <h3 style='margin:0; letter-spacing: 1px;'>TECHNICAL LEAD GEN ARCHITECTURE</h3>
                    <p style='margin-top:5px; opacity: 0.6;'>Sector: Business Ops | Time: 5.0 hrs</p>
                </div>
                <div style='text-align:right;'>
                    <h2 style='margin:0; color:#3b82f6 !important;'>$120.00</h2>
                    <p style='margin:0; font-size: 10px;'>ALLOCATED_REWARD</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("DOWNLOAD BRIEF", key="claim_1")
