import streamlit as st
import pandas as pd

# Set up Streamlit layout and configuration
st.set_page_config(
    page_title="Sleep Health Analyzer",
    layout="wide"
)

# Main app header
st.title("Sleep Health Analyzer")
st.write("Welcome to the app!")

# Load data from CSV file
data = pd.read_csv("sleep.csv")

# Sidebar for user inputs
st.sidebar.title("Filter Data")
selected_occupation = st.sidebar.selectbox("Select Occupation", data["Occupation"].unique())
selected_age_range = st.sidebar.slider("Select Age Range", int(data["Age"].min()), int(data["Age"].max()), (int(data["Age"].min()), int(data["Age"].max())))

# Apply filters to the data
filtered_data = data[(data["Occupation"] == selected_occupation) & (data["Age"].between(selected_age_range[0], selected_age_range[1]))]

# Display filtered data
st.header("Filtered Data")
st.write(filtered_data)

# Sleep duration analysis
st.header("Sleep Duration Analysis")
st.subheader("Average Sleep Duration by Gender")
average_sleep_duration_gender = filtered_data.groupby("Gender")["Sleep Duration"].mean()
st.bar_chart(average_sleep_duration_gender)

# Quality of sleep analysis
st.header("Quality of Sleep Analysis")
st.subheader("Distribution of Quality of Sleep")
quality_of_sleep_counts = filtered_data["Quality of Sleep"].value_counts()
st.bar_chart(quality_of_sleep_counts)

# Other analyses and visualizations can be added here
