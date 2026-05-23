import streamlit as st
import datetime

# Page Configuration
st.set_page_config(
    page_title="Uppseekers - Interactive Student Journey Matrix",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header { font-size: 36px; font-weight: 700; color: #1E3A8A; margin-bottom: 10px; }
    .sub-header { font-size: 18px; color: #4B5563; margin-bottom: 30px; }
    .section-card { background-color: #F3F4F6; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 5px solid #2563EB; }
    .timeline-badge { background-color: #DBEAFE; color: #1E40AF; padding: 4px 8px; border-radius: 4px; font-weight: 600; font-size: 14px; }
    .ops-badge { background-color: #FEF3C7; color: #92400E; padding: 4px 8px; border-radius: 4px; font-weight: 600; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-header">🌐 Uppseekers Student Journey Matrix</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Dynamic, counselor-led roadmap from enrollment to university admissions.</div>', unsafe_allow_html=True)

# --- SIDEBAR INPUTS ---
st.sidebar.header("📋 Student Profile Setup")
current_grade = st.sidebar.selectbox(
    "Select Current Grade Level:",
    options=["Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛠️ Core Tracking Parameters")
st.sidebar.info(
    "This dashboard dynamically filters the end-to-end journey starting from your selected grade down to Grade 12 Departure."
)

# --- UNIVERSAL 7-DAY ONBOARDING & ICP ENGINE ---
st.markdown("## ⚡ Phase 1: The Fast-Track 7-Day Onboarding & ICP Engine")
st.markdown("*Mandatory foundational launchpad for every newly onboarded student.*")

col1, col2 = st.columns(2)

with col1:
    with st.expander("📅 Days 1–3: Enrollment & Deep Discovery", expanded=True):
        st.markdown("**🔹 Day 1: Welcome & Document Hygiene**")
        st.markdown("- **What Happens:** Program Manager (PM) hosts welcome call. Dashboard access to **Zoho Learn** is provisioned.")
        st.markdown("- **Counsellor Action:** Initial review of historical transcripts (past 3 years) and passport validity check.")
        
        st.markdown("**🔹 Day 2–3: Ice-Breaking & Psychometric Launch**")
        st.markdown("- **What Happens:** Student completes the 45-minute online psychometric assessment.")
        st.markdown("- **Counsellor Action:** Conducts a relaxed profile discovery session to analyze behavioral traits and natural affinities.")

with col2:
    with st.expander("📅 Days 4–7: ICP Alignment & Batch Allocation", expanded=True):
        st.markdown("**🔹 Day 4–5: Profile Gap Analysis**")
        st.markdown("- **Counsellor Action:** Generates system-backed **AS-IS vs. TO-BE Profile Gap Report**. Maps initial country filters and program choices.")
        
        st.markdown("**🔹 Day 6–7: The Roadmap Freeze & Batching**")
        st.markdown("- **What Happens:** Core **ICP Alignment Meeting** with parents. Master 3+ Year Calendar is locked.")
        st.markdown("- **Ops Team Action:** Allocates student to active **Research Batches** or **Internship Tracks** based on availability.")

st.markdown("---")

# --- DYNAMIC TIMELINE GENERATOR ---
st.markdown(f"## 🗺️ Your Personalized Journey Matrix: Starting from {current_grade}")

# Grade Mapping Logistics
grade_list = ["Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"]
active_grades = grade_list[grade_list.index(current_grade):]

for idx, grade in enumerate(active_grades):
    st.markdown(f"### 🏫 {grade} Milestone Track")
    
    # ---------------- MIDDLE SCHOOL TRACKS ----------------
    if grade in ["Grade 6", "Grade 7", "Grade 8"]:
        tabs = st.tabs(["🎯 Core Focus & Academics", "🎭 Cocurriculars & Projects", "📂 Document Hygiene & Guardrails"])
        
        with tabs[0]:
            if grade == "Grade 6":
                st.markdown("**Academic Blueprint:** Focus on school curriculum mastery and foundational time-management habit building.")
            elif grade == "Grade 7":
                st.markdown("**Academic Blueprint:** Introduce light competitive frameworks like Olympiads or Asset exams to establish external benchmarking.")
            elif grade == "Grade 8":
                st.markdown("**Academic Blueprint:** Map future high school curriculum choices (IB, AP, A-Levels, National Boards) against long-term university ambitions.")
                
        with tabs[1]:
            if grade == "Grade 6":
                st.markdown("**Activities & Supercurriculars:** Explore introductory public speaking, debate circles, and reading groups. Focus on trial-and-error.")
            elif grade == "Grade 7":
                st.markdown("**Activities & Supercurriculars:** Commit to 2 school clubs. Initiate a micro-local community service project.")
            elif grade == "Grade 8":
                st.markdown("**Research & Internship Sprints:**")
                st.markdown("- **Week 3 Batch Placement:** Join the 3-to-4-month *Uppseekers Foundational Research Cohort* to learn basic writing and citation structures.")
                st.markdown("- **Real-World Exposure:** 1-week structured job shadowing or family business exposure.")

        with tabs[2]:
            st.markdown("<span class='timeline-badge'>Monthly Routine</span> **Document Upload:** Upload school report cards and milestone certificates every 30 days.", unsafe_allow_html=True)
            if grade == "Grade 7":
                st.markdown("<span class='ops-badge'>🚨 CRITICAL ALERT</span> **Passport Verification:** Parents must complete an audit of the student's passport. If not possessed or expiring, trigger application workflows.", unsafe_allow_html=True)
            st.markdown("<span class='ops-badge'>Counsellor Guardrail</span> Bi-weekly 45-minute strategy checkpoints with the student; monthly summary update loop with parents.", unsafe_allow_html=True)

    # ---------------- HIGH SCHOOL TRACKS ----------------
    else:
        tabs = st.tabs([
            "📚 Academics & Standardized Tests", 
            "🔬 Research, Internships & Activities", 
            "✍️ Essay Engine & LORs", 
            "💼 Applications, Finance & Visa"
        ])
        
        with tabs[0]:
            if grade == "Grade 9":
                st.markdown("**Academics Plan:** Start of official high school transcript. Target maximum GPA. Map out a 4-year strategic subject portfolio.")
                st.markdown("**Standardized Tests:** Exploration phase only. Build reading comprehension speed and baseline vocabulary.")
            elif grade == "Grade 10":
                st.markdown("**Academics Plan:** Board Examination focus year. Prioritize internal metrics and target specific national/international score brackets.")
                st.markdown("**Standardized Tests:** Run official diagnostic SAT/ACT/IELTS tests in Month 2. Finalize test-prep calendar timelines.")
            elif grade == "Grade 11":
                st.markdown("**Academics Plan:** Pivot to advanced subject rigor (AP, IB DP, or specialized streams). Closely monitor predicted score tracking.")
                st.markdown("**Standardized Tests:** **Sittings Window.** Take 1st official SAT/ACT/IELTS attempt between Months 3–5. Reserve Months 8–9 for strategic retakes.")
            elif grade == "Grade 12":
                st.markdown("**Academics Plan:** Maintain rigorous senior year academic grades. Confirm final predicted score matrices for submissions.")
                st.markdown("**Standardized Tests:** Send official score reports directly to final university application portals.")

        with tabs[1]:
            if grade == "Grade 9":
                st.markdown("**Activities Profile:** Identify a clear thematic narrative. Select 3 core school clubs to target for executive leadership tracks.")
                st.markdown("**Research Batch:** Enroll in a 4-month structured research cohort to co-author a foundational domain whitepaper.")
            elif grade == "Grade 10":
                st.markdown("**Activities Profile:** Secure active officer/committee positions. Enter regional/national hackathons, MUNs, or pitch fests.")
                st.markdown("**Internship Batch:** *Summer Window.* Complete an industry-aligned corporate internship. Ensure reflection logs are added to the portal.")
            elif grade == "Grade 11":
                st.markdown("**The Activity List:** Compile the Top 10 activities matching Common App 150-character limit rules. Launch a major independent Passion Project.")
                st.markdown("**Advanced Research Batch:** Pair 1:1 with a domain mentor to draft an advanced independent paper targeting peer-reviewed publications.")
            elif grade == "Grade 12":
                st.markdown("**Asset Consolidation:** Lock down and polish the final resume, activity portfolios, and supplemental creative/research design exhibits.")

        with tabs[2]:
            if grade in ["Grade 9", "Grade 10"]:
                st.markdown("**📝 The 150-Word Weekly Reflective Writing Habit**")
                st.markdown("- *Student Action:* Every single Friday, upload a 150-word micro-essay detailing a challenge, achievement, or perspective change from the week.")
                st.markdown("- *Counsellor Action:* Evaluate submissions monthly to extract raw, organic narrative seeds for ultimate college essays.")
            elif grade == "Grade 11":
                st.markdown("**Essay Development:** Transition the 150-word weekly habit into formal brainstorming workshops. Generate 3 core Personal Statement seeds.")
                st.markdown("**LOR Strategy:** Identify 2 academic teachers and 1 counsellor for recommendation pipelines. Provide them with Uppseekers Brag Sheets.")
            elif grade == "Grade 12":
                st.markdown("**The Writing Marathon (June - August):**")
                st.markdown("- Finalize the core **Common App Personal Statement**.")
                st.markdown("- Draft specialized, tailor-made **Supplemental Essays** (*Why Us, Why This Major*).")
                st.markdown("- Lock, polish, and review the **SOP / Statement of Purpose** for UK/Canadian portals.")

        with tabs[3]:
            st.markdown("<span class='timeline-badge'>Documentation Hygiene</span> **Every 30 Days:** Mandatorily upload report cards, certificates, and mock test datasets to the dashboard.", unsafe_allow_html=True)
            
            if grade == "Grade 9":
                st.markdown("**Financial Horizon Tracking:** Parents complete financial parameters assessment (budget limits, financial aid requirements, merit eligibility flags).")
            elif grade == "Grade 10":
                st.markdown("**Immigration Hygiene:** Mid-year audit of passport validity. Preliminary visa pathway alignment mapping.")
            elif grade == "Grade 11":
                st.markdown("**University Shortlisting:** Formulate a tentative roster of 20 universities categorized cleanly across Reach, Match, and Safety limits.")
            elif grade == "Grade 12":
                st.markdown("#### 🚀 The Application Timeline Window")
                st.markdown("- **Sept – Nov:** Direct application form filling support. Submit **Early Action (EA) / Early Decision (ED)** packages.")
                st.markdown("- **Dec – Jan:** Finalize **Regular Decision (RD)** applications. Execute intensive interview prep with mock feedback loops.")
                st.markdown("- **Feb – Apr:** Track application portals for missing metrics. Evaluate acceptance offers and scholarship awards. Pay final enrollment deposit.")
                st.markdown("- **May – Sept:** **Visa Engineering Phase.** Collate bank letters, affidavits of support, and complete mock visa interview sessions. Host pre-departure briefings.")
                st.markdown("- **Post-Departure (Day 7–15):** Execute post-arrival closure checks to transition the file to the alumni ecosystem.")

    st.markdown("---")

# --- GENERAL OPS & AUDIT MATRIX ---
st.markdown("## 🛡️ Internal Operations & Quality Guardrails")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("### 👥 Counselor Playbook")
    st.markdown("1. **Weekly 45-Min Sprints:** Unblock student timeline tasks and review the weekly writing habit metrics.")
    st.markdown("2. **Document Auditing:** Verify every upload against standard institutional parameters before verifying the credential status.")

with col_b:
    st.markdown("### 👪 Parent Transparency")
    st.markdown("1. **Monthly Review Loops:** Mandatory 30-minute monthly deep-dives to review calendar milestones and track progress.")
    st.markdown("2. **Strategic Freeze:** Shortlists and major profile alterations require documented parental sign-off.")

with col_c:
    st.markdown("### 📊 Ops Team Audits")
    st.markdown("1. **CRM Red-Flag Logs:** The platform monitors counselor touchpoints weekly. Any missed milestone triggers a 48-hour operational alert.")
    st.markdown("2. **Cohort Management:** Systematically balance capacity across the active **Research Batches** and **Internship Cohorts**.")
