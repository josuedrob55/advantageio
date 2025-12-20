import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vantage | Forge Your Future", page_icon="🌉", layout="wide")

# --- HIGH-CONTRAST SaaS CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* 1. GLOBAL TEXT RULES (Prevents Blue-on-Navy) */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #1e293b; /* Default: Dark Slate for White backgrounds */
    }

    /* 2. HERO SECTION: Clean Contrast */
    .hero-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 90px 40px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 50px;
    }
    
    /* Force text inside Hero to be White/Light only */
    .hero-section h1 {
        color: #ffffff !important;
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        margin-bottom: 20px !important;
    }
    
    .hero-section p {
        color: #e2e8f0 !important; /* Light Silver */
        font-size: 1.3rem !important;
        max-width: 800px;
        margin: 0 auto !important;
        line-height: 1.6;
    }

    /* 3. CARD DESIGN: Dark Text on Light Paper */
    .category-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
        text-align: left;
    }
    
    .category-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
        border-color: #3b82f6;
    }

    .category-card h3 {
        color: #0f172a !important; /* Bold Black-Slate */
        font-weight: 700 !important;
    }

    .category-card p {
        color: #475569 !important; /* Slate Grey for body text */
    }

    /* 4. NAVIGATION: Clean Slate */
    .nav-btn > div > button {
        background: none !important;
        border: none !important;
        color: #1e3a8a !important; /* Navy text on white header */
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    
    .nav-btn > div > button:hover {
        color: #3b82f6 !important;
        text-decoration: underline !important;
    }

    /* 5. PRIMARY BUTTONS */
    .stButton > button {
        border-radius: 12px !important;
        background-color: #1e3a8a !important;
        color: #ffffff !important; /* Pure White text on Blue buttons */
        border: none !important;
        font-weight: 600 !important;
        height: 45px;
    }
    
    .stButton > button:hover {
        background-color: #000000 !important;
        color: white !important;
    }

    /* Fix for Streamlit's default "Blue" links/text */
    h1, h2, h3, h4, h5, h6 { color: #0f172a !important; }
    
    /* Hide Streamlit Header Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate(page_name):
    st.session_state.page = page_name

# --- TOP NAVIGATION BAR ---
t1, t2 = st.columns([1, 1.5])
with t1:
    st.markdown("<h2 style='color: #1e3a8a; margin:0; font-weight:800; cursor:pointer;'>🌉 VANTAGE</h2>", unsafe_allow_html=True)

with t2:
    n1, n2, n3, n4 = st.columns(4)
    with n1: 
        if st.button("Home", key="n_h"): navigate('Home')
    with n2:
        if st.button("Explore", key="n_e"): navigate('Bounties')
    with n3:
        if st.button("Mission", key="n_m"): navigate('About')
    with n4:
        if st.button("Portfolio", key="n_p"): navigate('Portfolio')

st.markdown("<br>", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-section">
            <h1>Proof of skill is the <br>new pedigree.</h1>
            <p>Skip the networking. Complete technical bounties for top companies and build a verified portfolio that opens doors.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center; margin-bottom:40px; color:#0f172a;'>Select Your Career Track</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="category-card">
            <span style='font-size:40px;'>💻</span>
            <h3 style='margin-top:15px;'>STEM & Data</h3>
            <p>Build automation scripts, perform QA testing, or clean data for scaling AI startups.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Open Tech Bounties", key="go_s", use_container_width=True)

    with c2:
        st.markdown("""<div class="category-card">
            <span style='font-size:40px;'>📈</span>
            <h3 style='margin-top:15px;'>Growth & Marketing</h3>
            <p>Execute SEO audits, design social kits, and build growth funnels for real brands.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Open Marketing Bounties", key="go_m", use_container_width=True)

    with c3:
        st.markdown("""<div class="category-card">
            <span style='font-size:40px;'>📊</span>
            <h3 style='margin-top:15px;'>Business Ops</h3>
            <p>Conduct competitor research, build lead lists, and create high-stakes pitch decks.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Open Business Bounties", key="go_b", use_container_width=True)

# --- MISSION PAGE ---
elif st.session_state.page == 'About':
    st.markdown("<h1 style='text-align:center;'>Our Mission</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 1.2], gap="large")
    with col_img:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800")
    
    with col_txt:
        st.markdown("""
        <h2 style='margin-top:0;'>Bridging the Experience Gap</h2>
        <p style='font-size:1.1rem; color:#475569;'>The world's best talent isn't always at the best schools. It's often hidden in communities without a direct path to tech.</p>
        <p style='font-size:1.1rem; color:#475569;'>Vantage is a <b>Work-Experience Marketplace</b>. We connect startups needing fast technical work with students who need real entries on their resume.</p>
        <hr style='border: 0.5px solid #e2e8f0;'>
        <h4 style='color:#0f172a;'>The Outcome</h4>
        <p style='color:#475569;'>Students earn cash and a <b>'Verified Proof of Work'</b>—a permanent digital credential that proves their skill level to any employer.</p>
        """, unsafe_allow_html=True)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.markdown("<h1 style='text-align:center;'>Digital Portfolio</h1>", unsafe_allow_html=True)
    
    p_col1, p_col2 = st.columns([1, 2], gap="large")
    with p_col1:
        st.markdown("""<div style='background:#ffffff; padding:40px; border-radius:30px; border:1px solid #e2e8f0; text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='140'>
            <h2 style='margin-top:20px; color:#0f172a;'>Alex Rivera</h2>
            <p style='color:#64748b;'>Oakland, CA | Student</p>
            <div style='background:#f1f5f9; padding:15px; border-radius:12px; margin:20px 0;'>
                <p style='margin:0; font-weight:700; color:#1e3a8a;'>Rank: Top 10% Overall</p>
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("Share Portfolio Link", use_container_width=True)
        
    with p_col2:
        st.subheader("✅ Verified Proof of Work")
        st.markdown("""
            <div style='background:white; padding:25px; border-radius:15px; border:1px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0; color:#0f172a;'>Python Lead-Gen Script</h4>
                <p style='color:#64748b; margin:5px 0;'>Employer: TechFlow AI • Oct 2024</p>
            </div>
            <div style='background:white; padding:25px; border-radius:15px; border:1px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0; color:#0f172a;'>SEO Competitor Analysis</h4>
                <p style='color:#64748b; margin:5px 0;'>Employer: SmartBites Bakery • Sept 2024</p>
            </div>
        """, unsafe_allow_html=True)

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.markdown("<h1 style='text-align:center;'>Active Bounties</h1>", unsafe_allow_html=True)
    st.text_input("🔍 Search skills or companies...")
    
    # Bounty Card 1
    st.markdown("""
        <div style='background: white; padding:35px; border-radius:24px; border:1px solid #e2e8f0; border-left: 10px solid #1e3a8a; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-top:20px;'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <h3 style='margin:0; color:#0f172a;'>Market Research Strategy Deck</h3>
                    <p style='color:#64748b; margin-top:8px; font-size:1.1rem;'>Track: Business Ops | Est. Time: 6 Hours</p>
                </div>
                <div style='text-align:right;'>
                    <h2 style='margin:0; color:#166534;'>$150</h2>
                    <p style='color:#64748b; margin:0;'>Guaranteed Reward</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Claim Bounty Brief", key="b_claim")
