import streamlit as st
import pandas
from PIL import Image

st.set_page_config(
    page_title="Omar Sanchez | Network & Automation Engineer",
    page_icon="🔗",
    layout="wide"
)

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
	profile_pic = Image.open("images/photo.jpg")
	st.image(profile_pic, width=400, caption='Omar Sanchez')

with col2:
	st.title("Omar D. Sanchez")
	st.subheader("Network & Automation Engineer | USMC Veteran")
	content = """
	Highly motivated and results-driven with over 9 years of experience designing,
        securing, and automating complex DoD network infrastructures.
	"""

	st.info(content)
	st.write(
		"[🔗 LinkedIn](https://linkedin.com/in/os-networks) | "
		"[🐙 GitHub](https://github.com/OmrSanchez)")
body_text = """
	Below you can find some of the apps I have built in Python. Feel free to contact me! Test TEXT
	"""
st.write(body_text)

df = pandas.read_csv("data.csv", sep=";")
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

