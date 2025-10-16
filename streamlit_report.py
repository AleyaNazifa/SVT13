import streamlit as st

def main():
    """
    Renders the data analysis interpretations for the Faculty of Arts data using Streamlit.
    This script is designed to be deployed as a web application.
    """
    # --- Configuration and Styling ---
    st.set_page_config(
        page_title="Faculty of Arts Data Analysis",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Faculty of Arts Student Data: Key Interpretations")
    st.markdown("---")

    st.subheader("Summary of Insights from Demographic and Academic Data")
    st.markdown(
        """
        The following five points summarize the key findings derived from the compiled demographic, academic performance, and satisfaction data collected from students in the Faculty of Arts program.
        """
    )

    # --- Interpretation 1: Gender Distribution ---
    st.markdown("### 1. Gender Distribution: Enrollment Demographics")
    st.info("""
    The pie chart shows that **female students** make up a slightly larger portion of the Faculty of Arts compared to male students. This indicates that the faculty attracts more female participants, which may reflect broader enrollment trends in arts and humanities disciplines. Such gender balance could influence teaching approaches and student engagement activities.
    """)

    # --- Interpretation 2: Average GPA Comparison ---
    st.markdown("### 2. Average GPA Comparison (S.S.C vs H.S.C): Academic Performance Trends")
    st.info("""
    The bar chart reveals that students generally achieved **higher average GPA scores in the S.S.C** compared to the H.S.C examinations. This suggests that academic performance tends to decline slightly as students progress to higher levels of education, possibly due to increased academic difficulty or subject specialization. It may also highlight the need for better academic support at the higher secondary level.
    """)

    # --- Interpretation 3: Coaching Center Attendance ---
    st.markdown("### 3. Coaching Center Attendance: Learning Strategies")
    st.info("""
    The majority of students reported **not attending a coaching center**, as seen in the bar chart. This implies that most students relied on their formal education rather than external academic support. Those who did attend coaching centers may have sought additional help to strengthen specific subject areas, indicating varying learning strategies among students.
    """)

    # --- Interpretation 4: Expectation vs Reality (Box Plot) ---
    st.markdown("### 4. Expectation vs Reality (Box Plot): Alignment of Outcomes")
    st.info("""
    The box plot indicates that students had **consistently high expectations** (Q1–Q4) regarding educational quality, faculty, and learning resources, typically around a score of 4 to 5. However, the “extent expectations were met” (Q5) showed slightly lower median scores, suggesting a **moderate gap between student expectations and actual experiences**. This points to potential areas for institutional improvement to align outcomes with expectations.
    """)

    # --- Interpretation 5: Top Aspects of the Program ---
    st.markdown("### 5. Top Aspects of the Program: Program Strengths")
    st.info("""
    The bar chart highlights that **“Teaching and Learning” was the most appreciated aspect** of the program, followed by positive mentions of faculty quality and learning environment. This suggests that students value the direct teaching experience and instructor engagement the most. Focusing on sustaining and enhancing teaching quality could further boost student satisfaction and academic outcomes.
    """)

    st.markdown("---")
    st.caption("End of Data Analysis Report.")

if __name__ == "__main__":
    main()
