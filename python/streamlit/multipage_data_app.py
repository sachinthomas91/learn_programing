# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title and description of the Streamlit app
st.title("Earthquake Data Explorer")
st.text("This is a simple Streamlit app to explore earthquake data")

def stats(dataframe):
    """Display basic statistics of the uploaded data."""
    st.header("Data Statistics")
    st.write(dataframe.describe())
    
def header(dataframe):
    """Show the first few rows of the data."""
    st.header("Data Header")
    st.write(dataframe.head())
    
def visualization(dataframe):
    """Visualize Depth vs Magnitude as a scatter plot."""
    st.header("Data Visualization")
    st.write("This is a scatter plot of Depth vs Magnitude")
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=dataframe['Depth'], y=dataframe['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    ax.set_title('Depth vs Magnitude')
    st.pyplot(fig)

st.sidebar.title("Navigation")
# File uploader widget for CSV files
uploaded_file = st.sidebar.file_uploader("Choose a CSV file to Upload", type="csv")
# Sample data for this project was downloaded from Github
# https://github.com/andymcdgeo/streamlit_tutorial_series/blob/main/data/kaggle_significant_earthquakes_database.csv

options = st.sidebar.radio('Pages', options=["Home", "Data Statistics", "Data Header", "Data Visualization"])

# If a file is uploaded, process and display the data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if options == "Home":
        st.write("Welcome to the Earthquake Data Explorer!")
    elif options == "Data Statistics":
        stats(df)
    elif options == "Data Header":
        header(df)
    elif options == "Data Visualization":
        visualization(df)
    elif options == "Data Statistics":
        stats(df)