# ============================================================
# AI STUDENT INTELLIGENCE SYSTEM
# Streamlit Application
# ============================================================

import streamlit as st
import os
import sys

from evaluation import get_evaluation
from prediction import predict_student

try:

    from prediction import predict_student
    from evaluation import get_evaluation

    MODEL_AVAILABLE = True

except Exception as e:

    MODEL_AVAILABLE = False
    MODEL_ERROR = str(e)
    
# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SRC_DIR = os.path.join(
    BASE_DIR,
    "src"
)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


# ============================================================
# IMPORT ML PREDICTION
# ============================================================

try:

    from prediction import predict_student

    MODEL_AVAILABLE = True

except Exception as e:

    MODEL_AVAILABLE = False
    MODEL_ERROR = str(e)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Student Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 15px;
    }

    .big-number {
        font-size: 32px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CAREER SKILLS
# ============================================================

career_skills = {

    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Data Visualization"
    ],

    "Data Analyst": [
        "Excel",
        "SQL",
        "Python",
        "Statistics",
        "Power BI",
        "Data Visualization"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "Git",
        "Docker",
        "APIs"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git",
        "APIs"
    ]
}


# ============================================================
# SKILL GAP FUNCTION
# ============================================================

def calculate_skill_gap(current_skills, career):

    required_skills = career_skills.get(
        career,
        []
    )

    current_skills = [
        skill.lower()
        for skill in current_skills
    ]

    missing_skills = [
        skill
        for skill in required_skills
        if skill.lower() not in current_skills
    ]

    matched_skills = [
        skill
        for skill in required_skills
        if skill.lower() in current_skills
    ]

    return matched_skills, missing_skills


# ============================================================
# ROADMAP GENERATOR
# ============================================================

def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        if skill == "Python":

            roadmap.append(
                "Learn Python fundamentals, functions, OOP and Python libraries."
            )

        elif skill == "SQL":

            roadmap.append(
                "Learn SQL queries, JOINs, GROUP BY, subqueries and window functions."
            )

        elif skill == "Statistics":

            roadmap.append(
                "Learn probability, distributions, hypothesis testing and regression."
            )

        elif skill == "Machine Learning":

            roadmap.append(
                "Learn supervised learning, classification, regression and model evaluation."
            )

        elif skill == "Pandas":

            roadmap.append(
                "Practice data cleaning, transformation and analysis using Pandas."
            )

        elif skill == "NumPy":

            roadmap.append(
                "Practice arrays, vectorization and numerical operations using NumPy."
            )

        elif skill == "Data Visualization":

            roadmap.append(
                "Learn Matplotlib, Seaborn and how to communicate data insights."
            )

        elif skill == "Power BI":

            roadmap.append(
                "Learn dashboards, Power Query, data modeling and DAX."
            )

        elif skill == "Git":

            roadmap.append(
                "Learn Git, GitHub, branching and collaborative workflows."
            )

        elif skill == "Docker":

            roadmap.append(
                "Learn Docker images, containers and basic deployment."
            )

        elif skill == "Deep Learning":

            roadmap.append(
                "Learn neural networks, TensorFlow/PyTorch and deep learning projects."
            )

        elif skill == "APIs":

            roadmap.append(
                "Learn REST APIs, requests, JSON and API integration."
            )

        elif skill == "Excel":

            roadmap.append(
                "Learn Excel formulas, Pivot Tables, charts and data analysis."
            )

        elif skill == "HTML":

            roadmap.append(
                "Learn HTML structure, forms, tables and semantic elements."
            )

        elif skill == "CSS":

            roadmap.append(
                "Learn CSS layouts, Flexbox, Grid and responsive design."
            )

        elif skill == "JavaScript":

            roadmap.append(
                "Learn JavaScript fundamentals, DOM manipulation and APIs."
            )

        elif skill == "React":

            roadmap.append(
                "Learn React components, props, state and API integration."
            )

        else:

            roadmap.append(
                f"Start learning {skill} and build a small practical project."
            )

    return roadmap


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# 🎓 AI Student\n# Intelligence"
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "👨‍🎓 Student Analysis",
            "💼 Career Intelligence",
            "🛣️ Skill Roadmap"
        ]
    )

    st.markdown("---")

    st.caption(
        "AI Student Success & Career Intelligence System"
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">🎓 AI Student Intelligence System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        "Student Outcome Prediction + Career Intelligence + Personalized Roadmap"
        "</div>",
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # MODEL STATUS
    # --------------------------------------------------------

    if MODEL_AVAILABLE:

        st.success(
            "🟢 Machine Learning Model Connected"
        )

    else:

        st.error(
            "🔴 Machine Learning Model Could Not Be Loaded"
        )

        st.code(
            MODEL_ERROR
        )

    st.markdown("## 🚀 What This System Does")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">

            <h3>👨‍🎓 Student Prediction</h3>

            <p>
            Predict whether a student's academic
            outcome is likely to be Dropout,
            Enrolled or Graduate.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">

            <h3>💼 Career Intelligence</h3>

            <p>
            Compare current skills with the
            skills required for a target career.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="card">

            <h3>🛣️ Skill Roadmap</h3>

            <p>
            Generate a personalized learning
            roadmap based on missing skills.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown("## 📊 Project Pipeline")

    pipeline_col1, pipeline_col2, pipeline_col3, pipeline_col4 = st.columns(4)

    with pipeline_col1:

        st.metric(
            "Dataset",
            "4,424 Students"
        )

    with pipeline_col2:

        st.metric(
            "ML Model",
            "Random Forest"
        )

    with pipeline_col3:

        st.metric(
            "Prediction",
            "3 Classes"
        )

    with pipeline_col4:

        st.metric(
            "Career Paths",
            len(career_skills)
        )

    st.markdown("---")

    st.info(
        "💡 Start with **Student Analysis** to make an ML prediction."
    )


# ============================================================
# STUDENT ANALYSIS
# ============================================================

elif page == "👨‍🎓 Student Analysis":

    st.title("👨‍🎓 Student Analysis")

    st.write(
        "Enter student information and use the trained "
        "Machine Learning model to predict the academic outcome."
    )

    if not MODEL_AVAILABLE:

        st.error(
            "The ML model is not available."
        )

        st.code(
            MODEL_ERROR
        )

    # ========================================================
    # DEMOGRAPHICS
    # ========================================================

    st.markdown("### 👤 Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        marital_status = st.number_input(
            "Marital Status",
            min_value=1,
            value=1,
            step=1
        )

        gender = st.number_input(
            "Gender",
            min_value=0,
            value=1,
            step=1
        )

        age = st.number_input(
            "Age at Enrollment",
            min_value=15,
            max_value=80,
            value=20,
            step=1
        )

        nationality = st.number_input(
            "Nacionality",
            min_value=1,
            value=1,
            step=1
        )

    with col2:

        displaced = st.number_input(
            "Displaced",
            min_value=0,
            max_value=1,
            value=0,
            step=1
        )

        international = st.number_input(
            "International",
            min_value=0,
            max_value=1,
            value=0,
            step=1
        )

        debtor = st.number_input(
            "Debtor",
            min_value=0,
            max_value=1,
            value=0,
            step=1
        )

    with col3:

        tuition = st.number_input(
            "Tuition Fees Up To Date",
            min_value=0,
            max_value=1,
            value=1,
            step=1
        )

        scholarship = st.number_input(
            "Scholarship Holder",
            min_value=0,
            max_value=1,
            value=0,
            step=1
        )

        special_needs = st.number_input(
            "Educational Special Needs",
            min_value=0,
            max_value=1,
            value=0,
            step=1
        )

    # ========================================================
    # ADMISSION INFORMATION
    # ========================================================

    st.markdown("### 🎓 Admission Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        application_mode = st.number_input(
            "Application Mode",
            min_value=1,
            value=1,
            step=1
        )

        application_order = st.number_input(
            "Application Order",
            min_value=0,
            value=1,
            step=1
        )

        course = st.number_input(
            "Course",
            min_value=1,
            value=1,
            step=1
        )

    with col2:

        attendance = st.number_input(
            "Daytime/Evening Attendance",
            min_value=0,
            max_value=1,
            value=1,
            step=1
        )

        previous_qualification = st.number_input(
            "Previous Qualification",
            min_value=1,
            value=1,
            step=1
        )

        previous_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0
        )

    with col3:

        admission_grade = st.number_input(
            "Admission Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0
        )

    # ========================================================
    # FAMILY / EDUCATION
    # ========================================================

    st.markdown("### 👨‍👩‍👧 Family & Education")

    col1, col2 = st.columns(2)

    with col1:

        mother_qualification = st.number_input(
            "Mother's Qualification",
            min_value=1,
            value=1,
            step=1
        )

        father_qualification = st.number_input(
            "Father's Qualification",
            min_value=1,
            value=1,
            step=1
        )

    with col2:

        mother_occupation = st.number_input(
            "Mother's Occupation",
            min_value=0,
            value=0,
            step=1
        )

        father_occupation = st.number_input(
            "Father's Occupation",
            min_value=0,
            value=0,
            step=1
        )

    # ========================================================
    # SEMESTER 1
    # ========================================================

    st.markdown("### 📘 1st Semester")

    col1, col2, col3 = st.columns(3)

    with col1:

        sem1_credited = st.number_input(
            "Credited Units",
            min_value=0,
            max_value=30,
            value=0,
            key="sem1_credited"
        )

        sem1_enrolled = st.number_input(
            "Enrolled Units",
            min_value=0,
            max_value=30,
            value=6,
            key="sem1_enrolled"
        )

    with col2:

        sem1_evaluations = st.number_input(
            "Evaluations",
            min_value=0,
            max_value=30,
            value=6,
            key="sem1_evaluations"
        )

        sem1_approved = st.number_input(
            "Approved Units",
            min_value=0,
            max_value=30,
            value=5,
            key="sem1_approved"
        )

    with col3:

        sem1_grade = st.number_input(
            "Average Grade",
            min_value=0.0,
            max_value=20.0,
            value=12.0,
            key="sem1_grade"
        )

        sem1_without_eval = st.number_input(
            "Without Evaluations",
            min_value=0,
            max_value=30,
            value=0,
            key="sem1_without_eval"
        )

    # ========================================================
    # SEMESTER 2
    # ========================================================

    st.markdown("### 📗 2nd Semester")

    col1, col2, col3 = st.columns(3)

    with col1:

        sem2_credited = st.number_input(
            "Credited Units",
            min_value=0,
            max_value=30,
            value=0,
            key="sem2_credited"
        )

        sem2_enrolled = st.number_input(
            "Enrolled Units",
            min_value=0,
            max_value=30,
            value=6,
            key="sem2_enrolled"
        )

    with col2:

        sem2_evaluations = st.number_input(
            "Evaluations",
            min_value=0,
            max_value=30,
            value=6,
            key="sem2_evaluations"
        )

        sem2_approved = st.number_input(
            "Approved Units",
            min_value=0,
            max_value=30,
            value=5,
            key="sem2_approved"
        )

    with col3:

        sem2_grade = st.number_input(
            "Average Grade",
            min_value=0.0,
            max_value=20.0,
            value=12.0,
            key="sem2_grade"
        )

        sem2_without_eval = st.number_input(
            "Without Evaluations",
            min_value=0,
            max_value=30,
            value=0,
            key="sem2_without_eval"
        )

    # ========================================================
    # ECONOMIC INFORMATION
    # ========================================================

    st.markdown("### 🌍 Economic Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        unemployment = st.number_input(
            "Unemployment Rate",
            value=10.0
        )

    with col2:

        inflation = st.number_input(
            "Inflation Rate",
            value=1.5
        )

    with col3:

        gdp = st.number_input(
            "GDP",
            value=1.0
        )

    # ========================================================
    # PERFORMANCE CALCULATION
    # ========================================================

    if sem1_enrolled > 0:

        sem1_rate = (
            sem1_approved /
            sem1_enrolled
        )

    else:

        sem1_rate = 0

    if sem2_enrolled > 0:

        sem2_rate = (
            sem2_approved /
            sem2_enrolled
        )

    else:

        sem2_rate = 0

    average_rate = (
        sem1_rate +
        sem2_rate
    ) / 2

    st.markdown("### 📈 Calculated Performance")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Semester 1 Approval",
            f"{sem1_rate * 100:.1f}%"
        )

    with c2:

        st.metric(
            "Semester 2 Approval",
            f"{sem2_rate * 100:.1f}%"
        )

    with c3:

        st.metric(
            "Average Approval",
            f"{average_rate * 100:.1f}%"
        )

    # ========================================================
    # ML PREDICTION
    # ========================================================

    st.markdown("---")

    if st.button(
        "🚀 Predict Student Outcome",
        use_container_width=True
    ):

        if not MODEL_AVAILABLE:

            st.error(
                "Prediction cannot start because the model could not be loaded."
            )

        else:

            student_data = {

                "Marital Status": marital_status,

                "Application mode": application_mode,

                "Application order": application_order,

                "Course": course,

                "Daytime/evening attendance": attendance,

                "Previous qualification": previous_qualification,

                "Previous qualification (grade)": previous_grade,

                "Nacionality": nationality,

                "Mother's qualification": mother_qualification,

                "Father's qualification": father_qualification,

                "Mother's occupation": mother_occupation,

                "Father's occupation": father_occupation,

                "Admission grade": admission_grade,

                "Displaced": displaced,

                "Educational special needs": special_needs,

                "Debtor": debtor,

                "Tuition fees up to date": tuition,

                "Gender": gender,

                "Scholarship holder": scholarship,

                "Age at enrollment": age,

                "International": international,

                "Curricular units 1st sem (credited)": (
                    sem1_credited
                ),

                "Curricular units 1st sem (enrolled)": (
                    sem1_enrolled
                ),

                "Curricular units 1st sem (evaluations)": (
                    sem1_evaluations
                ),

                "Curricular units 1st sem (approved)": (
                    sem1_approved
                ),

                "Curricular units 1st sem (grade)": (
                    sem1_grade
                ),

                "Curricular units 1st sem (without evaluations)": (
                    sem1_without_eval
                ),

                "Curricular units 2nd sem (credited)": (
                    sem2_credited
                ),

                "Curricular units 2nd sem (enrolled)": (
                    sem2_enrolled
                ),

                "Curricular units 2nd sem (evaluations)": (
                    sem2_evaluations
                ),

                "Curricular units 2nd sem (approved)": (
                    sem2_approved
                ),

                "Curricular units 2nd sem (grade)": (
                    sem2_grade
                ),

                "Curricular units 2nd sem (without evaluations)": (
                    sem2_without_eval
                ),

                "Unemployment rate": unemployment,

                "Inflation rate": inflation,

                "GDP": gdp
            }

            try:

                prediction, probabilities = predict_student(
                    student_data
                )

                # ------------------------------------------------
                # RESULT
                # ------------------------------------------------

                st.success(
                    "✅ Prediction completed successfully!"
                )

                st.markdown(
                    "## 🎯 Predicted Student Outcome"
                )

                if str(prediction).lower() == "graduate":

                    st.success(
                        f"🎓 **{prediction}**"
                    )

                elif str(prediction).lower() == "dropout":

                    st.error(
                        f"⚠️ **{prediction}**"
                    )

                else:

                    st.info(
                        f"📚 **{prediction}**"
                    )

                # ------------------------------------------------
                # PROBABILITIES
                # ------------------------------------------------

                st.markdown(
                    "### 📊 Prediction Probabilities"
                )

                probability_columns = st.columns(
                    len(probabilities)
                )

                for i, (class_name, probability) in enumerate(
                    probabilities.items()
                ):

                    with probability_columns[i]:

                        st.metric(
                            str(class_name),
                            f"{probability * 100:.2f}%"
                        )

                        st.progress(
                            probability
                        )

            except Exception as e:

                st.error(
                    "❌ Prediction failed."
                )

                st.exception(e)


# ============================================================
# CAREER INTELLIGENCE
# ============================================================

elif page == "💼 Career Intelligence":

    st.title("💼 Career Intelligence")

    st.write(
        "Select your target career and enter the skills "
        "you already know."
    )

    career = st.selectbox(
        "🎯 Target Career",
        list(career_skills.keys())
    )

    skills_text = st.text_area(
        "🧠 Your Current Skills",
        placeholder="Example: Python, Pandas, SQL"
    )

    if st.button(
        "🔍 Analyze Career Fit",
        use_container_width=True
    ):

        if skills_text.strip() == "":

            st.warning(
                "Please enter at least one skill."
            )

        else:

            current_skills = [

                skill.strip()

                for skill in skills_text.split(",")

                if skill.strip()

            ]

            matched, missing = calculate_skill_gap(
                current_skills,
                career
            )

            required = career_skills[career]

            match_percentage = (

                len(matched) /
                len(required)

            ) * 100

            st.markdown(
                "## 📊 Career Skill Analysis"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Career",
                    career
                )

            with col2:

                st.metric(
                    "Skill Match",
                    f"{match_percentage:.1f}%"
                )

            with col3:

                st.metric(
                    "Missing Skills",
                    len(missing)
                )

            st.markdown(
                "### ✅ Matched Skills"
            )

            if matched:

                for skill in matched:

                    st.success(
                        f"✓ {skill}"
                    )

            else:

                st.info(
                    "No matching skills found yet."
                )

            st.markdown(
                "### 📚 Missing Skills"
            )

            if missing:

                for skill in missing:

                    st.warning(
                        f"• {skill}"
                    )

            else:

                st.success(
                    "🎉 All listed career skills are matched!"
                )

            # Save for roadmap

            st.session_state[
                "missing_skills"
            ] = missing

            st.session_state[
                "career"
            ] = career


# ============================================================
# SKILL ROADMAP
# ============================================================

elif page == "🛣️ Skill Roadmap":

    st.title(
        "🛣️ Personalized Skill Roadmap"
    )

    missing_skills = st.session_state.get(
        "missing_skills",
        []
    )

    career = st.session_state.get(
        "career",
        None
    )

    if not career:

        st.info(
            "First go to Career Intelligence "
            "and analyze a career."
        )

    else:

        st.success(
            f"Roadmap generated for: **{career}**"
        )

        roadmap = generate_roadmap(
            missing_skills
        )

        if roadmap:

            for i, step in enumerate(
                roadmap,
                start=1
            ):

                st.markdown(
                    f"""
                    <div class="card">

                    <h3>Step {i}</h3>

                    <p>{step}</p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "🎉 No missing skills! "
                "Your current skills cover "
                "the listed requirements."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🎓 AI Student Success & Career Intelligence System | "
    "Built with Python, Scikit-learn and Streamlit"
)