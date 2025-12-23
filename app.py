import streamlit as st
import uuid
from datetime import datetime

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="VANTAGE",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# HARD OVERRIDE STYLES
# ===============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Space+Grotesk:wght@300;500&display=swap');

html, body, [class*="css"] {
    background: radial-gradient(circle at top, #0a0f2c, #02030a);
    color: #eaf4ff;
    font-family: 'Space Grotesk', sans-serif;
}

#MainMenu, footer, header {
    visibility: hidden;
}

h1, h2, h3 {
    font-family: 'Orbitron', monospace;
    letter-spacing: 2px;
}

.neon {
    color: #00f6ff;
    text-shadow: 0 0 12px rgba(0,246,255,0.8);
}

.panel {
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.02)
    );
    border: 1px solid rgba(0,246,255,0.25);
    border-radius: 22px;
    padding: 26px;
    box-shadow:
        0 0 30px rgba(0,246,255,0.15),
        inset 0 0 20px rgba(0,246,255,0.05);
    margin-bottom: 28px;
}

.card {
    background: rgba(5, 8, 25, 0.85);
    border: 1px solid rgba(255, 0, 255, 0.25);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 0 25px rgba(255,0,255,0.15);
}

.tag {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: linear-gradient(90deg, #ff00cc, #00f6ff);
    color: black;
    font-size: 12px;
    margin-right: 8px;
}

.xpbar {
    height: 12px;
    background: rgba(255,255,255,0.1);
    border-radius: 999px;
    overflow: hidden;
}

.xpfill {
    height: 100%;
    background: linear-gradient(90deg, #ffb347, #00f6ff);
    box-shadow: 0 0 12px rgba(0,246,255,0.8);
}

button[kind="primary"] {
    background: linear-gradient(90deg, #ff00cc, #00f6ff) !important;
    color: black !important;
    border-radius: 999px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# STATE
# ===============================
if "users" not in st.session_state:
    st.session_state.users = {
        "alex": {"role": "student", "xp": 120},
        "genisys": {"role": "company", "xp": 0}
    }

if "bounties" not in st.session_state:
    st.session_state.bounties = []

if "submissions" not in st.session_state:
    st.session_state.submissions = []

if "user" not in st.session_state:
    st.session_state.user = None

# Normalize
for u in st.session_state.users:
    st.session_state.users[u].setdefault("xp", 0)
    st.session_state.users[u].setdefault("role", "student")

# ===============================
# LOGIN
# ===============================
if not st.session_state.user:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<h1 class='neon'>VANTAGE</h1>", unsafe_allow_html=True)
    st.markdown("### CONNECT TO THE NETWORK")

    user = st.selectbox("IDENTITY", list(st.session_state.users.keys()))
    if st.button("ENTER PROTOCOL"):
        st.session_state.user = user
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

user = st.session_state.user
role = st.session_state.users[user]["role"]
xp = st.session_state.users[user]["xp"]
level = xp // 100 + 1
progress = (xp % 100) / 100

# ===============================
# HEADER HUD
# ===============================
st.markdown(f"""
<div class="panel">
<h2 class="neon">AGENT: {user.upper()}</h2>
<div>ROLE: {role.upper()} · LEVEL {level}</div>
<div class="xpbar">
    <div class="xpfill" style="width:{progress*100}%"></div>
</div>
</div>
""", unsafe_allow_html=True)

mode = st.radio(
    "",
    ["COMMAND", "BOUNTIES", "SUBMIT", "VERIFY", "IDENTITY"],
    horizontal=True
)

# ===============================
# COMMAND
# ===============================
if mode == "COMMAND":
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("### SYSTEM OVERVIEW")

    st.markdown(f"""
- ACTIVE BOUNTIES: **{len(st.session_state.bounties)}**
- VERIFIED PROOFS: **{len([s for s in st.session_state.submissions if s["status"]=="VERIFIED"])}**
""")
    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# BOUNTIES
# ===============================
elif mode == "BOUNTIES":
    if role == "company":
        with st.form("bounty"):
            st.markdown("<div class='panel'>", unsafe_allow_html=True)
            title = st.text_input("MISSION TITLE")
            reward = st.number_input("XP REWARD", 50, 500, 100)
            skills = st.text_input("SKILLS")
            if st.form_submit_button("DEPLOY MISSION"):
                st.session_state.bounties.append({
                    "id": str(uuid.uuid4())[:6],
                    "title": title,
                    "reward": reward,
                    "skills": skills,
                    "company": user,
                    "claimed": None
                })
            st.markdown("</div>", unsafe_allow_html=True)

    for b in st.session_state.bounties:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"## {b['title']}")
        st.markdown(f"<span class='tag'>{b['reward']} XP</span>", unsafe_allow_html=True)
        st.markdown(f"SKILLS: {b['skills']}")
        if role == "student" and not b["claimed"]:
            if st.button("CLAIM", key=b["id"]):
                b["claimed"] = user
        st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# SUBMIT
# ===============================
elif mode == "SUBMIT":
    if role != "student":
        st.warning("ACCESS DENIED")
        st.stop()

    claimed = [b for b in st.session_state.bounties if b["claimed"] == user]
    if not claimed:
        st.info("NO ACTIVE MISSIONS")
        st.stop()

    b = st.selectbox("MISSION", claimed, format_func=lambda x: x["title"])
    with st.form("submit"):
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        link = st.text_input("DELIVERABLE LINK")
        process = st.text_area("PROCESS LOG")
        if st.form_submit_button("TRANSMIT PROOF"):
            st.session_state.submissions.append({
                "id": b["id"],
                "student": user,
                "company": b["company"],
                "reward": b["reward"],
                "link": link,
                "process": process,
                "status": "PENDING"
            })
        st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# VERIFY
# ===============================
elif mode == "VERIFY":
    if role != "company":
        st.warning("ACCESS DENIED")
        st.stop()

    for s in st.session_state.submissions:
        if s["company"] != user:
            continue

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"## TASK {s['id']} — {s['student']}")
        st.markdown(s["link"])
        if s["status"] == "PENDING":
            if st.button("VERIFY", key="v"+s["id"]):
                s["status"] = "VERIFIED"
                st.session_state.users[s["student"]]["xp"] += s["reward"]
        st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# IDENTITY
# ===============================
elif mode == "IDENTITY":
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("### VERIFIED PROOF-OF-WORK")

    proofs = [
        s for s in st.session_state.submissions
        if s["student"] == user and s["status"] == "VERIFIED"
    ]

    if not proofs:
        st.info("NO VERIFIED PROOFS")
    else:
        for p in proofs:
            st.markdown(f"- `{p['id']}` · {p['company']} · +{p['reward']} XP")
    st.markdown("</div>", unsafe_allow_html=True)
