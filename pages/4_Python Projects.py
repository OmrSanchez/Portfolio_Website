import streamlit as st
import pandas
from pathlib import Path

st.set_page_config(
	page_title="Python Projects",
	page_icon='🐍',
	layout='wide'
)

csv_path = Path(__file__).parent.parent / 'python_projects_data.csv'

st.title("Python Projects")

df = pandas.read_csv(csv_path, sep=";")
columns = st.columns(3)

for index, row in df.iterrows():
	with columns[index % 3]:
		with st.container(border=True, height=600):
			st.subheader(row['title'])
			st.markdown(f"###### {row["description"]}")
			st.image("images/" + row["image"], width=325)
			st.write(row['goal'])
			st.write(f"[Source Code]({row['url']})")
		st.write("---")