# Import required libraries
import streamlit as st  # For building interactive web apps
import pandas as pd     # For data manipulation
import matplotlib.pyplot as plt  # For static plotting
import plotly_express as px      # For interactive plotting

# Set the title and description of the Streamlit app
st.title("Earthquake Data Explorer")
st.text("This is a simple Streamlit app to explore earthquake data")

# --- Helper Functions ---
def stats(dataframe):
    """Display basic statistics of the uploaded data using pandas describe()."""
    st.header("Data Statistics")
    st.write(dataframe.describe())
    
def header(dataframe):
    """Show the first few rows of the data for a quick preview."""
    st.header("Data Header")
    st.write(dataframe.head())
    
def visualization(dataframe):
    """Visualize Depth vs Magnitude as a static scatter plot using matplotlib."""
    st.header("Data Visualization")
    st.write("This is a scatter plot of Depth vs Magnitude")
    fig, ax = plt.subplots(1,1)
    # Scatter plot: each point represents an earthquake event
    ax.scatter(x=dataframe['Depth'], y=dataframe['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    ax.set_title('Depth vs Magnitude')
    st.pyplot(fig)
    
def interactive_viz(dataframe):
    """Create an interactive scatter plot using Plotly, allowing user to pick axes and color."""
    # Dropdowns for user to select which columns to plot
    x_axis_val = st.selectbox("Select X-axis", dataframe.columns)
    y_axis_val = st.selectbox("Select Y-axis", dataframe.columns)
    # Color picker for customizing marker color
    col = st.color_picker("Pick a color")
    # Create interactive scatter plot
    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val, title=f'Interactive {x_axis_val} vs {y_axis_val}')
    plot.update_traces(marker=dict(size=5, color=col, line=dict(width=2)))
    st.plotly_chart(plot)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
# File uploader widget in the sidebar for CSV files
uploaded_file = st.sidebar.file_uploader("Choose a CSV file to Upload", type="csv")
# Sample data for this project was downloaded from Github
# https://github.com/andymcdgeo/streamlit_tutorial_series/blob/main/data/kaggle_significant_earthquakes_database.csv

# Sidebar radio buttons for navigating between different pages/views
options = st.sidebar.radio('Pages', options=["Home", "Data Statistics", "Data Header", "Data Visualization", "Interactive Viz"])

# --- Main App Logic ---
# Only proceed if a file is uploaded
if uploaded_file is not None:
    # Read the uploaded CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    # Show different content based on the selected page
    if options == "Home":
        st.write("Welcome to the Earthquake Data Explorer! Upload a CSV file to get started.")
    elif options == "Data Statistics":
        stats(df)
    elif options == "Data Header":
        header(df)
    elif options == "Data Visualization":
        visualization(df)
    elif options == "Interactive Viz":
        interactive_viz(df)