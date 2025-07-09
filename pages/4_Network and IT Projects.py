import streamlit as st
import pandas
from pathlib import Path

st.set_page_config(
	page_title="Network/Automation Projects",
	page_icon='🐍',
	layout='wide'
)


csv_path = Path(__file__).parent.parent / 'network_automation_projects_data.csv'

st.header("Network and IT Projects")

st.info("This page is currently a work in progress as I gather the necessary information.")

df = pandas.read_csv(csv_path, sep=";")