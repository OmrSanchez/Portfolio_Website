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
st.write("---")

column_count = 2
df = pandas.read_csv(csv_path, sep=";")
columns = st.columns(column_count)

for index, row in df.iterrows():
	with columns[index % column_count]:
		with st.container(border=True, height=600):
			st.subheader(row['title'])
			st.markdown(f"###### {row["description"]}")
			st.write(f"[Source Code]({row['url']})")
			st.image("images/" + row["image"], use_container_width=True)
			st.write(row['goal'])

		st.write("---")