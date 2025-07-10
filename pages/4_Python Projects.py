import streamlit as st
import pandas
from pathlib import Path

st.set_page_config(
	page_title="Python Projects",
	page_icon='🐍',
	layout='wide'
)

csv_path = Path(__file__).parent.parent / 'python_projects_data.csv'

st.header("Python Projects")

df = pandas.read_csv(csv_path, sep=";")
columns = st.columns(4)

for index, row in df.iterrows():
	with columns[index % 4]:
		with st.container(border=True):
			st.header(row['title'])
			st.write(row["description"])
			st.image("images/" + row["image"], use_container_width=True)
			st.write(row['goal'])
			st.write(f"[Source Code]({row['url']})")