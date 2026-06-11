import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "John Carter"
DESCRIPTION = """
Detail-oriented and analytical Data Analyst with experience in collecting, cleaning, and interpreting data.
"""

EMAIL = "john.carter@email.com"
LINKEDIN_URL = "https://www.linkedin.com/in/johncarter"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

resume_file = current_dir / "assets" / "egezon_cv_12_2024.pdf"
profile_pic_file = current_dir / "assets" / "JohnCarter.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ 5+ years of experience working with data analysis, business intelligence, and data science projects across the banking, retail, and healthcare industries.
- ✔️ Strong proficiency in Python, SQL, Excel, Power BI, and Tableau for data analysis, visualization, and reporting.
- ✔️ Skilled in data cleaning, transformation, and preprocessing of large datasets.
- ✔️ Strong understanding of statistical analysis, data modeling, and forecasting techniques.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Python (FastAPI, Scikit-learn, Pandas), SQL, DBT
- 📊 Data Visualization: PowerBI, Streamlit
- 🗄️ Databases: Snowflake, AWS, PostgreSQL
- 🤖 Machine Learning: Neural networks, classification algorithms
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Data Scientist | National Trust Bank**")
    st.write("11/2023 - 11/2024")
    st.write(
        """
- ► Developed machine learning models to predict customer churn and loan default risk.
- ► Analyzed large financial datasets using Python and SQL.
- ► Built fraud detection systems that helped identify suspicious transactions.
"""
    )

    # --- JOB 2
    st.write("\n")
    st.write("🚧", "**Data Analyst | MedCare Healthcare Group**")
    st.write("10/2021 - 08/2023")
    st.write(
        """
- ► Collected, cleaned, and analyzed healthcare data using Excel, SQL, and Python.
- ► Produced reports on patient outcomes and operational performance.
- ► Identified trends that helped improve resource allocation and service quality.
"""
    )

    # --- JOB 3
    st.write("\n")
    st.write("🚧", "**Business Intelligence Analyst | RetailMax Solutions**")
    st.write("05/2023 - present")
    st.write(
        """
- ► Designed interactive Power BI dashboards for sales and inventory tracking.
- ► Analyzed customer purchasing behavior to identify growth opportunities.
- ► Automated reporting processes, reducing manual work and improving efficiency.
"""
    )


elif page == "About":
    st.title("About Me")
    st.write("""
    I am a motivated and detail-oriented Data Analyst with a strong passion
    for transforming data into meaningful insights. I enjoy working with data
    to identify trends, solve problems, and support informed decision-making.
    Skilled in data analysis, data visualization, and reporting, I am proficient
    in tools such as Excel, SQL, Python, and Power BI. I am a quick learner, an
    effective communicator, and a collaborative team player who is always eager to
    develop new skills and contribute to organizational success. 
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
