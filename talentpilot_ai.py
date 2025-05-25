# talentpilot_ai.py

import streamlit as st

st.set_page_config(page_title="TalentPilot AI", layout="centered")

st.title("🚀 TalentPilot AI")
st.subheader("Your On-Demand Recruiting Assistant")

st.markdown("Use this AI-powered tool to create cold outreach emails, job descriptions, and summaries in seconds.")

st.sidebar.header("Choose a Feature")

feature = st.sidebar.radio("Select one:", [
    "Cold Outreach Generator",
    "Job Description Builder",
    "Resume Summary Tool",
    "Follow-Up Cadence Writer"
])

# Simulated GPT Output Function
def generate_response(feature, inputs):
    if feature == "Cold Outreach Generator":
        return f"""
        Hi {inputs.get('name', '[Candidate Name]')},

        I came across your profile and was impressed with your experience in {inputs.get('skill', '[Python and AWS]')}. 
        We’re hiring a {inputs.get('role', '[Senior Backend Engineer]')} for a fast-growing startup.

        If you're open to a chat, I'd love to share more. Let me know!

        Best,  
        {inputs.get('recruiter', '[Your Name]')}
        """
    elif feature == "Job Description Builder":
        return f"""
        **Role: {inputs.get('title', 'Senior Backend Engineer')}**

        Our client, a growing tech startup, is looking for a skilled engineer with strong experience in {inputs.get('skills', 'Python and AWS')}. 
        The ideal candidate will thrive in remote environments and contribute to scalable backend systems.

        Benefits include competitive salary, remote flexibility, and a collaborative team culture.
        """
    elif feature == "Resume Summary Tool":
        return """
        - 8+ years of backend development with Python, Django, and AWS.  
        - Led migration of legacy systems, improving performance by 40%.  
        - Strong communication and leadership skills; quick to onboard and mentor juniors.
        """
    elif feature == "Follow-Up Cadence Writer":
        return """
        **Email 1:** Just checking in to see if you had a chance to consider the role I sent. Let me know if you’re open to chatting.

        **Email 2 (3 days later):** Still interested in connecting – this is a high-impact opportunity at a fast-scaling team.

        **Email 3 (7 days later):** No worries if now’s not the right time. I’ll stay in touch with other opportunities down the line!
        """
    else:
        return "Feature not recognized."

# UI Logic
if feature == "Cold Outreach Generator":
    st.header("📬 Cold Outreach Generator")
    name = st.text_input("Candidate Name")
    role = st.text_input("Role You're Hiring For")
    skill = st.text_input("Key Skills You're Targeting")
    recruiter = st.text_input("Your Name")
    
    if st.button("Generate Email"):
        output = generate_response(feature, {
            "name": name,
            "role": role,
            "skill": skill,
            "recruiter": recruiter
        })
        st.text_area("Generated Email:", output, height=250)

elif feature == "Job Description Builder":
    st.header("📝 Job Description Builder")
    title = st.text_input("Job Title")
    skills = st.text_area("List Key Responsibilities and Skills")

    if st.button("Generate JD"):
        output = generate_response(feature, {"title": title, "skills": skills})
        st.text_area("Generated JD:", output, height=250)

elif feature == "Resume Summary Tool":
    st.header("📄 Resume Summary Tool")
    resume = st.text_area("Paste Resume Text Below")

    if st.button("Generate Summary"):
        output = generate_response(feature, {"resume": resume})
        st.text_area("Generated Summary:", output, height=250)

elif feature == "Follow-Up Cadence Writer":
    st.header("📆 Follow-Up Cadence Writer")
    st.markdown("No inputs needed — generates a simple 3-message sequence.")

    if st.button("Generate Cadence"):
        output = generate_response(feature, {})
        st.text_area("Generated Follow-Up:", output, height=250)
