import streamlit as st
import pandas

df = pandas.read_csv("../data.csv", sep=";")
col3, col4 = st.columns([1.5, 1.5])

with col3:
	for index, row in df[:10].iterrows():
		st.header(row['title'])
		st.write(row["description"])
		st.image("images/" + row["image"])
		st.write("[Source Code]({row['url']})")

with col4:
	for index, row in df[10:].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])
		st.write("[Source Code]({row['url']})")