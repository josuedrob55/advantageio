import streamlit as st
import uuid
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="VANTAGE // PROTOCOL",
    page_icon="🧬",
    layout="wide"
)

# =====================================================
# CYBER UI STYLES
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&family=Inter:wght@300;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #05070d;
    color: #e6f1ff;
}

h1, h2, h3 {
    font-family: 'Orbitron', monospace;
    letter-spacing: 1px;
}

.glass {
    background: rgba(15, 20, 40, 0.6);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(0, 255, 255, 0.15);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
}

.neon {
    color: #00f6ff;
}

.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 12px;
    margin-right: 6px;
    background: linear-gradient(90deg, #ff00cc, #00f6ff);
    color: black;
}

.xp {
    color: #ffb347;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='neon'>VANTAGE // PROTOCOL</h1>", unsafe_allow_html=True)

# =====================================================
# STATE INIT
# =====================================================
if "users" not in st.session_state:
    st.session_state.users = {
        "alex": {"role": "student", "xp": 120, "level": 2},
        "genisys": {"role": "company", "xp": 0, "level": 0}
    }

if "bounties" not in st.session_state:
    st.session_state.bounties = []

if "submissions" not in st.session_state:
    st.session_state.submissions = []

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# Normalize users (prevents ALL KeyErrors)
for u in st.session_state.users:
    st.session_state.users[u].setdefault("xp", 0)
    st.session_state.users[u].setdefault("level", 1)
    st.session_state.users[u].setdefault("role", "student")

# =====================================================
# LOGIN
# =====================================================
if not st.session_state.current_user:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("CONNECT TO VANTAGE")

    user = st.selectbox("IDENTITY", list(st.session_state.users.keys()))
    if st.button("CONNECT"):
        st.session_state.current_user = user
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

user = st.session_state.current_user
role = st.session_state.users[user]["role"]
xp = st.session_state.users[user]["xp"]
level = st.session_state.users[user]["level"]

# =====================================================
# SIDEBAR HUD
# =====================================================
st.sidebar.markdown(f"### 🧠 `{user.upper()}`")
st.sidebar.markdown(f"ROLE: `{role.upper()}`")
st.sidebar.markdown(f"<span class='xp'>XP: {xp}</span>", unsafe_allow_html=True)
st.sidebar.progress(min(xp % 100 / 100, 1.0))
st.sidebar.markdown(f"LEVEL {level}")

if st.sidebar.button("DISCONNECT"):
    st.session_state.current_user = None
    st.rerun()

page = st.sidebar.radio(
    "NAV",
    ["Command Center", "Bounty Terminal", "Submit Proof", "Validate", "Neural Identity"]
)

# =====================================================
# COMMAND CENTER
# =====================================================
if page == "Command Center":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("SYSTEM STATUS")

    st.metric("ACTIVE BOUNTIES", len(st.session_state.bounties))
    st.metric(
        "VERIFIED PROOFS",
        len([s for s in st.session_state.submissions if s["status"] == "VERIFIED"])
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# BOUNTY TERMINAL
# =====================================================
elif page == "Bounty Terminal":
    st.subheader("BOUNTY TERMINAL")

    if role == "company":
        with st.form("new_bounty"):
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            title = st.text_input("TASK NAME")
            reward = st.number_input("XP REWARD", 50, 500, 100)
            skills = st.text_input("SKILLS (comma separated)")
            hours = st.selectbox("TIME", ["4–6h", "6–8h", "8–10h"])
            if st.form_submit_button("DEPLOY"):
                st.session_state.bounties.append({
                    "id": str(uuid.uuid4())[:8],
                    "title": title,
                    "reward": reward,
                    "skills": skills,
                    "hours": hours,
                    "company": user,
                    "claimed_by": None
                })
                st.success("BOUNTY DEPLOYED")
            st.markdown("</div>", unsafe_allow_html=True)

    for b in st.session_state.bounties:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.markdown(f"### {b['title']}")
        st.markdown(f"XP: `{b['reward']}` | TIME: `{b['hours']}`")
        st.markdown(f"SKILLS: {b['skills']}")
        st.markdown(f"COMPANY: `{b['company']}`")

        if role == "student" and not b["claimed_by"]:
            if st.button(f"CLAIM {b['id']}", key=b["id"]):
                b["claimed_by"] = user
                st.success("BOUNTY CLAIMED")
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# SUBMIT PROOF
# =====================================================
elif page == "Submit Proof":
    if role != "student":
        st.warning("STUDENT ONLY")
        st.stop()

    claimed = [b for b in st.session_state.bounties if b["claimed_by"] == user]

    if not claimed:
        st.info("NO CLAIMED BOUNTIES")
        st.stop()

    bounty = st.selectbox("SELECT BOUNTY", claimed, format_func=lambda x: x["title"])

    with st.form("submit"):
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        link = st.text_input("DELIVERABLE LINK")
        process = st.text_area("PROCESS LOG (MIN 50 CHARS)")
        if st.form_submit_button("TRANSMIT"):
            if len(process) < 50:
                st.error("PROCESS LOG TOO SHORT")
            else:
                st.session_state.submissions.append({
                    "id": bounty["id"],
                    "student": user,
                    "company": bounty["company"],
                    "reward": bounty["reward"],
                    "link": link,
                    "process": process,
                    "status": "PENDING",
                    "timestamp": datetime.utcnow()
                })
                st.success("SUBMISSION SENT")
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# VALIDATE
# =====================================================
elif page == "Validate":
    if role != "company":
        st.warning("COMPANY ONLY")
        st.stop()

    for s in st.session_state.submissions:
        if s["company"] != user:
            continue

        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.markdown(f"### TASK `{s['id']}` — {s['student']}")
        st.markdown(f"[DELIVERABLE]({s['link']})")
        with st.expander("PROCESS LOG"):
            st.write(s["process"])

        if s["status"] == "PENDING":
            c1, c2 = st.columns(2)
            if c1.button("VERIFY", key="v"+s["id"]):
                s["status"] = "VERIFIED"
                stu = s["student"]
                st.session_state.users[stu]["xp"] += s["reward"]
                st.session_state.users[stu]["level"] = (
                    st.session_state.users[stu]["xp"] // 100 + 1
                )
                st.success("VERIFIED")
            if c2.button("REJECT", key="r"+s["id"]):
                s["status"] = "REJECTED"
                st.error("REJECTED")
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# NEURAL IDENTITY
# =====================================================
elif page == "Neural Identity":
    st.subheader("NEURAL IDENTITY")

    proofs = [
        s for s in st.session_state.submissions
        if s["student"] == user and s["status"] == "VERIFIED"
    ]

    if not proofs:
        st.info("NO VERIFIED PROOFS YET")
    else:
        for p in proofs:
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            st.markdown(f"### `{p['id']}`")
            st.markdown(f"COMPANY: `{p['company']}`")
            st.markdown(f"<span class='badge'>VERIFIED</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
