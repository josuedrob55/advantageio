import streamlit as st
import pandas as pd
import time

# --- 00. INITIALIZE INTERFACE ---
st.set_page_config(
    page_title="VANTAGE // PROTOCOL",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 01. THE "GLITCH-GLASS" CSS ENGINE ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;700&family=Rajdhani:wght@300;500;700&display=swap');

    /* DARK-MATTER BACKGROUND */
    .stApp {
        background: #000000 !important;
        background-image: 
            radial-gradient(circle at 2px 2px, rgba(0, 255, 255, 0.03) 1px, transparent 0),
            linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
        background-size: 40px 40px, 100px 100px, 100px 100px;
    }

    /* GLOBAL TYPOGRAPHY */
    h1, h2, h3 { font-family: 'Orbitron', sans-serif !important; letter-spacing: 5px !important; text-transform: uppercase; color: #00ffff !important; }
    p, span, div, li { font-family: 'JetBrains Mono', monospace !important; color: #cbd5e1 !important; }

    /* HOLOGRAPHIC DOCK NAVIGATION */
    [data-testid="stSidebar"] {
        background-color: rgba(5, 5, 5, 0.95) !important;
        border-right: 1px solid #333;
        backdrop-filter: blur(20px);
    }
    
    /* NAVIGATION BUTTONS */
    .stButton > button {
        border-radius: 0px !important;
        border: 1px solid #333 !important;
        background: rgba(255,255,255,0.02) !important;
        color: #888 !important;
        font-family: 'Orbitron' !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s;
        margin-bottom: 5px;
    }
    .stButton > button:hover {
        border-color: #00ffff !important;
        color: #00ffff !important;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.4);
    }

    /* THE GLITCH CARD */
    .vantage-card {
        background: rgba(10, 10, 10, 0.8);
        border: 1px solid #222;
        padding: 30px;
        position: relative;
        transition: 0.5s;
        overflow: hidden;
    }
    .vantage-card:hover {
        border-color: #ff00ff;
        box-shadow: -5px 0 20px rgba(255, 0, 255, 0.2);
        transform: translateX(5px);
    }
    .vantage-card::before {
        content: ""; position: absolute; top: 0; left: 0; width: 2px; height: 100%; background: #00ffff;
    }

    /* STAT MODULES */
    .stat-box {
        text-align: center;
        padding: 20px;
        border: 1px solid #1a1a1a;
        background: rgba(255,255,255,0.01);
    }

    /* HIDE DEFAULT HEADER/FOOTER */
    header, footer, #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- 02. SYSTEM NAVIGATION ---
if 'active_node' not in st.session_state:
    st.session_state.active_node = 'DASHBOARD'

def set_node(node_name):
    st.session_state.active_node = node_name

with st.sidebar:
    st.markdown("<h1 style='font-size: 22px;'>VANTAGE // OS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 9px; color: #555;'>SYSTEM: ONLINE | SECURE: YES</p>", unsafe_allow_html=True)
    st.divider()
    
    st.button("⬢ 01 // DASHBOARD", on_click=set_node, args=('DASHBOARD',), use_container_width=True)
    st.button("⬢ 02 // BOUNTIES", on_click=set_node, args=('BOUNTIES',), use_container_width=True)
    st.button("⬢ 03 // SECTORS", on_click=set_node, args=('SECTORS',), use_container_width=True)
    st.button("⬢ 04 // PROTOCOL", on_click=set_node, args=('ABOUT',), use_container_width=True)
    st.button("⬢ 05 // IDENTITY", on_click=set_node, args=('PROFILE',), use_container_width=True)
    
    st.divider()
    st.markdown("<p style='font-size: 10px;'>VANTAGE-AI ANALYTICS</p>", unsafe_allow_html=True)
    st.progress(0.74, text="SYNC: 74%")
    
    st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
    if st.button("LOGOUT // DISCONNECT"):
        st.toast("Disconnecting from Neural Link...")

# --- 03. PAGE MODULES ---

# --- DASHBOARD (HOME) ---
if st.session_state.active_node == 'DASHBOARD':
    st.markdown("<h1>COMMAND_CENTER</h1>", unsafe_allow_html=True)
    st.write(">> INITIALIZING USER_METRICS_MODULE...")
    
    # Hero Visual
    col_h1, col_h2 = st.columns([2, 1])
    with col_h1:
        st.markdown("""
            <div style='padding: 50px 0;'>
                <h1 style='font-size: 4rem; line-height: 0.9;'>FORGE YOUR<br><span style='color: #ff00ff !important;'>DIGITAL FATE</span></h1>
                <p style='margin-top: 20px; letter-spacing: 3px;'>THE TRADITIONAL RESUME IS OBSOLETE. PROVE YOUR VALUE THROUGH WORK.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.image("https://images.unsplash.com/photo-1614728263952-84ea256f9679?auto=format&fit=crop&q=80&w=800", caption="[SYSTEM_CORE]")

    # Quick Stats Row
    st.markdown("### SYSTEM_OVERVIEW")
    s1, s2, s3, s4 = st.columns(4)
    s1.markdown("<div class='stat-box'><h3 style='margin:0;'>1.2K</h3><p style='font-size: 10px;'>ACTIVE BOUNTIES</p></div>", unsafe_allow_html=True)
    s2.markdown("<div class='stat-box'><h3 style='margin:0;'>$240K</h3><p style='font-size: 10px;'>REWARDS DISTRIBUTED</p></div>", unsafe_allow_html=True)
    s3.markdown("<div class='stat-box'><h3 style='margin:0;'>14MS</h3><p style='font-size: 10px;'>LATENCY</p></div>", unsafe_allow_html=True)
    s4.markdown("<div class='stat-box'><h3 style='margin:0;'>TOP 1%</h3><p style='font-size: 10px;'>YOUR GLOBAL RANK</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### RECENT_TRANSMISSIONS")
    st.markdown("""
        <div class='vantage-card'>
            <h4>NEW_BOUNTY: PYTHON_LEAD_EXTRACTOR</h4>
            <p style='font-size: 11px;'>REWARD: 200_CREDITS | COMPANY: GENISYS_AI | SECTOR: STEM</p>
        </div>
        <div class='vantage-card' style='border-color: #ff00ff;'>
            <h4>SECTOR_UPDATE: GROWTH_MARKETING</h4>
            <p style='font-size: 11px;'>5 NEW SEO AUDITS POSTED | REWARDS INCREASED BY 15%</p>
        </div>
    """, unsafe_allow_html=True)

# --- BOUNTY BOARD ---
elif st.session_state.active_node == 'BOUNTIES':
    st.markdown("<h1>BOUNTY_TERMINAL</h1>", unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
    with col_f1:
        st.text_input("QUERY_DATABASE (SKILL / COMPANY / SECTOR)")
    with col_f2:
        st.selectbox("PAYOUT_THRESHOLD", ["ALL", "> 100", "> 500", "> 1000"])
    with col_f3:
        st.selectbox("RISK_LEVEL", ["ALL", "LOW", "STABLE", "HIGH"])

    # Bounty Cards
    bounties = [
        {"id": "B-001", "name": "Algorithmic Market Intel", "co": "QuantLabs", "pay": "350", "sec": "BIZ", "time": "8h"},
        {"id": "B-002", "name": "Neural Data Sanitizer", "co": "NeuroLink", "pay": "150", "sec": "STEM", "time": "4h"},
        {"id": "B-003", "name": "Viral Growth Loop Script", "co": "TikTokEvolved", "pay": "500", "sec": "MKT", "time": "12h"},
    ]

    for b in bounties:
        st.markdown(f"""
            <div class='vantage-card'>
                <div style='display: flex; justify-content: space-between;'>
                    <div>
                        <h2 style='margin:0; font-size: 18px;'>{b['name']}</h2>
                        <p style='font-size: 10px; color: #00ffff;'>{b['co']} // {b['sec']} // ID: {b['id']}</p>
                    </div>
                    <div style='text-align: right;'>
                        <h2 style='margin:0; font-size: 22px; color: #00ff00 !important;'>{b['pay']} CR</h2>
                        <p style='font-size: 10px;'>DUE: {b['time']}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"DOWNLOAD_BRIEF // {b['id']}", key=b['id'])

# --- SECTORS ---
elif st.session_state.active_node == 'SECTORS':
    st.markdown("<h1>OPERATIONAL_SECTORS</h1>", unsafe_allow_html=True)
    st.write(">> CHOOSE YOUR SPECIALIZATION PATH")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown("""<div class='vantage-card' style='height: 400px;'>
            <h1 style='font-size: 60px;'>💻</h1>
            <h3>STEM_GRID</h3>
            <p>Master Python, SQL, and AI-Human interfaces. Build real code modules for software companies.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE STEM")
    with col_s2:
        st.markdown("""<div class='vantage-card' style='height: 400px; border-color: #ff00ff;'>
            <h1 style='font-size: 60px;'>📈</h1>
            <h3 style='color: #ff00ff !important;'>GROWTH_NODE</h3>
            <p>Weaponize SEO, brand strategy, and social engineering to scale digital entities.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE GROWTH")
    with col_s3:
        st.markdown("""<div class='vantage-card' style='height: 400px; border-color: #f59e0b;'>
            <h1 style='font-size: 60px;'>📊</h1>
            <h3 style='color: #f59e0b !important;'>INTEL_CORE</h3>
            <p>Perform deep-market research, competitive lead extraction, and financial modeling.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE INTEL")

# --- PROTOCOL (ABOUT) ---
elif st.session_state.active_node == 'ABOUT':
    st.markdown("<h1>VANTAGE_PROTOCOL</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["01. THE PROBLEM", "02. THE SOLUTION", "03. THE FUTURE"])
    
    with tab1:
        st.markdown("""
            <h3>>> LEGACY DECAY</h3>
            <p>The current economy uses 'The Network' as a gatekeeper. Talent is everywhere, but opportunity is concentrated in zip codes and pedigrees.</p>
            <p>We are here to destroy the "Experience Loop" (Can't get a job without experience, can't get experience without a job).</p>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown("""
            <h3>>> MICRO-BOUNTIES</h3>
            <p>Vantage atomizes work. Companies post 4-10 hour technical tasks. Students complete them. Students get paid. Students get <b>Verified</b>.</p>
            <p>No interviewing. No bias. Just code, data, and deliverables.</p>
        """, unsafe_allow_html=True)
    with tab3:
        st.markdown("""
            <h3>>> GLOBAL MERITOCRACY</h3>
            <p>A world where a 16-year-old in rural Ohio can out-compete a Harvard graduate because their <b>Verified Portfolio</b> proves they are better.</p>
        """, unsafe_allow_html=True)

# --- IDENTITY (PROFILE) ---
elif st.session_state.active_node == 'PROFILE':
    st.markdown("<h1>NEURAL_IDENTITY</h1>", unsafe_allow_html=True)
    
    p1, p2 = st.columns([1, 2])
    with p1:
        st.markdown("""
            <div style='border: 1px solid #00ffff; padding: 40px; text-align: center;'>
                <h1 style='font-size: 8rem; margin: 0;'>R</h1>
                <h2>ALEX_RIVERA</h2>
                <p>OAKLAND // CA</p>
                <div style='background: #00ffff; color: #000; font-weight: bold; padding: 10px; margin-top: 20px;'>
                    ELITE_RANK: TOP 1%
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("EXPORT_CREDENTIAL_KEY")
        
    with p2:
        st.markdown("### >> VERIFIED_LEDGER")
        ledger = [
            {"task": "Python Data Scraper", "node": "Genisys_AI", "status": "VERIFIED"},
            {"task": "SEO Audit v4", "node": "SmartBread", "status": "VERIFIED"},
            {"task": "Competitive Map", "node": "VentureLink", "status": "PENDING_AUTH"},
        ]
        for item in ledger:
            st.markdown(f"""
                <div style='border-bottom: 1px solid #222; padding: 15px 0;'>
                    <p style='margin:0;'>{item['task']} // NODE: {item['node']} // STATUS: <span style='color: #00ff00;'>{item['status']}</span></p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>### >> COMPETENCY_TREE", unsafe_allow_html=True)
        st.write("STEM: 88%")
        st.progress(0.88)
        st.write("GROWTH: 45%")
        st.progress(0.45)
        st.write("INTEL: 12%")
        st.progress(0.12)
