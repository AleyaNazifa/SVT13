import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization")

# URL for the data file
url = "https://raw.githubusercontent.com/AleyaNazifa/SVT13/refs/heads/main/arts_faculty_data.csv"

# Set the title for the Streamlit application
st.title('Arts Faculty Data Analysis')

## Data Loading and Preview

# Load the DataFrame from the URL
@st.cache_data
def load_data(data_url):
    """
    Loads the data from the URL and caches it to prevent reloading.
    """
    try:
        data = pd.read_csv(data_url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

arts_df = load_data(url)

# Display the first few rows of the DataFrame
if not arts_df.empty:
    st.subheader('Data Preview (First 5 Rows)')
    st.dataframe(arts_df.head())
else:
    st.warning("Could not load data. Check the URL and file format.")


# Check if the 'Gender' column exists and is not empty before charting
if 'Gender' in arts_df.columns and not arts_df.empty:
    st.subheader('Gender Distribution')

    # Calculate the value counts for the 'Gender' column
    gender_counts = arts_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    ## Plotly Pie Chart

    # Create a Plotly Pie Chart
    fig = px.pie(
        gender_counts,
        names='Gender',          # Column to use for the sectors' names (labels)
        values='Count',          # Column to use for the sectors' sizes
        title='Distribution of Gender in Arts Faculty',
        color_discrete_sequence=px.colors.qualitative.Set3 # Optional: set a color palette
    )

    # Optional: Customize the appearance for better presentation
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("The 'Gender' column is missing or the DataFrame is empty. Cannot generate the chart.")
