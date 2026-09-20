# ============================================================
# AI STUDENT INTELLIGENCE SYSTEM
# Streamlit Application
# ============================================================
import streamlit as st
import os
import sys

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
# PROJECT IMPORTS
# ============================================================

from prediction import predict_student
from evaluation import get_evaluation
# ============================================================
# IMPORT ML PREDICTION
# ============================================================

try:

    from prediction import predict_student
    from evaluation import get_evaluation

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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root { --bg:#07111f; --panel:#0d1b2d; --panel2:#10243b; --line:rgba(148,163,184,.16); --text:#f8fafc; --muted:#94a3b8; --accent:#67e8f9; --accent2:#818cf8; }
    .stApp { background: radial-gradient(circle at 75% 0%, rgba(99,102,241,.16), transparent 30%), radial-gradient(circle at 15% 20%, rgba(34,211,238,.08), transparent 25%), var(--bg); font-family:Inter,sans-serif; }
    [data-testid="stHeader"] { background:transparent; }
    [data-testid="stSidebar"] { background:linear-gradient(180deg,#081423,#07111f); border-right:1px solid var(--line); }
    [data-testid="stSidebar"] > div:first-child { padding-top:1.4rem; }
    .brand-box { display:flex; align-items:center; gap:12px; padding:12px 8px 22px; }
    .brand-icon { width:42px;height:42px;border-radius:13px;display:grid;place-items:center;background:linear-gradient(135deg,#22d3ee,#6366f1);font-size:22px;box-shadow:0 10px 30px rgba(99,102,241,.25); }
    .brand-title { color:#fff;font-size:17px;font-weight:800;line-height:1.1; } .brand-subtitle { color:#64748b;font-size:11px;margin-top:3px; }
    .nav-label { color:#64748b;font-size:10px;font-weight:800;letter-spacing:1.5px;margin:4px 8px 10px; }
    .sidebar-divider { height:1px;background:var(--line);margin:20px 0; }
    .status-pill { display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:7px 10px;font-size:10px;font-weight:800;letter-spacing:.7px; }
    .status-pill span { width:7px;height:7px;border-radius:50%;display:inline-block; } .online { color:#67e8f9;background:rgba(34,211,238,.08); } .online span { background:#22d3ee;box-shadow:0 0 10px #22d3ee; } .offline { color:#fda4af;background:rgba(244,63,94,.08); } .offline span { background:#f43f5e; }
    .hero { position:relative;overflow:hidden;border:1px solid var(--line);border-radius:26px;padding:42px 46px;margin:5px 0 24px;background:linear-gradient(135deg,rgba(15,34,56,.96),rgba(10,21,37,.88));box-shadow:0 25px 70px rgba(0,0,0,.22); }
    .hero:after { content:'';position:absolute;width:280px;height:280px;border-radius:50%;right:-90px;top:-100px;background:radial-gradient(circle,rgba(103,232,249,.16),transparent 68%); }
    .hero-eyebrow { color:#67e8f9;font-size:11px;font-weight:800;letter-spacing:2px;margin-bottom:14px; }
    .hero-title { color:#f8fafc;font-size:44px;line-height:1.08;font-weight:800;letter-spacing:-1.5px; } .hero-title span { background:linear-gradient(90deg,#67e8f9,#818cf8);-webkit-background-clip:text;color:transparent; }
    .hero-text { color:#94a3b8;font-size:15px;max-width:690px;line-height:1.7;margin-top:16px; }
    .action-card,.kpi-card,.flow-card,.score-card { background:rgba(13,27,45,.82);border:1px solid var(--line);border-radius:18px; }
    .action-card { min-height:84px;padding:17px;display:flex;align-items:center;gap:14px;margin-bottom:8px;transition:.2s; } .action-card:hover { transform:translateY(-2px);border-color:rgba(103,232,249,.35); }
    .action-icon { width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:rgba(99,102,241,.13);font-size:20px; } .action-card b { color:#f8fafc;font-size:14px; } .action-card small { color:#64748b;font-size:11px; }
    .kpi-card { padding:20px;min-height:130px; } .kpi-tag { color:#64748b;font-size:9px;font-weight:800;letter-spacing:1.4px; } .kpi-value { color:#f8fafc;font-size:31px;font-weight:800;margin-top:14px; } .kpi-label { color:#94a3b8;font-size:12px;margin-top:3px; }
    .section-heading span { color:#67e8f9;font-size:9px;font-weight:800;letter-spacing:1.7px; } .section-heading h2 { color:#f8fafc;font-size:22px;margin:4px 0 16px; } .section-gap { height:10px; }
    .panel-title { color:#f8fafc;font-size:15px;font-weight:700;margin-bottom:12px; }
    .flow-card { padding:20px 22px; } .flow-step { display:flex;gap:14px;align-items:center; } .flow-number { min-width:35px;height:35px;border-radius:11px;display:grid;place-items:center;background:linear-gradient(135deg,rgba(34,211,238,.16),rgba(99,102,241,.18));color:#67e8f9;font-size:10px;font-weight:800; } .flow-step b { display:block;color:#e2e8f0;font-size:13px; } .flow-step small { display:block;color:#64748b;font-size:10px;margin-top:3px; } .flow-line { width:1px;height:18px;background:rgba(103,232,249,.2);margin:4px 0 4px 17px; }
    .career-name { color:#f8fafc;font-size:20px;font-weight:800; } .career-count { color:#64748b;font-size:11px;margin:3px 0 14px; } .skill-row { padding:9px 11px;border-bottom:1px solid rgba(148,163,184,.08);color:#cbd5e1;font-size:12px; } .skill-row span { color:#67e8f9;margin-right:8px; }
    .score-card { padding:18px; } .score-title { color:#94a3b8;font-size:11px; } .score-value { color:#f8fafc;font-size:25px;font-weight:800;margin:8px 0 10px; } .score-track { height:6px;border-radius:99px;background:#17283b;overflow:hidden; } .score-fill { height:100%;border-radius:99px;background:linear-gradient(90deg,#22d3ee,#818cf8); }
    .insight-banner { display:flex;gap:14px;align-items:center;padding:18px 20px;border:1px solid rgba(103,232,249,.15);border-radius:18px;background:linear-gradient(90deg,rgba(34,211,238,.06),rgba(99,102,241,.06)); } .insight-icon { font-size:24px; } .insight-banner b { color:#f8fafc;font-size:13px; } .insight-banner span { color:#94a3b8;font-size:11px;line-height:1.6; } .model-badge { margin-top:16px;color:#67e8f9;font-size:10px;font-weight:700;letter-spacing:.5px; } .offline-badge { color:#fda4af; }
    div.stButton > button { border-radius:11px;border:1px solid rgba(103,232,249,.15);background:rgba(13,27,45,.9);color:#cbd5e1;font-weight:600;transition:.2s; } div.stButton > button:hover { border-color:rgba(103,232,249,.45);color:#67e8f9; }
    [data-testid="stMetricValue"] { color:#f8fafc; } .stProgress > div > div { background:linear-gradient(90deg,#22d3ee,#818cf8); }
    input, textarea { background:#0b192a !important;color:#e2e8f0 !important; }
    footer { visibility:hidden; }
    @media (max-width:900px) { .hero-title {font-size:32px;} .hero {padding:30px 24px;} }
    </style>
    """, unsafe_allow_html=True
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

    st.markdown("""
    <div class="brand-box">
        <div class="brand-icon">🎓</div>
        <div>
            <div class="brand-title">AI Student</div>
            <div class="brand-subtitle">Intelligence System</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='nav-label'>WORKSPACE</div>", unsafe_allow_html=True)

    page = st.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👨‍🎓 Student Analysis",
        "💼 Career Intelligence",
        "🛣️ Skill Roadmap",
        "📊 Model Evaluation"
    ],
    label_visibility="collapsed"
   )

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='nav-label'>SYSTEM STATUS</div>", unsafe_allow_html=True)

    status_text = "ONLINE" if MODEL_AVAILABLE else "OFFLINE"
    status_class = "online" if MODEL_AVAILABLE else "offline"
    st.markdown(
        f"<div class='status-pill {status_class}'><span></span>{status_text} · ML MODEL</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
    st.caption("Built with Python · Scikit-learn · Streamlit")


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">✦ AI-POWERED STUDENT ANALYTICS</div>
        <div class="hero-title">Your academic journey,<br><span>decoded by AI.</span></div>
        <div class="hero-text">Understand academic outcomes, discover career gaps, and turn your next steps into a clear learning plan.</div>
    </div>
    """, unsafe_allow_html=True)

    # Primary actions
    a1, a2, a3 = st.columns([1, 1, 1], gap="medium")
    with a1:
        st.markdown("<div class='action-card'><div class='action-icon'>🎯</div><div><b>Predict Outcome</b><br><small>Analyze student performance</small></div></div>", unsafe_allow_html=True)
        if st.button("Open Student Analysis →", key="dash_student", use_container_width=True):
            st.session_state["dashboard_jump"] = "👨‍🎓 Student Analysis"
            st.rerun()
    with a2:
        st.markdown("<div class='action-card'><div class='action-icon'>💼</div><div><b>Explore Career</b><br><small>Find your skill gaps</small></div></div>", unsafe_allow_html=True)
        if st.button("Open Career Intelligence →", key="dash_career", use_container_width=True):
            st.session_state["dashboard_jump"] = "💼 Career Intelligence"
            st.rerun()
    with a3:
        st.markdown("<div class='action-card'><div class='action-icon'>🛣️</div><div><b>Build Roadmap</b><br><small>Turn gaps into action</small></div></div>", unsafe_allow_html=True)
        if st.button("Open Skill Roadmap →", key="dash_roadmap", use_container_width=True):
            st.session_state["dashboard_jump"] = "🛣️ Skill Roadmap"
            st.rerun()

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    # Platform overview
    st.markdown("<div class='section-heading'><span>LIVE OVERVIEW</span><h2>Intelligence at a glance</h2></div>", unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4, gap="medium")
    metrics = [
        (k1, "4,424", "Students analyzed", "DATASET"),
        (k2, "39", "Model features", "SIGNALS"),
        (k3, "3", "Outcome classes", "PREDICTION"),
        (k4, str(len(career_skills)), "Career paths", "CAREER AI"),
    ]
    for col, value, label, tag in metrics:
        with col:
            st.markdown(f"<div class='kpi-card'><div class='kpi-tag'>{tag}</div><div class='kpi-value'>{value}</div><div class='kpi-label'>{label}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    left, right = st.columns([1.35, 1], gap="large")

    with left:
        st.markdown("<div class='panel-title'>🧠 How the intelligence engine works</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="flow-card">
            <div class="flow-step"><div class="flow-number">01</div><div><b>Academic Profile</b><small>39 academic, demographic and economic signals</small></div></div>
            <div class="flow-line"></div>
            <div class="flow-step"><div class="flow-number">02</div><div><b>Random Forest</b><small>Analyzes patterns from historical student data</small></div></div>
            <div class="flow-line"></div>
            <div class="flow-step"><div class="flow-number">03</div><div><b>Outcome Intelligence</b><small>Dropout · Enrolled · Graduate probabilities</small></div></div>
            <div class="flow-line"></div>
            <div class="flow-step"><div class="flow-number">04</div><div><b>Career Action Plan</b><small>Skill gaps → personalized learning roadmap</small></div></div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("<div class='panel-title'>⚡ Quick career explorer</div>", unsafe_allow_html=True)
        dash_career = st.selectbox("Choose a career", list(career_skills.keys()), key="dashboard_career_select", label_visibility="collapsed")
        req = career_skills[dash_career]
        st.markdown(f"<div class='career-name'>{dash_career}</div><div class='career-count'>{len(req)} core skills</div>", unsafe_allow_html=True)
        for skill in req[:5]:
            st.markdown(f"<div class='skill-row'><span>✓</span>{skill}</div>", unsafe_allow_html=True)
        if len(req) > 5:
            st.caption(f"+ {len(req)-5} more skills in Career Intelligence")
        if st.button("Explore this career →", key="dash_explore", use_container_width=True):
            st.session_state["selected_career"] = dash_career
            st.session_state["dashboard_jump"] = "💼 Career Intelligence"
            st.rerun()

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    # Interactive readiness simulator
    st.markdown("<div class='section-heading'><span>INTERACTIVE</span><h2>Student readiness simulator</h2></div>", unsafe_allow_html=True)
    st.caption("Adjust the academic indicators to see how the dashboard communicates student progress. This is a visual simulator; the actual ML prediction is performed in Student Analysis.")
    s1, s2, s3 = st.columns(3, gap="medium")
    with s1:
        sim_sem1 = st.slider("Semester 1 approval", 0, 100, 80, 5, key="sim_sem1")
    with s2:
        sim_sem2 = st.slider("Semester 2 approval", 0, 100, 75, 5, key="sim_sem2")
    with s3:
        sim_skills = st.slider("Career skill coverage", 0, 100, 60, 5, key="sim_skills")

    avg = (sim_sem1 + sim_sem2) / 2
    overall = round((avg * 0.65) + (sim_skills * 0.35), 1)
    r1, r2, r3 = st.columns(3, gap="medium")
    for col, title, val, suffix in [(r1, "Academic Index", avg, "%"), (r2, "Career Readiness", sim_skills, "%"), (r3, "Overall Profile", overall, "%")]:
        with col:
            st.markdown(f"<div class='score-card'><div class='score-title'>{title}</div><div class='score-value'>{val:.1f}{suffix}</div><div class='score-track'><div class='score-fill' style='width:{min(val,100)}%'></div></div></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    # Product value
    st.markdown("<div class='insight-banner'><div class='insight-icon'>💡</div><div><b>Start with your profile</b><br><span>Run a student analysis first. Then use Career Intelligence to identify missing skills and generate a focused roadmap.</span></div></div>", unsafe_allow_html=True)

    if MODEL_AVAILABLE:
        st.markdown("<div class='model-badge'>● MODEL ONLINE &nbsp;·&nbsp; Random Forest &nbsp;·&nbsp; Prediction ready</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='model-badge offline-badge'>● MODEL OFFLINE &nbsp;·&nbsp; Check model path</div>", unsafe_allow_html=True)


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
        list(career_skills.keys()),
        index=list(career_skills.keys()).index(st.session_state.get("selected_career", list(career_skills.keys())[0])) if st.session_state.get("selected_career", list(career_skills.keys())[0]) in career_skills else 0
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
# MODEL EVALUATION
# ============================================================

elif page == "📊 Model Evaluation":

    st.title("📊 Model Evaluation")

    st.write(
        "Performance analysis of the trained "
        "student outcome prediction model."
    )

    if not MODEL_AVAILABLE:

        st.error(
            "The ML model is not available."
        )

    else:

        evaluation = get_evaluation()

        # ----------------------------------------------------
        # MODEL METRICS
        # ----------------------------------------------------

        st.markdown("### 📈 Model Performance")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Accuracy",
                f"{evaluation['accuracy'] * 100:.2f}%"
            )

        with col2:

            st.metric(
                "Macro F1 Score",
                f"{evaluation['macro_f1'] * 100:.2f}%"
            )

        with col3:

            st.metric(
                "Test Samples",
                evaluation["test_samples"]
            )

        st.markdown("---")

        # ----------------------------------------------------
        # CLASSIFICATION REPORT
        # ----------------------------------------------------

        st.markdown("### 📋 Classification Report")

        st.dataframe(
            evaluation["report_df"].round(3),
            use_container_width=True
        )

        st.markdown("---")

        # ----------------------------------------------------
        # CONFUSION MATRIX
        # ----------------------------------------------------

        st.markdown("### 🎯 Confusion Matrix")

        st.dataframe(
            evaluation["confusion_matrix_df"],
            use_container_width=True
        )

        st.markdown("---")

        # ----------------------------------------------------
        # FEATURE IMPORTANCE
        # ----------------------------------------------------

        st.markdown("### 🔎 Top Feature Importance")

        feature_importance = (
            evaluation["feature_importance"]
            .head(15)
        )

        st.bar_chart(
            feature_importance
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🎓 AI Student Success & Career Intelligence System | "
    "Built with Python, Scikit-learn and Streamlit"
)