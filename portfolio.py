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
    "resume": "cv_cpeteconnor.pdf"
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
tab_hero, tab_projects, tab_testimonials, tab_apps = st.tabs(
    ["Hero Section", "Key Projects", "Testimonials", "Other Apps"]
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

# --- Key Projects Section ---
with tab_projects:
    st.markdown("## Key Projects")

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

    # Link to Video Explanation for the Project
    st.markdown("[Watch Explanation Video: Streamlit Highlight of Code and Prompts](https://www.youtube.com/embed/ZlEjftMX1qI)")

    st.markdown("---")

    # Integrated Predictive Analytics for Healthcare ROI
    st.markdown("### **Integrated Predictive Analytics for Healthcare ROI**")
    st.write("""
    The healthcare industry often faces challenges in managing claim denials, ensuring compliance, and optimizing operational efficiency. This project introduces a comprehensive **predictive analytics and machine learning solution** tailored to healthcare organizations, focusing on:
    - **Sentiment Analysis**: Gaining insights from patient and staff interactions to identify areas for improvement.
    - **Predictive Analytics**: Forecasting claim denials based on historical trends, payer rules, and specific claim attributes.
    - **Machine Learning Models**: Delivering actionable insights to mitigate risks and improve decision-making.

    **Project Highlights:**
    1. **Sentiment Analysis**:
       - Understand patient feedback to enhance service delivery and identify dissatisfaction trends.
       - Improve communication strategies and patient satisfaction scores.
    2. **Predictive Denial Management**:
       - Identify high-risk claims before submission using historical denial patterns and advanced classification models.
       - Proactively resolve issues such as missing documentation, non-compliant CPT codes, and preauthorization gaps.
    3. **Revenue Optimization through Automation**:
       - Automate tedious tasks like payer-specific denial analysis and eligibility checks.
       - Free up staff for patient-centric activities while accelerating reimbursement cycles.

    **Outcomes and Benefits:**
    - **Financial Impact**: Reduce denial rates by up to 20%, resulting in immediate ROI and faster reimbursements.
    - **Operational Efficiency**: Free up administrative resources by automating 50% of manual tasks.
    - **Compliance**: Ensure adherence to the latest payer rules and minimize audit risks.

    **Access the Case Studies:**
    - [Case Study: ML in Healthcare ROI in Days, Not Weeks](https://drive.google.com/file/d/18EE635Yf-qCsfzbK1gDnX7pe5YE4hnmw/view?usp=drive_link)
    - [RCM Automation and Prediction Model](https://drive.google.com/file/d/1MJ08YGgEP4I4LJm-xEf_Fw1U8Y_QLjMg/view?usp=drive_link)

    **Conclusion:**  
    This project demonstrates the transformative potential of predictive analytics and machine learning in healthcare, delivering measurable ROI in days, not weeks. By addressing inefficiencies and enabling data-driven decision-making, healthcare organizations can improve patient outcomes while optimizing financial performance.
    """)

    st.markdown("---")

# --- Other Apps Section ---
with tab_apps:
    st.markdown("## Other Streamlit Apps")
    st.write("Explore other Streamlit apps I have developed. These tools demonstrate my problem-solving approach and focus on practical, strategic solutions.")

    # App 1: Customer Churn Assessment Tool
    st.markdown("### Customer Churn Assessment Tool")
    st.write("""
    This tool helps organizations analyze customer churn and loyalty logic. By using this app, businesses can identify key drivers 
    of customer retention and take actionable steps to improve loyalty.
    """)
    st.markdown("[Open App](https://customer-churn-loyalty-logic-8tvwyfjvs6cjrmjcs2mndt.streamlit.app/)")

    st.markdown("---")

    # App 2: Technology Readiness Assessment
    st.markdown("### Technology Readiness Assessment Tool")
    st.write("""
    This app provides organizations with a customizable assessment framework to evaluate technology readiness, 
    avoiding the need for expensive third-party assessments. The methodology is backed by fundamentals from premium 
    personality assessments, tailored to meet strategic needs.
    """)
    st.markdown("[Open App](https://jewfi5agnuff4ecurpuqcy.streamlit.app/)")

# --- Testimonials Section ---
with tab_testimonials:
    st.markdown("## Professional Recommendations")
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
