import streamlit as st
from PIL import Image, UnidentifiedImageError  # For handling images
from io import BytesIO  # For binary data
import os
import matplotlib.pyplot as plt  # For bar charts
import pandas as pd  # For data processing

# --- Page Configuration ---
st.set_page_config(page_title="Digital Portfolio | C. Pete Connor", page_icon=None, layout="wide")

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
tab_hero, tab_certifications, tab_projects, tab_testimonials, tab_apps = st.tabs(
    ["Hero Section", "Certifications", "Key Projects", "Testimonials", "Other Apps"]
)

# --- Hero Section ---
with tab_hero:
    st.title("C. Pete Connor: Digital Portfolio")
    col1, col2 = st.columns([1, 2])

    # Display YouTube Introduction Video with Autoplay
    with col1:
        st.markdown("### \ud83c\udfa5 Introduction Video")
        youtube_autoplay_url = "https://www.youtube.com/embed/ZlEjftMX1qI?autoplay=1"
        st.video(youtube_autoplay_url)

    # Connect with Virtual Agent Section
    with col2:
        st.markdown("### \ud83d\udcde Connect with My Virtual Agent")
        st.write("Click the phone number below to call and interact with my virtual conversational agent:")
        st.markdown("[+1 325 666 4949](tel:+13256664949)")
        st.write("""
        **Customer Experience Leader | AI Strategist | Operational Excellence**  
        Delivering innovative solutions and measurable results in customer experience and operational transformation.
        """)
        st.markdown("[\ud83d\udce7 Email Me](mailto:cpeteconnor@gmail.com) | [\ud83d\udd17 LinkedIn](https://linkedin.com/in/cpeteconnor)")

        resume_data = load_file(FILES["resume"])
        if resume_data:
            st.download_button(
                label="\ud83d\udcc4 Download My Resume Highlights",
                data=resume_data,
                file_name="resume_visualization.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Resume file not found.")

    # MP3 Audio Section
    st.markdown("---")
    st.subheader("\ud83c\udfa7 Listen to a Summary of My Portfolio")
    st.write("Experience a quick audio overview of my career highlights and achievements:")
    dropbox_audio_link = "https://www.dropbox.com/scl/fi/rimzqokmz986bbqzz24p3/Celebrity-Endorsement.mp3?rlkey=6ccxqt2ovtgw9ajeac7fksfai&raw=1"
    st.audio(dropbox_audio_link, format="audio/mp3")

# --- Certifications Section ---
with tab_certifications:
    st.markdown("## \ud83c\udf93 Certifications")
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
    st.markdown("### \ud83d\udd8c\ufe0f Certification Images")
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
    st.markdown("## \ud83c\udfc6 Key Projects and Achievements")

    # Project: LinkedIn Job Seeker Tool
    st.markdown("### \ud83d\udd0d LinkedIn Job Seeker Tool")
    st.write("""
    The purpose of this tool is to assist LinkedIn job seekers with little to no coding experience.
    It helps:
    - Decompress the overwhelming number of applications by focusing on suitable roles.
    - Avoid ghost jobs and optimize the time spent applying.
    
    This project highlights my proactive approach to problem-solving: while others may complain about inefficiencies, I take strategic action to address and solve them.
    """)

    # Embed Video Explanation for the Project
    st.markdown("### \ud83c\udfa5 Explanation Video: Streamlit Highlight of Code and Prompts")
    video_file = "Streamlit Highlight of Code and Prompts.mp4"  # Ensure this file matches your GitHub repo
    try:
        with open(video_file, "rb") as video:
            video_bytes = video.read()
            st.video(video_bytes)
    except FileNotFoundError:
        st.error(f"Video file '{video_file}' not found.")

    # Add Download Button for the Code
    code_file = "Copy Paste Code.txt"  # Ensure this matches the file path in your GitHub repo
    try:
        with open(code_file, "rb") as file:
            st.download_button(
                label="\ud83d\udcc4 Download Code: LinkedIn Job Seeker Tool",
                data=file,
                file_name="LinkedIn_Job_Seeker_Tool.txt",
                mime="text/plain",
            )
    except FileNotFoundError:
        st.error(f"Code file '{code_file}' not found.")

    st.markdown("---")

# --- Other Apps Section ---
with tab_apps:
    st.markdown("## \ud83c\udf10 Other Streamlit Apps")
    st.write("Explore other Streamlit apps I have developed. These tools demonstrate my problem-solving approach and focus on practical, strategic solutions.")

    # App 1: Customer Churn Assessment Tool
    st.markdown("### \ud83d\udcc8 Customer Churn Assessment Tool")
    st.write("""
    This tool helps organizations analyze customer churn and loyalty logic. By using this app, businesses can identify key drivers 
    of customer retention and take actionable steps to improve loyalty.
    """)
    st.markdown("[Open App](https://customer-churn-loyalty-logic-8tvwyfjvs6cjrmjcs2mndt.streamlit.app/)")

    st.markdown("---")

    # App 2: Technology Readiness Assessment
    st.markdown("### \ud83d\udcca Technology Readiness Assessment Tool")
    st.write("""
    This app provides organizations with a customizable assessment framework to evaluate technology readiness, 
    avoiding the need for expensive third-party assessments. The methodology is backed by fundamentals from premium 
    personality assessments, tailored to meet strategic needs.
    """)
    st.markdown("[Open App](https://jewfi5agnuff4ecurpuqcy.streamlit.app/)")

# --- Testimonials Section ---
with tab_testimonials:
    st.markdown("## \ud83d\udcac Professional Recommendations")
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
*Your future transformation starts here!* \ud83d\ude80
""")
