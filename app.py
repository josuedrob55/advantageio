import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vantage | Forge Your Future", page_icon="🌉", layout="wide")

# --- CLEAN WHITE & HIGH CONTRAST CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* 1. GLOBAL RESET TO WHITE BACKGROUND */
    .stApp {
        background-color: #ffffff !important;
    }

    /* 2. UNIVERSAL TEXT VISIBILITY (High Contrast) */
    html, body, [class*="st-"], .stMarkdown {
        font-family: 'Inter', sans-serif;
        color: #0f172a !important; /* Extremely dark navy for crisp reading */
    }

    /* Remove Streamlit default header/footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 3. MINIMALIST WHITE HERO SECTION */
    .hero-container {
        padding: 80px 20px;
        text-align: center;
        background-color: #ffffff;
        border-bottom: 1px solid #f1f5f9;
        margin-bottom: 40px;
    }
    
    .hero-container h1 {
        color: #0f172a !important;
        font-size: 4rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 25px !important;
    }
    
    .hero-container p {
        color: #475569 !important; /* Slate Grey for subtext */
        font-size: 1.4rem !important;
        max-width: 800px;
        margin: 0 auto !important;
        line-height: 1.6;
    }

    /* 4. PROFESSIONAL CARDS */
    .category-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
        text-align: left;
    }
    
    .category-card:hover {
        border-color: #1e3a8a;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.05);
        transform: translateY(-5px);
    }

    .category-card h3 {
        color: #1e3a8a !important; /* Navy for headers */
        font-weight: 700 !important;
        margin-top: 15px !important;
    }

    .category-card p {
        color: #334155 !important; /* Dark slate for card text */
    }

    /* 5. PRIMARY BUTTONS (Dark Navy with White Text) */
    .stButton > button {
        background-color: #0f172a !important;
        color: #ffffff !important; /* Pure white text on dark button */
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        width: 100%;
        transition: 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #3b82f6 !important;
        color: #ffffff !important;
    }

    /* 6. NAV BUTTONS (Clean text links) */
    .nav-btn > div > button {
        background: none !important;
        color: #0f172a !important;
        border: none !important;
        font-weight: 600 !important;
    }

    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate(page_name):
    st.session_state.page = page_name

# --- TOP NAVIGATION BAR ---
col_logo, col_nav = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='color: #0f172a; margin:0; font-weight:800; letter-spacing:-1px;'>🌉 VANTAGE</h2>", unsafe_allow_html=True)

with col_nav:
    n1, n2, n3, n4 = st.columns(4)
    if n1.button("Home", key="n1"): navigate('Home')
    if n2.button("Bounties", key="n2"): navigate('Bounties')
    if n3.button("Mission", key="n3"): navigate('About')
    if n4.button("Portfolio", key="n4"): navigate('Portfolio')

st.markdown("<hr style='margin:0; border: 0.1px solid #f1f5f9;'>", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-container">
            <h1>Experience is the <br>New Credential.</h1>
            <p>Complete professional technical tasks for growing startups. Build a verified portfolio that bypasses the traditional resume screen.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align:center; margin-bottom:40px; color:#0f172a;'>Choose Your Career Track</h3>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="category-card">
            <span style='font-size:35px;'>💻</span>
            <h3>STEM & Data</h3>
            <p>Build automation scripts, clean data, and perform QA testing for scaling AI startups.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Explore Tech", key="b_s")

    with c2:
        st.markdown("""<div class="category-card">
            <span style='font-size:35px;'>📈</span>
            <h3>Marketing</h3>
            <p>Develop SEO keyword maps, social kit audits, and growth funnels for real-world brands.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Explore Growth", key="b_m")

    with c3:
        st.markdown("""<div class="category-card">
            <span style='font-size:35px;'>📊</span>
            <h3>Business Ops</h3>
            <p>Conduct market research, competitor analysis, and lead generation for high-stakes teams.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Explore Business", key="b_b")

# --- MISSION PAGE ---
elif st.session_state.page == 'About':
    st.markdown("<h1 style='margin-top:40px; text-align:center;'>Our Mission</h1>", unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 1], gap="large")
    with col_img:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800")
    
    with col_txt:
        st.markdown("""
        <h2 style='color:#0f172a;'>Solving the "Experience Catch-22"</h2>
        <p style='font-size:1.1rem;'>You need experience to get a job, but you need a job to get experience. We’re here to break that cycle.</p>
        <p style='font-size:1.1rem;'>Vantage connects students—particularly those from underrepresented backgrounds—with 'Micro-Bounties'. These are real technical tasks that startups need help with today.</p>
        <hr style='border: 0.1px solid #e2e8f0;'>
        <h4 style='color:#1e3a8a;'>The Result</h4>
        <p>Every completed project earns you a <b>'Verified Proof of Work'</b>—a permanent digital credential that proves your skill to any employer, anywhere.</p>
        """, unsafe_allow_html=True)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.markdown("<h1 style='margin-top:40px; text-align:center;'>Student Portfolio</h1>", unsafe_allow_html=True)
    
    p_col1, p_col2 = st.columns([1, 2], gap="large")
    with p_col1:
        st.markdown("""<div style='background:#f8fafc; padding:40px; border-radius:24px; border:1px solid #e2e8f0; text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='130'>
            <h2 style='margin-top:20px; color:#0f172a;'>Alex Rivera</h2>
            <p style='color:#64748b;'>Oakland, CA | Student</p>
            <div style='background:#ffffff; border:1px solid #cbd5e1; padding:15px; border-radius:12px; margin:20px 0;'>
                <p style='margin:0; font-weight:700; color:#1e3a8a;'>Vantage Rank: Top 10%</p>
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("Copy Public Profile Link", key="copy_link")
        
    with p_col2:
        st.subheader("✅ Verified Projects")
        st.markdown("""
            <div style='background:white; padding:25px; border-radius:16px; border:1px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0; color:#0f172a;'>Python Automation Script</h4>
                <p style='color:#475569; margin:5px 0;'>Employer: TechFlow AI • Verified Oct 2024</p>
            </div>
            <div style='background:white; padding:25px; border-radius:16px; border:1px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0; color:#0f172a;'>SEO Content Strategy Audit</h4>
                <p style='color:#475569; margin:5px 0;'>Employer: SmartBites Bakery • Verified Sept 2024</p>
            </div>
        """, unsafe_allow_html=True)

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.markdown("<h1 style='margin-top:40px;'>Active Bounties</h1>", unsafe_allow_html=True)
    st.text_input("🔍 Search skills or companies...")
    
    st.markdown("""
        <div style='background: #f8fafc; padding:30px; border-radius:20px; border:1px solid #e2e8f0; border-left: 8px solid #0f172a; margin-top:25px;'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <h3 style='margin:0; color:#0f172a;'>Technical Lead List Generation</h3>
                    <p style='color:#475569; margin-top:5px; font-size:1.1rem;'>Track: Business Ops | Est. Time: 5 Hours</p>
                </div>
                <div style='text-align:right;'>
                    <h2 style='margin:0; color:#15803d;'>$120</h2>
                    <p style='color:#64748b; margin:0;'>Reward</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Claim Bounty Brief", key="b1_claim")
