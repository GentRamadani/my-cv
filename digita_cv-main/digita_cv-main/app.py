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
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects", "Lessons"])

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


elif page == "Projects":
    st.title("Projects")

    st.subheader("📊 Customer Churn Prediction")
    st.write("""
    Developed a machine learning model using Python and Scikit-learn to predict
    customer churn for a telecommunications company. The project included data
    cleaning, feature engineering, model training, and performance evaluation.
    """)
    st.write("**Technologies:** Python, Pandas, Scikit-learn, Streamlit")

    st.write("---")

    st.subheader("🏦 Banking Fraud Detection System")
    st.write("""
    Built a fraud detection solution for banking transactions using historical
    transaction data. The model identified suspicious activities and generated
    alerts for potential fraud cases.
    """)
    st.write("**Technologies:** Python, SQL, Machine Learning")

    st.write("---")

    st.subheader("📈 Sales Performance Dashboard")
    st.write("""
    Designed an interactive dashboard to track sales performance, customer trends,
    and product profitability. The dashboard helped management make data-driven
    business decisions.
    """)
    st.write("**Technologies:** Power BI, SQL, Excel")

    st.write("---")

    st.subheader("🏥 Healthcare Analytics Project")
    st.write("""
    Analyzed healthcare data to identify trends in patient outcomes and hospital
    resource utilization. Created reports and visualizations to support operational
    improvements.
    """)
    st.write("**Technologies:** Python, Tableau, SQL")


# ✅ FIXED PART (LESSONS - corrected indentation)
elif page == "Lessons":

    st.title("Lessons")
    st.write("""
    Here you will find different lectures and summaries of topics
    covered throughout the course.
    """)

    lesson_page = st.selectbox(
        "Jump to a Lecture",
        ["Select a Lecture", "Lecture_12"]
    )

    if lesson_page == "Lecture_12":
        st.title("Lecture 12")

        st.subheader("Introduction to SQL")
        st.write("""
        SQL (Structured Query Language) is the standard language used to communicate
        with databases. It allows you to store, retrieve, update, and delete data
        from a database.
        """)

        st.subheader("Relationships in SQL")
        st.write("""
        In SQL, relationships define how tables are connected to each other.

        • One-to-One (1:1): One record in Table A is linked to one record in Table B.

        • One-to-Many: One record in Table A is linked to many records in Table B.

        • Many-to-Many: Many records in Table A can be linked to many records in Table B.
        """)

        st.subheader("Difference between Star Schema and Snowflake Schema")
        st.write("""
        The Star Schema and Snowflake Schema are two approaches to data warehouse design.

        In the Star Schema, a central fact table is connected to dimension tables,
        forming a star-like structure. This design is simpler and faster for querying.

        On the other hand, the Snowflake Schema normalizes dimension tables into
        multiple related tables, resembling a snowflake. While it reduces data
        redundancy, it can make queries more complex.

        The Star Schema prioritizes query speed and simplicity, while the Snowflake
        Schema focuses on data normalization and storage efficiency.
        """)

        st.subheader("What is Database Normalization?")
        st.write("""
        Database normalization is a database design process that organizes data into
        specific table structures.

        It helps to improve data integrity, prevent data anomalies, minimize data
        redundancy, and bolster query performance.
        """)


    
        
    



    

    

