import streamlit as st

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="VANTAGE // NEURAL LINK", page_icon="🧬", layout="wide")

# --- THE "ANTI-WHITE" CYBERPUNK ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* 1. FORCE KILL ALL WHITE BACKGROUNDS */
    .stApp, .main, .block-container {
        background-color: #050505 !important;
        background-image: 
            linear-gradient(90deg, rgba(255, 0, 255, 0.03) 1px, transparent 1px),
            linear-gradient(rgba(0, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
    }

    /* 2. TEXT COLOR OVERRIDES */
    h1, h2, h3 { 
        font-family: 'Orbitron', sans-serif !important; 
        color: #00ffff !important; /* Cyan Neon */
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 5px;
    }
    
    p, span, div, label { 
        font-family: 'Rajdhani', sans-serif !important; 
        color: #e2e8f0 !important; /* Silver text */
        font-weight: 500 !important;
        font-size: 18px !important;
    }

    /* 3. NEON GLASS PANELS */
    .cyber-card {
        background: rgba(15, 15, 20, 0.9) !important;
        border: 2px solid #ff00ff !important; /* Pink Neon Border */
        padding: 30px;
        border-radius: 0px 20px 0px 20px;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.2);
        transition: 0.4s;
        margin-bottom: 20px;
    }
    .cyber-card:hover {
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.6);
        transform: scale(1.02);
        background: rgba(20, 20, 30, 1) !important;
    }

    /* 4. GLITCH BUTTONS */
    .stButton > button {
        width: 100% !important;
        background: transparent !important;
        color: #00ffff !important;
        border: 2px solid #00ffff !important;
        font-family: 'Orbitron' !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        padding: 15px !important;
        position: relative;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: #00ffff !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00ffff;
    }

    /* 5. SIDEBAR OVERRIDE */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 2px solid #00ffff;
    }

    /* HIDE DEFAULTS */
    header, footer, #MainMenu { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- NAV LOGIC ---
if 'page' not in st.session_state: st.session_state.page = 'TERMINAL'

with st.sidebar:
    st.markdown("<h1>VANTAGE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#ff00ff !important;'>>> SYSTEM STATUS: OVERRIDE</p>", unsafe_allow_html=True)
    st.divider()
    if st.button(">> 01_TERMINAL"): st.session_state.page = 'TERMINAL'
    if st.button(">> 02_BOUNTIES"): st.session_state.page = 'BOUNTIES'
    if st.button(">> 03_ARCHIVE"): st.session_state.page = 'MISSION'
    if st.button(">> 04_IDENTITY"): st.session_state.page = 'USER'

# --- PAGE: TERMINAL (HOME) ---
if st.session_state.page == 'TERMINAL':
    st.markdown("""
        <div style='text-align: center; padding: 50px 0;'>
            <h1 style='font-size: 5rem; color: #ff00ff !important; text-shadow: 0 0 20px #ff00ff;'>VANTAGE</h1>
            <h2 style='font-size: 1.5rem;'>The Experience Protocol</h2>
            <p style='color: #00ffff !important;'>[ STATUS: ACCESS GRANTED ]</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class='cyber-card'>
            <h3>CORE_STEM</h3>
            <p>PYTHON // AUTOMATION // DATA</p>
            <p style='font-size: 14px !important; opacity: 0.7;'>Execute code bounties for high-growth AI nodes.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE_STEM", key="b1")

    with col2:
        st.markdown("""<div class='cyber-card' style='border-color: #00ffff !important; box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);'>
            <h3 style='color: #ff00ff !important;'>CORE_GROWTH</h3>
            <p>SEO // STRATEGY // BRAND</p>
            <p style='font-size: 14px !important; opacity: 0.7;'>Optimize brand architecture for market dominance.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE_GROWTH", key="b2")

    with col3:
        st.markdown("""<div class='cyber-card'>
            <h3>CORE_BIZ</h3>
            <p>INTEL // RESEARCH // LEADS</p>
            <p style='font-size: 14px !important; opacity: 0.7;'>Extract competitor intelligence and market data.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE_BIZ", key="b3")

# --- PAGE: BOUNTIES ---
elif st.session_state.page == 'BOUNTIES':
    st.markdown("<h1>LIVE_BOUNTY_STREAM</h1>", unsafe_allow_html=True)
    st.text_input("QUERY_DATABASE_")
    
    st.markdown("""
        <div class='cyber-card' style='border-color: #00ffff !important;'>
            <div style='display: flex; justify-content: space-between;'>
                <div>
                    <h2 style='margin:0; font-size: 1.5rem;'>DATA_SCRAPE_V4</h2>
                    <p style='color:#ff00ff !important;'>NODE: NEXUS_AI</p>
                </div>
                <div style='text-align: right;'>
                    <h1 style='color: #00ffff !important; margin:0;'>250.00</h1>
                    <p style='font-size: 12px !important;'>REWARD_CREDITS</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("CONNECT_TO_BRIEF")

# --- PAGE: IDENTITY (USER) ---
elif st.session_state.page == 'USER':
    st.markdown("<h1>IDENTITY_NODE</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("""
            <div class='cyber-card' style='text-align: center;'>
                <div style='width: 120px; height: 120px; background: linear-gradient(#ff00ff, #00ffff); border-radius: 50%; margin: 0 auto; box-shadow: 0 0 20px #ff00ff;'></div>
                <h2 style='margin-top: 20px;'>ALEX_RIVERA</h2>
                <p>RANK: [ ELITE_10 ]</p>
                <p style='font-size: 12px !important;'>LOCATION: OAKLAND_GRID_04</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='cyber-card'><h3>VERIFIED_LEDGER</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#00ffff !important;'>>> TASK_042: PYTHON_AUTOMATION // VERIFIED</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#00ffff !important;'>>> TASK_089: MARKET_INTEL_V1 // VERIFIED</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.button("EXPORT_IDENTITY_KEY")
