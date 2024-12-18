import streamlit as st
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import os
import requests  # For loading remote files
import matplotlib.pyplot as plt
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Digital Portfolio | C. Pete Connor", page_icon="🏆", layout="wide")

# --- File Paths ---
FILES = {
    "profile_pic": "https://raw.githubusercontent.com/UsernameTron/Portfolio/main/profile-pic.png",
    "resume": "https://raw.githubusercontent.com/UsernameTron/Portfolio/main/cv_cpeteconnor.pdf",
    "audio_summary": "https://www.dropbox.com/scl/fi/rimzqokmz986bbqzz24p3/Celebrity-Endorsement.mp3?rlkey=6ccxqt2ovtgw9ajeac7fksfai&raw=1"
}

# --- Helper Functions ---
def load_file(file_path):
    """Load a file from a remote URL or local path."""
    try:
        if file_path.startswith("http"):  # If the file path is a URL
            response = requests.get(file_path)
            if response.status_code == 200:
                return BytesIO(response.content)
            else:
                st.error(f"Failed to load file from {file_path}")
                return None
        else:  # If the file is a local file
            with open(file_path, "rb") as f:
                return BytesIO(f.read())
    except Exception as e:
        st.error(f"Error loading file: {e}")
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
        try:
            profile_pic = Image.open(profile_pic_data)
            st.image(profile_pic, caption="C. Pete Connor")
        except UnidentifiedImageError:
            st.error("Uploaded profile picture is not a valid image file.")
else:
    with col1:
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
            file_name="cv_cpeteconnor.pdf",
            mime="application/pdf",
        )
    else:
        st.warning("Resume file not found.")

# --- MP3 Audio Section ---
st.markdown("---")
st.subheader("🎧 Listen to a Summary of My Portfolio")
st.write("Experience a quick audio overview of my career highlights and achievements:")

# Stream the audio from Dropbox
st.audio(FILES["audio_summary"], format="audio/mp3")

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
