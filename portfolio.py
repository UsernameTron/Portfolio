import streamlit as st
from PIL import Image
import os
import base64
import matplotlib.pyplot as plt
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Digital Portfolio | C. Pete Connor", page_icon="🏆", layout="wide")

# --- File Paths ---
FILES = {
    "profile_pic": "profile-pic.png",         # Root directory
    "resume": "cv_cpeteconnor.pdf",           # Root directory
    "audio_summary": "Celebrity Endorsement.mp3"  # Root directory
}

# --- Helper Functions ---
def load_file(file_path):
    """Load a file if it exists, or return None."""
    try:
        with open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return None

def display_bar_chart(title, data, xlabel, ylabel):
    """Create a horizontal bar chart using matplotlib."""
    st.markdown(f"### {title}")
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df["Category"], df["Value"], color="skyblue")
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_xticks(range(len(df["Category"])))
    ax.set_xticklabels(df["Category"], rotation=45, ha="right")
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    st.pyplot(fig)

# --- Hero Section ---
st.title("C. Pete Connor: Digital Portfolio")
col1, col2 = st.columns([1, 2])

# Display Profile Picture
profile_pic_data = load_file(FILES["profile_pic"])
if profile_pic_data:
    with col1:
        profile_pic = Image.open(FILES["profile_pic"])
        st.image(profile_pic, caption="C. Pete Connor", use_container_width=True)
else:
    st.warning("Profile picture not found.")

# Description and Resume Download
with col2:
    st.write("""
    **Customer Experience Leader | AI Strategist | Operational Excellence**  
    Delivering innovative solutions and measurable results in customer experience and operational transformation.
    """)
    st.markdown("[📧 Email Me](mailto:cpeteconnor@gmail.com) | [🔗 LinkedIn](https://linkedin.com/in/cpeteconnor)")

    resume_data = load_file(FILES["resume"])
    if resume_data:
        st.download_button(
            label="📄 Download My Resume Highlights",
            data=resume_data,
            file_name="resume_visualization.pdf",
            mime="application/pdf",
        )
    else:
        st.warning("Resume file not found.")

# --- MP3 Audio Section ---
st.markdown("---")
st.subheader("🎧 Listen to a Summary of My Portfolio")
st.write("Experience a quick audio overview of my career highlights and achievements:")

audio_data = load_file(FILES["audio_summary"])
if audio_data:
    st.audio(audio_data, format="audio/mp3")
else:
    st.warning("Audio file not found.")

# --- Certifications Section ---
st.markdown("## 🎓 Certifications")
certifications_data = [
    {"Category": "AI & Data Science", "Value": 4},
    {"Category": "Leadership & Management", "Value": 4},
    {"Category": "Productivity & Personal Development", "Value": 3},
    {"Category": "Customer Experience", "Value": 1},
    {"Category": "Technical Skills", "Value": 2},
    {"Category": "Process Improvement", "Value": 2},
    {"Category": "Public Speaking", "Value": 1},
    {"Category": "Public Recognition", "Value": 1},
]
display_bar_chart("Certifications by Category", certifications_data, xlabel="Category", ylabel="Certifications Count")

# --- Key Projects and Achievements ---
st.markdown("## 🏆 Key Projects and Achievements")
projects_data = [
    {"Category": "Feedback System Implementation", "Value": 93},
    {"Category": "CX Roadmap Development", "Value": 20},
    {"Category": "KPI Tracking", "Value": 25},
    {"Category": "SOP Documentation", "Value": 10},
    {"Category": "Cross-Functional Collaboration", "Value": 10},
]
display_bar_chart("Key Projects and Achievements", projects_data, xlabel="Projects", ylabel="Impact (%)")

# --- Technical Proficiencies ---
st.markdown("## 💻 Technical Proficiencies")
tech_proficiencies = {
    "AI & Machine Learning": "Python, TensorFlow, scikit-learn",
    "CRM & CX Platforms": "Zendesk, Totango, RingCentral, Salesforce",
    "Data Visualization": "Power BI, Tableau, Excel, Google Sheets",
    "Database Management": "SQL",
    "Communication Tools": "Slack, Microsoft Teams, Zoom",
    "Project Management": "Asana, Trello, Jira"
}
cols = st.columns(2)
for i, (category, tools) in enumerate(tech_proficiencies.items()):
    with cols[i % 2]:
        st.markdown(f"**{category}**")
        st.write(tools)

# --- Testimonials Section ---
st.markdown("## 💬 Professional Recommendations")
testimonials = [
    {"name": "Darren Prine", "title": "CX Solutions Guru", "comment": "Pete's expertise in AI-driven analytics and predictive modeling has delivered millions in revenue by reducing churn and boosting NPS."},
    {"name": "Michele Crocker", "title": "Digital Transformation Expert", "comment": "Pete connects people, processes, and technology to drive measurable results. A true leader with a growth mindset."},
    {"name": "John Jarvis", "title": "VP Client Services", "comment": "Pete builds high-performing teams, identifies issues quickly, and enhances processes for better efficiency."},
    {"name": "Angela McKenzie", "title": "Surgery Scheduler", "comment": "One of the most supportive and talented leaders I’ve worked under."},
    {"name": "Shawn Foley", "title": "Healthcare Executive", "comment": "Pete is a consummate professional—great leader with humor and results-driven attitude."},
    {"name": "Tina M. Martino", "title": "Director, Healogics", "comment": "Pete’s profound knowledge of call center operations and technology sets him apart as a top asset."},
]
cols = st.columns(2)
for i, t in enumerate(testimonials):
    with cols[i % 2]:
        st.markdown(f"**{t['name']}** - *{t['title']}*")
        st.info(f"_{t['comment']}_")

# --- Footer ---
st.markdown("---")
st.markdown("""
**Let’s connect and discuss how I can drive success for your organization.**  
*Your future transformation starts here!* 🚀
""")
