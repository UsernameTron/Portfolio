import streamlit as st
from PIL import Image, UnidentifiedImageError  # For handling images
from io import BytesIO  # For binary data
import os
import matplotlib.pyplot as plt  # For bar charts
import pandas as pd  # For data processing
import plotly.express as px  # For dynamic visualizations

# --- Page Configuration ---
st.set_page_config(page_title="Digital Portfolio | C. Pete Connor", page_icon=None, layout="wide")

# --- File Paths ---
FILES = {
    "profile_pic": "profile-pic.png",
    "resume": "cv_cpeteconnor.pdf",
    "audio_summary": "Celebrity Endorsement.mp3"
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

# --- Tabs ---
tab_hero, tab_authentic_ai, tab_projects, tab_testimonials, tab_apps = st.tabs(
    ["Hero Section", "The Authentic Intelligence Project", "Key Projects", "Testimonials", "Other Apps"]
)

# --- Hero Section ---
with tab_hero:
    st.title("C. Pete Connor: Digital Portfolio")
    col1, col2 = st.columns([1, 2])

    # Display YouTube Introduction Video with Autoplay
    with col1:
        st.markdown("### Introduction Video")
        youtube_autoplay_url = "https://www.youtube.com/embed/ZlEjftMX1qI?autoplay=1"
        st.video(youtube_autoplay_url)

    # Connect with Virtual Agent Section
    with col2:
        st.markdown("### Connect with My Virtual Agent")
        st.write("Click the phone number below to call and interact with my virtual conversational agent:")
        st.markdown("[+1 325 666 4949](tel:+13256664949)")
        st.write("""
        **Customer Experience Leader | AI Strategist | Operational Excellence**  
        Delivering innovative solutions and measurable results in customer experience and operational transformation.
        """)
        st.markdown("[Email Me](mailto:cpeteconnor@gmail.com) | [LinkedIn](https://linkedin.com/in/cpeteconnor)")

        resume_data = load_file(FILES["resume"])
        if resume_data:
            st.download_button(
                label="Download My Resume Highlights",
                data=resume_data,
                file_name="resume_visualization.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Resume file not found.")

    # MP3 Audio Section
    st.markdown("---")
    st.subheader("Listen to a Summary of My Portfolio")
    st.write("Experience a quick audio overview of my career highlights and achievements:")
    dropbox_audio_link = "https://www.dropbox.com/scl/fi/rimzqokmz986bbqzz24p3/Celebrity-Endorsement.mp3?rlkey=6ccxqt2ovtgw9ajeac7fksfai&raw=1"
    st.audio(dropbox_audio_link, format="audio/mp3")

# --- The Authentic Intelligence Project ---
with tab_authentic_ai:
    st.markdown("## The Authentic Intelligence Project")
    st.write("""
    The Authentic Intelligence Project explores innovative approaches to artificial intelligence in customer experience.  
    By focusing on actionable insights and practical applications, this project highlights the importance of tailoring AI solutions to meet real-world needs.
    """)

    # Video Selector
    st.markdown("### Explore Leadership Personas")
    persona = st.radio(
        "Select a Persona:",
        ["Vendor-Driven Leader", "Empathy-Centric Leader", "Authentic Strategist Leader"]
    )

    if persona == "Vendor-Driven Leader":
        st.subheader("Vendor-Driven Leader")
        st.write("""
        The Vendor-Driven Leader relies heavily on external vendors for quick, pre-packaged solutions.
        While this approach may deliver speed, it often lacks alignment with long-term goals, leading to inefficiencies and poor outcomes.
        """)
        st.video("https://www.dropbox.com/scl/fi/nqh7sg9epzyzs7xcia8na/Vendor-Driven-Leader-1.mp4?raw=1")

    elif persona == "Empathy-Centric Leader":
        st.subheader("Empathy-Centric Leader")
        st.write("""
        The Empathy-Centric Leader emphasizes customer loyalty and relationships.
        However, without AI for scalability, this approach struggles to meet efficiency demands.
        """)
        st.video("https://www.dropbox.com/scl/fi/jve8p4eao8sdrj0ptjb6y/Empathy-Centric-Leader-1.mp4?raw=1")

    elif persona == "Authentic Strategist Leader":
        st.subheader("Authentic Strategist Leader")
        st.write("""
        The Authentic Strategist Leader balances empathy and AI for sustainable success.
        By aligning AI with business goals, this leader drives efficiency, loyalty, and ROI.
        """)
        st.video("https://www.dropbox.com/scl/fi/ngituhxz5o0m3ho16ia6c/Authentic-Strategist-Leader-1.mp4?raw=1")

    # Insights and Metrics
    st.markdown("### Insights and Metrics")
    data = {
        "Persona": ["Vendor-Driven", "Empathy-Centric", "Authentic Strategist"],
        "Success Rate (%)": [40, 65, 90]
    }
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Persona", y="Success Rate (%)", title="Leadership Persona Success Rates")
    st.plotly_chart(fig, use_container_width=True)

# --- Key Projects and Achievements Section ---
with tab_projects:
    st.markdown("## Key Projects and Achievements")

    # Project: LinkedIn Job Seeker Tool
    st.markdown("### **LinkedIn Job Seeker Tool**")
    st.write("""
    The purpose of this tool is to assist LinkedIn job seekers with little to no coding experience.
    It helps:
    - Decompress the overwhelming number of applications by focusing on suitable roles.
    - Avoid ghost jobs and optimize the time spent applying.
    """)

    # Hyperlink for File Download
    st.markdown("[Download LinkedIn Job Seeker Tool Code](Copy%20Paste%20Code.txt)")

    # Embed Video Explanation for the Project
    st.markdown("### Explanation Video: Streamlit Highlight of Code and Prompts")
    video_file = "Streamlit Highlight of Code and Prompts.mp4"  # Ensure this file matches your GitHub repo
    try:
        with open(video_file, "rb") as video:
            video_bytes = video.read()
            st.video(video_bytes)
    except FileNotFoundError:
        st.error(f"Video file '{video_file}' not found.")

    st.markdown("---")
