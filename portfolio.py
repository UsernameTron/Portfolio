import streamlit as st
from PIL import Image, UnidentifiedImageError
from io import BytesIO
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
    "audio_summary": "Celebrity-Endorsement.mp3"  # Root directory
}

# --- Helper Functions ---
def load_file(file_path):
    """
    Load a file from the same directory or raise an error if not found.
    """
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return None
    with open(file_path, "rb") as f:
        return BytesIO(f.read())  # Return as BytesIO for compatibility

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

# --- Tabs ---
tab1, tab2 = st.tabs(["Portfolio", "Graphic Arts"])

# --- Tab 1: Portfolio ---
with tab1:
    st.title("C. Pete Connor: Digital Portfolio")
    col1, col2 = st.columns([1, 2])

    # Display Profile Picture
    profile_pic_data = load_file(FILES["profile_pic"])
    if profile_pic_data:
        try:
            profile_pic = Image.open(profile_pic_data)
            with col1:
                st.image(profile_pic, caption="C. Pete Connor")
        except UnidentifiedImageError:
            st.error("Uploaded profile picture is not a valid image file.")
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
                data=resume_data.getvalue(),
                file_name="cv_cpeteconnor.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Resume file not found.")

    # MP3 Audio Section
    st.markdown("---")
    st.subheader("🎧 Listen to a Summary of My Portfolio")
    st.write("Experience a quick audio overview of my career highlights and achievements:")

    # Use the Dropbox streaming link
    dropbox_audio_link = "https://www.dropbox.com/scl/fi/rimzqokmz986bbqzz24p3/Celebrity-Endorsement.mp3?rlkey=6ccxqt2ovtgw9ajeac7fksfai&raw=1"
    st.audio(dropbox_audio_link, format="audio/mp3")

# --- Footer ---
st.markdown("---")
st.markdown("""
**Let’s connect and discuss how I can drive success for your organization.**  
*Your future transformation starts here!* 🚀
""")
