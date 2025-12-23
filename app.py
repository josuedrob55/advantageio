import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="VANTAGE // PROTOCOL",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# IN-MEMORY DATABASE (MVP)
# -----------------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "alex": {"role": "student"},
        "genisys": {"role": "company"}
    }

if "bounties" not in st.session_state:
    st.session_state.bounties = []

if "submissions" not in st.session_state:
    st.session_state.submissions = []

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# -----------------------------
# AUTH
# -----------------------------
def login():
    st.sidebar.subheader("LOGIN")
    user = st.sidebar.text_input("HANDLE")
    if st.sidebar.button("CONNECT"):
        if user in st.session_state.users:
            st.session_state.current_user = user
        else:
            st.sidebar.error("USER NOT FOUND")

def logout():
    st.session_state.current_user = None

# -----------------------------
# NAV
# -----------------------------
if not st.session_state.current_user:
    login()
    st.stop()

user = st.session_state.current_user
role = st.session_state.users[user]["role"]

st.sidebar.markdown(f"**USER:** `{user.upper()}`")
st.sidebar.markdown(f"**ROLE:** `{role.upper()}`")
if st.sidebar.button("DISCONNECT"):
    logout()
    st.stop()

page = st.sidebar.radio(
    "NAV",
    ["Dashboard", "Bounties", "Submit Work", "Verify Work", "Neural Identity"]
)

# -----------------------------
# DASHBOARD
# -----------------------------
if page == "Dashboard":
    st.title("COMMAND_CENTER")
    st.metric("ACTIVE BOUNTIES", len(st.session_state.bounties))
    st.metric("VERIFIED WORK", len([s for s in st.session_state.submissions if s["status"] == "VERIFIED"]))

# -----------------------------
# BOUNTIES
# -----------------------------
elif page == "Bounties":
    st.title("BOUNTY_TERMINAL")

    if role == "company":
        st.subheader("POST BOUNTY")
        with st.form("post"):
            title = st.text_input("TASK")
            reward = st.number_input("REWARD", min_value=50)
            hours = st.selectbox("TIME", ["4–6h", "6–8h", "8–10h"])
            skills = st.text_input("SKILLS (comma separated)")
            if st.form_submit_button("DEPLOY"):
                st.session_state.bounties.append({
                    "id": str(uuid.uuid4())[:8],
                    "title": title,
                    "reward": reward,
                    "hours": hours,
                    "skills": skills,
                    "company": user,
                    "claimed_by": None
                })

    st.subheader("AVAILABLE BOUNTIES")
    for b in st.session_state.bounties:
        st.markdown(f"""
        **{b['title']}**  
        `{b['id']}` | {b['reward']} CR | {b['hours']}  
        SKILLS: {b['skills']}  
        COMPANY: {b['company']}
        """)
        if role == "student" and not b["claimed_by"]:
            if st.button(f"CLAIM {b['id']}"):
                b["claimed_by"] = user

# -----------------------------
# SUBMISSION
# -----------------------------
elif page == "Submit Work":
    if role != "student":
        st.warning("STUDENTS ONLY")
        st.stop()

    st.title("SUBMIT_DELIVERABLE")

    claimed = [b for b in st.session_state.bounties if b["claimed_by"] == user]

    if not claimed:
        st.info("NO CLAIMED BOUNTIES")
        st.stop()

    bounty = st.selectbox("SELECT BOUNTY", claimed, format_func=lambda x: x["title"])

    with st.form("submit"):
        link = st.text_input("DELIVERABLE LINK (GitHub / Drive)")
        process = st.text_area("PROCESS LOG (REQUIRED)")
        if st.form_submit_button("TRANSMIT"):
            if len(process) < 50:
                st.error("PROCESS LOG TOO SHORT")
            else:
                st.session_state.submissions.append({
                    "id": bounty["id"],
                    "student": user,
                    "company": bounty["company"],
                    "link": link,
                    "process": process,
                    "status": "PENDING",
                    "timestamp": datetime.utcnow()
                })

# -----------------------------
# VERIFICATION
# -----------------------------
elif page == "Verify Work":
    if role != "company":
        st.warning("COMPANIES ONLY")
        st.stop()

    st.title("VALIDATION_QUEUE")

    queue = [s for s in st.session_state.submissions if s["company"] == user]

    for s in queue:
        st.markdown(f"""
        **TASK:** `{s['id']}`  
        STUDENT: {s['student']}  
        LINK: {s['link']}  
        STATUS: {s['status']}
        """)
        with st.expander("PROCESS LOG"):
            st.write(s["process"])

        if s["status"] == "PENDING":
            col1, col2 = st.columns(2)
            if col1.button(f"VERIFY {s['id']}"):
                s["status"] = "VERIFIED"
            if col2.button(f"REJECT {s['id']}"):
                s["status"] = "REJECTED"

# -----------------------------
# NEURAL IDENTITY
# -----------------------------
elif page == "Neural Identity":
    st.title("NEURAL_IDENTITY")

    ledger = [s for s in st.session_state.submissions if s["student"] == user and s["status"] == "VERIFIED"]

    st.subheader("VERIFIED LEDGER")
    if not ledger:
        st.write("NO VERIFIED WORK")
    else:
        for l in ledger:
            st.markdown(f"""
            `{l['id']}` | VERIFIED  
            COMPANY: {l['company']}  
            """)
