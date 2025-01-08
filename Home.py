import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
	st.image("images/photo.jpg", width=400)

with col2:
	st.title("Omar D. Sanchez")
	content = """
	Network administrator  and veteran with 7 years of experience of troubleshooting, ensuring the 
	stable operation of computer network and connected PC’s. Pursuing a Bachelor of Science in Network 
	Engineering and Security. Strong knowledge of TCP/IP protocol and experience troubleshooting ISP/WAN 
	and vendor hardware for repair. Specialized with working in various dynamic teams and 
	environments and consistently commended for initiative, leadership, and ability to complete essential 
	tasks on time and accurately. Learning to use Python for network automation and cybersecurity is a 
	skill I enjoy practicing as a hobby.
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

