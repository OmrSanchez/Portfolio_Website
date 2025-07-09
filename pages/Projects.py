import streamlit as st
import pandas
from pathlib import Path

csv_path = Path(__file__).parent.parent / '..data.csv'


df = pandas.read_csv(csv_path, sep=";")
col3, col4 = st.columns([1.5, 1.5])

with col3:
	for index, row in df[:10].iterrows():
		st.header(row['title'])
		st.write(row["description"])
		st.image("images/" + row["image"])
		st.write(f"[Source Code]({row['url']})")

with col4:
	for index, row in df[10:].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])
		st.write(f"[Source Code]({row['url']})")