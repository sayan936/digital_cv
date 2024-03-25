from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Sayan_Chakraborty_resume3.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Sayan Chakraborty"
PAGE_ICON = ":wave:"
NAME = "Sayan Chakraborty"
DESCRIPTION = """
Data science graduate specializing in quantitative analysis and AI, with advanced skills in Python and R for data analysis and visualization, and a commitment to impactful, data-driven projects and continuous skill improvement.
"""
EMAIL = "sayanchakraborty289@gmail.com"
PHONE_NUMBER = "+91 8334869162"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sayanchakraborty97/",
    "GitHub": "https://github.com/sayan936",
}
PROJECTS = {
    "🏆 Detecting Aggression in Social Media Post - Using Transfer learning and Deep Learning methods ": "https://github.com/sayan936/Social-Media-Aggression-Detection",
    "🏆 Empathy Score Detection - Predicting empathy score from eye T4 dataset": "https://github.com/sayan936/Empathy/tree/main",
    "🏆 Cricket Player Statistics Chatbot Development": "https://github.com/sayan936/cricbot",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞" ,PHONE_NUMBER)
    
    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
    - 🎓 Master of Science in Data Science from the University of Essex
    - 🎓 Bachelor of Technology in Computer Science from Asansol Engineering College
    - ✔️ Strong hands-on experience and knowledge in Python, Excel and SQL
    - 💡 Proficient in data analysis, data visualization, and statistical modeling
    - 🛠️ Experienced in using data science tools and libraries (e.g., Pandas, NumPy, Matplotlib, Scikit-Learn)
    - 📊 Capable of translating business problems into data-driven solutions
    - 🔄 Skilled in machine learning algorithms and predictive modeling
    - ✨ Demonstrated ability to communicate complex data insights in a clear and effective manner
    - 🤖 Knowledgeable in artificial intelligence and machine learning applications
    - 🌐 Familiar with SQL, NoSQL databases, and data warehousing solutions
    - 🌍 Team player with experience in cross-functional collaboration
    """
)


# --- SKILLS ---
st.write('\n')
st.subheader("Core Competencies")
st.write(
    """
    - 💻 Programming: Proficient in Python, R, Java, HTML, CSS.
    - 📈 Data Science: Skilled in ML, DL, NLP, with hands-on TensorFlow, SciKit Learn.
    - 🌍 Web Development: Experienced with Flask, Django.
    - 📊 Visualization & Databases: Proficient in Tableau, PowerBi, MySQL, Oracle SQL.
    - 🌐 Big Data & Cloud: Knowledgeable in Hadoop, Azure Data Factory, Azure Databricks.
    - 🛠️ Tools & Technologies: Familiar with VS Code, Jupyter, PyCharm, RStudio.
    """
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist Associate | BlackCoffer**")
st.write("10/2023 - 02/2024")
st.write(
    """
- Developed custom Python web scraping scripts tailored to client-specific data extraction needs, enhancing data collection processes.
- Created and maintained Python scripts for organizing data, significantly improving efficiency in client promotional activities.
- Utilized advanced SQL queries for efficient data retrieval, contributing to more informed data-driven decision-making processes.
- Managed client interactions, ensuring clear communication and providing tailored data solutions to meet specific business needs.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Assistant System Engineer | Tata Consultancy Services**")
st.write("04/2021 - 09/2022")
st.write(
    """
- Developed and maintained JCL scripts, optimizing the execution of batch jobs and ensuring smooth data processing operations.
- Demonstrated quick problem-solving by promptly addressing software bugs, maintaining a high bug resolution rate.
- Collaborated effectively with cross-functional teams to implement new features, significantly enhancing application functionality.
- Monitored and managed client software systems, identifying and resolving performance issues to maintain optimal system stability.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Project Engineer | Wipro Technologies**")
st.write("09/2020 - 03/2021")
st.write(
    """
- Utilized Hadoop, Spark, and Hive technologies to manage and analyze large datasets, leading to more efficient data processing.
- Conducted comprehensive data cleaning operations, resulting in a notable improvement in data quality and analysis reliability.
- Developed and executed SQL queries for data extraction, facilitating better support for data-driven decision-making.
- Created detailed reports summarizing key findings and insights, aiding stakeholders in informed decision-making.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


