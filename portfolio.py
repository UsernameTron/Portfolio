# --- Key Projects and Achievements Section ---
with tab_projects:
    st.markdown("## 🏆 Key Projects and Achievements")

    # Project: LinkedIn Job Seeker Tool
    st.markdown("### 🔍 LinkedIn Job Seeker Tool")
    st.write("""
    The purpose of this tool is to assist LinkedIn job seekers with little to no coding experience.
    It helps:
    - Decompress the overwhelming number of applications by focusing on suitable roles.
    - Avoid ghost jobs and optimize the time spent applying.
    
    This project highlights my proactive approach to problem-solving: while others may complain about inefficiencies, I take strategic action to address and solve them.
    """)

    # Embed Video Explanation for the Project
    st.markdown("### 🎥 Explanation Video: Streamlit Highlight of Code and Prompts")
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
                label="📄 Download Code: LinkedIn Job Seeker Tool",
                data=file,
                file_name="LinkedIn_Job_Seeker_Tool.txt",
                mime="text/plain",
            )
    except FileNotFoundError:
        st.error(f"Code file '{code_file}' not found.")

    st.markdown("---")
