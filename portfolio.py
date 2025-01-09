import streamlit as st
from PIL import Image, UnidentifiedImageError  # For handling images
from io import BytesIO  # For binary data
import os
import matplotlib.pyplot as plt  # For bar charts
import pandas as pd  # For data processing

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

# --- Tabs ---
tab_hero, tab_certifications, tab_projects, tab_testimonials = st.tabs(
    ["Hero Section", "Certifications", "Key Projects", "Testimonials"]
)

# --- Hero Section ---
with tab_hero:
    st.title("C. Pete Connor: Digital Portfolio")
    col1, col2 = st.columns([1, 2])

    # Display YouTube Introduction Video
    with col1:
        st.markdown("### 🎥 Introduction Video")
        st.video("https://youtube.com/shorts/ZlEjftMX1qI")

    # Connect with Virtual Agent Section
    with col2:
        st.markdown("### 📞 Connect with My Virtual Agent")
        st.write("Click the phone number below to call and interact with my virtual conversational agent:")
        st.markdown("[+1 325 666 4949](tel:+13256664949)")
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

    # MP3 Audio Section
    st.markdown("---")
    st.subheader("🎧 Listen to a Summary of My Portfolio")
    st.write("Experience a quick audio overview of my career highlights and achievements:")
    dropbox_audio_link = "https://www.dropbox.com/scl/fi/rimzqokmz986bbqzz24p3/Celebrity-Endorsement.mp3?rlkey=6ccxqt2ovtgw9ajeac7fksfai&raw=1"
    st.audio(dropbox_audio_link, format="audio/mp3")

# --- Certifications Section ---
with tab_certifications:
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

    # Add Certification Images
    st.markdown("### 📜 Certification Images")
    image_files = ["1.png", "2.png"]  # Specify your image filenames explicitly
    for image_file in image_files:
        try:
            image_path = os.path.join(os.getcwd(), image_file)  # Use current working directory
            image = Image.open(image_path)
            st.image(image, caption=image_file.split('.')[0], use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image {image_file}: {e}")

# --- Key Projects and Achievements Section ---
with tab_projects:
    st.markdown("## 🏆 Key Projects and Achievements")

    # Add Project Images
    st.markdown("### 📸 Project Highlights")
    project_images = [
        {"file": "2025 RCM Assistant.jpg", "caption": "2025 RCM Assistant"},
        {"file": "Denial Prediction and Avoidance.jpg", "caption": "Denial Prediction and Avoidance"}
    ]

    for project in project_images:
        try:
            image_path = os.path.join(os.getcwd(), project["file"])  # Ensure the images are in the same directory
            image = Image.open(image_path)
            st.image(image, caption=project["caption"], use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image '{project['file']}': {e}")

    # Custom GPTs Section
    st.markdown("### 🤖 Custom GPTs")
    st.write("Explore the following custom GPT projects that showcase innovative AI applications:")
    
    # 1. OpenArt AI
    st.markdown("""
    **[OpenArt AI](https://chatgpt.com/g/g-67313d9c22c88190b415c70d5e1c0382-image-prompt-generator)**  
    A stable diffusion prompt generator that uses iterative user questions and answers to optimize outputs.
    """)

    # 2. GPT Builder
    st.markdown("""
    **[GPT Builder](https://chatgpt.com/g/g-673777f64ee08190bdcf4533dea839b6-optimize-your-custom-gpt)**  
    An OpenAI custom GPT creation tool that leverages meta-prompting, iterative user inputs, and advanced frameworks, including JSON and other prompt engineering techniques.
    """)

    # 3. Chat GPT Prompt Engineering Assistant
    st.markdown("""
    **[Chat GPT Prompt Engineering Assistant](https://chatgpt.com/g/g-2pON2NqCm-guided-gpt-prompting)**  
    A simplified, guided user experience leveraging best practices in OpenAI prompt engineering, yielding better results on the first attempt.
    """)


# --- Testimonials Section ---
with tab_testimonials:
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
