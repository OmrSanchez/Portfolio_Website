import streamlit as st
import pandas
from pathlib import Path

csv_path = Path(__file__).parent.parent / 'projects_data.csv'

st.header("My Projects")
# st.write("---")

df = pandas.read_csv(csv_path, sep=";")
col3, col4 = st.columns(2)

with col3:
	for index, row in df[:3].iterrows():
		with st.container(border=True):
			st.header(row['title'])
			st.write(row["description"])
			st.image("images/" + row["image"], use_container_width=True)
			st.write(row['goal'])
			st.write(f"[Source Code]({row['url']})")

with col4:
	for index, row in df[3:].iterrows():
		with st.container(border=True):
			st.header(row["title"])
			st.write(row["description"])
			st.image("images/" + row["image"], use_container_width=True)
			st.write(row['goal'])
			st.write(f"[Source Code]({row['url']})")