import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # Included for completeness, though px is mostly used

# --- 1. Configuration and Data Loading ---
st.set_page_config(
    layout="wide", 
    page_title="Arts Faculty Comprehensive Data Analysis 📊"
)

st.title('Arts Faculty Data Analysis: Student & Academic Insights')
st.markdown("---")

# URL for the data file
url = "https://raw.githubusercontent.com/AleyaNazifa/SVT13/refs/heads/main/arts_faculty_data.csv"

# Load the DataFrame from the URL and cache it
@st.cache_data
def load_data(data_url):
    """Loads the data from the URL and caches it to prevent reloading."""
    try:
        data = pd.read_csv(data_url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

arts_df = load_data(url)

if arts_df.empty:
    st.error("Data could not be loaded. Please check the URL and file.")
    st.stop()

# Rename columns for simpler access and use 'df' as the working DataFrame
df = arts_df.rename(columns={
    'S.S.C (GPA)': 'SSC_GPA',
    'H.S.C (GPA)': 'HSC_GPA',
    'Did you ever attend a Coaching center?': 'Coaching_Attendance',
    'Q7. In your opinion,the best aspect of the program is': 'Best_Program_Aspect'
})

# Display a Data Preview
st.header('1. Data Preview')
st.markdown("Displaying the first few rows of the dataset.")
st.dataframe(df.head())

st.markdown("---")

# --- 2. Gender Distribution (Pie Chart) ---
st.header('2. Gender Distribution')

if 'Gender' in df.columns:
    # Calculate the value counts for the 'Gender' column
    gender_counts = df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    # Create a Plotly Pie Chart
    fig_gender = px.pie(
        gender_counts,
        names='Gender',
        values='Count',
        title='Distribution of Gender in Arts Faculty',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_gender.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_gender, use_container_width=True)

    # Interpretation 1
    st.info("""
    **Interpretation 1: Gender Distribution**

    The pie chart shows that **female students** make up a slightly larger portion of the Faculty of Arts compared to male students. This indicates that the faculty attracts more female participants, which may reflect broader enrollment trends in arts and humanities disciplines. Such gender balance could influence teaching approaches and student engagement activities.
    """)
else:
    st.warning("The 'Gender' column is missing. Cannot generate the chart.")

st.markdown("---")

# --- 3. Average GPA Comparison (Bar Chart) ---
st.header('3. Average GPA Comparison')

try:
    gpa_means = df[['SSC_GPA', 'HSC_GPA']].mean().reset_index()
    gpa_means.columns = ['Level', 'Average_GPA']

    fig_gpa = px.bar(
        gpa_means,
        x='Level',
        y='Average_GPA',
        title='Average GPA Comparison (S.S.C vs H.S.C)',
        labels={'Level': 'Academic Level', 'Average_GPA': 'Average GPA'},
        color='Level',
        color_discrete_sequence=['#4B0082', '#00CED1'] # Custom colors
    )
    fig_gpa.update_layout(yaxis_title='Average GPA', xaxis_title='Academic Level')
    st.plotly_chart(fig_gpa, use_container_width=True)

    # Interpretation 2
    st.info("""
    **Interpretation 2: Average GPA Comparison (S.S.C vs H.S.C)**

    The bar chart reveals that students generally achieved **higher average GPA scores in the S.S.C** compared to the H.S.C examinations. This suggests that academic performance tends to decline slightly as students progress to higher levels of education, possibly due to increased academic difficulty or subject specialization. It may also highlight the need for better academic support at the higher secondary level.
    """)
except Exception as e:
    st.warning(f"Could not generate GPA Comparison chart: {e}")

st.markdown("---")

# --- 4. Coaching Center Attendance (Bar Chart) ---
st.header('4. Coaching Center Attendance')

try:
    coaching_counts = df['Coaching_Attendance'].value_counts().reset_index()
    coaching_counts.columns = ['Attendance', 'Count']

    fig_coaching = px.bar(
        coaching_counts,
        x='Attendance',
        y='Count',
        title='Coaching Center Attendance',
        labels={'Attendance': 'Attended Coaching Center', 'Count': 'Number of Students'},
        color='Attendance',
        color_discrete_map={'Yes': 'skyblue', 'No': 'salmon'}
    )
    fig_coaching.update_layout(yaxis_title='Number of Students', xaxis_title='Attended Coaching Center?')
    st.plotly_chart(fig_coaching, use_container_width=True)

    # Interpretation 3
    st.info("""
    **Interpretation 3: Coaching Center Attendance**

    The majority of students reported **not attending a coaching center**, as seen in the bar chart. This implies that most students relied on their formal education rather than external academic support. Those who did attend coaching centers may have sought additional help to strengthen specific subject areas, indicating varying learning strategies among students.
    """)
except Exception as e:
    st.warning(f"Could not generate Coaching Attendance chart: {e}")

st.markdown("---")

# --- 5. Expectation vs Reality (Box Plot) ---
st.header('5. Expectation vs Reality (Box Plot)')

expectation_cols = [
    'Q1 [What was your expectation about the University as related to quality of education?]',
    'Q2 [What was your expectation about the University as related to quality of Faculty?]',
    'Q3 [What was your expectation about the University as related to quality of resources?]',
    'Q4 [What was your expectation about the University as related to quality of learning environment?]',
    'Q5 [To what extent your expectation was met?]'
]

try:
    # Melt the DataFrame for Plotly Box Plot
    df_melt = df[expectation_cols].melt(
        var_name='Question',
        value_name='Rating'
    ).dropna()

    # Create a mapping for simplified labels
    label_map = {col: f'Q{i+1}' for i, col in enumerate(expectation_cols)}
    df_melt['Question_Label'] = df_melt['Question'].map(label_map)

    fig_box = px.box(
        df_melt,
        x='Question_Label',
        y='Rating',
        title='Expectation vs Reality (Box Plot)',
        labels={'Question_Label': 'Question', 'Rating': 'Rating (1–5)'},
        color='Question_Label'
    )
    fig_box.update_layout(yaxis_title='Rating (1–5)', xaxis_title='Question')
    st.plotly_chart(fig_box, use_container_width=True)

    # Interpretation 4
    st.info("""
    **Interpretation 4: Expectation vs Reality (Box Plot)**

    The box plot indicates that students had **consistently high expectations** (Q1–Q4) regarding educational quality, faculty, and learning resources, typically around a score of 4 to 5. However, the “extent expectations were met” (Q5) showed slightly lower median scores, suggesting a **moderate gap between student expectations and actual experiences**. This points to potential areas for institutional improvement to align outcomes with expectations.
    """)
except Exception as e:
    st.warning(f"Could not generate Expectation vs Reality chart: {e}")

st.markdown("---")

# --- 6. Top Aspects of the Program (Bar Chart) ---
st.header('6. Top Aspects of the Program')
st.write("Counts of the best aspect of the program as rated by the students.")

try:
    aspect_counts = df['Best_Program_Aspect'].value_counts().reset_index()
    aspect_counts.columns = ['Aspect', 'Count']

    fig_aspect = px.bar(
        aspect_counts,
        x='Aspect',
        y='Count',
        title='Top Aspects of the Program (Best Aspect)',
        labels={'Aspect': 'Aspect of Program', 'Count': 'Number of Students'},
        color='Aspect', # This line tells Plotly to color each bar based on the 'Aspect'
        color_discrete_sequence=px.colors.qualitative.Prism # Using a new qualitative color sequence
    )
    fig_aspect.update_layout(
        yaxis_title='Number of Students',
        xaxis_title='Aspect of Program',
        xaxis={'categoryorder':'total descending'}
    )
    fig_aspect.update_xaxes(tickangle=30)
    fig_aspect.update_traces(marker_line_width=1, marker_line_color="black") # Add borders
    st.plotly_chart(fig_aspect, use_container_width=True)

    # Interpretation 5
    st.info("""
    **Interpretation 5: Top Aspects of the Program**

    The bar chart highlights that **“Teaching and Learning” was the most appreciated aspect** of the program, followed by positive mentions of faculty quality and learning environment. This suggests that students value the direct teaching experience and instructor engagement the most. Focusing on sustaining and enhancing teaching quality could further boost student satisfaction and academic outcomes.
    """)
except Exception as e:
    st.warning(f"Could not generate Top Aspects chart: {e}")

st.markdown("---")
st.success("Analysis complete! All charts and interpretations are now displayed!")
