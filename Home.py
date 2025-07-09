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
	st.image("images/photo.jpg", width=400)

with col2:
	st.title("Omar D. Sanchez")
	content = """
	Network Engineer and Marine Corps Veteran with over 9 years of experience and an active Secret clearance. Specializes in designing, 
	implementing, and securing complex, multi-protocol DoD network infrastructures. Proven expertise in multivendor environments (Cisco, VMWare), 
	advanced routing (BGP/OSPF), and leveraging automation (Python/Ansible) to enhance network performance. IAT Level II compliant (Security+), 
	with CCNA and DevNet certifications.
	"""

	st.info(content)

body_text = """
	Below you can find some of the apps I have built in Python. Feel free to contact me!
	"""
st.write(body_text)

df = pandas.read_csv("data.csv", sep=";")
col3, col_empty, col4 = st.columns([1.5, 0.5, 1.5])

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

