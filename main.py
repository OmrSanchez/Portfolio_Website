import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
	st.image("images/photo.jpg", width=700)

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