import streamlit as st
import pandas
from pathlib import Path

csv_path = Path(__file__).parent.parent / 'network_and_it_projects_data.csv'

st.header("Network and IT Projects")

st.info("This page is currently a work in progress as I gather the necessary information.")

df = pandas.read_csv(csv_path, sep=";")