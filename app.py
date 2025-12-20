import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vantage | Forge Your Future", page_icon="🌉", layout="wide")

# --- PROFESSIONAL SaaS CSS ---
st.markdown("""
    <style>
    /* Professional Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero Section: High Contrast */
    .hero-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 100px 40px;
        border-radius: 24px;
        text-align: center;
        color: white !important;
        margin-bottom: 40px;
    }
    
    .hero-section h1 {
        color: white !important;
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
        margin-bottom: 15px !important;
    }
    
    .hero-section p {
        color: #94a3b8 !important;
        font-size: 1.3rem !important;
        max-width: 800px;
        margin: 0 auto !important;
    }

    /* Navigation Styling */
    .nav-link {
        color: #1e3a8a !important;
        font-weight: 600;
        text-decoration: none;
    }

    /* Professional Card Layout */
    .category-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        text-align: left;
        height: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: 0.3s;
    }
    
    .category-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        border-color: #3b82f6;
    }

    .category-card h3 {
        color: #0f172a !important;
        font-size: 1.5rem !important;
        margin-bottom: 15px !important;
    }

    /* Professional Content Images */
    .about-img {
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 100%;
        height: auto;
    }

    /* Buttons Override */
    .stButton > button {
        border-radius: 12px !important;
        padding: 10px 25px !important;
        font-weight: 600 !important;
        border: none !important;
        background-color: #1e3a8a !important;
        color: white !important;
    }

    .secondary-btn > div > button {
        background-color: #f1f5f9 !important;
        color: #1e3a8a !important;
    }

    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate_to(page_name):
    st.session_state.page = page_name

# --- TOP NAVIGATION BAR ---
col_logo, col_nav = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='color: #1e3a8a; margin:0;'>🌉 VANTAGE</h2>", unsafe_allow_html=True)

with col_nav:
    n1, n2, n3, n4 = st.columns(4)
    if n1.button("Home", key="nav_home"): navigate_to('Home')
    if n2.button("Bounties", key="nav_bounties"): navigate_to('Bounties')
    if n3.button("About Us", key="nav_about"): navigate_to('About')
    if n4.button("Portfolio", key="nav_port"): navigate_to('Portfolio')

st.markdown("<br>", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-section">
            <h1>Experience that speaks louder.</h1>
            <p>Complete technical projects for top-tier companies. Earn verified proof of work that skips the resume line.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🚀 Browse Career Tracks")
    st.write("Click a track to see available projects.")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="category-card">
            <h3>💻 STEM</h3>
            <p style='color: #64748b;'>Python scripts, data automation, and software QA for emerging startups.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Explore Tech", key="go_stem"): navigate_to('Bounties')

    with c2:
        st.markdown("""<div class="category-card">
            <h3>📈 Marketing</h3>
            <p style='color: #64748b;'>SEO keyword audits, growth hacking strategies, and content delivery.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Explore Marketing", key="go_mkt"): navigate_to('Bounties')

    with c3:
        st.markdown("""<div class="category-card">
            <h3>📊 Business</h3>
            <p style='color: #64748b;'>Market research, competitor analysis, and lead generation spreadsheets.</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Explore Business", key="go_biz"): navigate_to('Bounties')

# --- ABOUT PAGE ---
elif st.session_state.page == 'About':
    st.title("Our Mission")
    st.markdown("---")
    
    col_img, col_txt = st.columns([1, 1.2])
    with col_img:
        # High quality image scaled to fit correctly
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800", use_column_width=True)
    
    with col_txt:
        st.markdown("""
        ### Bridging the Experience Gap
        In today's market, you need experience to get a job, but you need a job to get experience. We fixed that.
        
        Vantage is built for the **next generation of talent**—the students from non-target schools and underrepresented communities who have the skills but lack the connections.
        
        ### How it Works
        1. **The Brief:** Companies post technical 'Bounties.'
        2. **The Work:** You complete the task using our professional templates.
        3. **The Proof:** Your work is verified and added to your permanent Vantage Portfolio.
        """)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.title("Your Proof of Work")
    st.write("This is your verified student profile.")
    
    p_col1, p_col2 = st.columns([1, 2])
    with p_col1:
        st.markdown("""<div style='background:#f8fafc; padding:30px; border-radius:20px; border:1px solid #e2e8f0; text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='120'>
            <h2 style='margin-bottom:0;'>Alex Rivera</h2>
            <p style='color:#64748b;'>Oakland, CA</p>
            <hr>
            <p><strong>Rank:</strong> Top 10%</p>
        </div>""", unsafe_allow_html=True)
        
    with p_col2:
        st.subheader("✅ Verified Projects")
        st.info("**SEO Keyword Audit** - SmartBites Bakery (Oct 2024)")
        st.info("**Lead Generation Spreadsheet** - TechFlow AI (Sept 2024)")
        st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
        st.button("Export Shareable Resume Link")

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.title("🎯 Active Bounties")
    st.write("Filter by skill and pick a project.")
    
    st.text_input("🔍 Search skills (e.g. Python, SEO, Excel)")
    
    # Mock Bounty Item
    st.markdown("""<div style='background: white; padding:25px; border-radius:15px; border-left: 6px solid #1e3a8a; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
        <div style='display:flex; justify-content:space-between;'>
            <h4 style='margin:0;'>Technical Lead List Generation</h4>
            <h4 style='margin:0; color:#166534;'>$120</h4>
        </div>
        <p style='color:#64748b; margin: 10px 0;'>Major: Business/STEM | Time: 5 Hours</p>
    </div>""", unsafe_allow_html=True)
    if st.button("Claim Bounty"):
        st.success("Brief sent to your email!")
