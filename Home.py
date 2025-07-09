import streamlit as st
import pandas
from PIL import Image

st.set_page_config(
    page_title="Omar Sanchez | Network & Automation Engineer",
    page_icon="🔗",
    layout="wide"
)

col1, col2 = st.columns([0.4, 0.6], gap="Large")

with col1:
	profile_pic = "images/photo.jpg"
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

st.write("---")
st.subheader("Technical Skills & Expertise")

skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.markdown("""
    ##### Routing & Switching
    - BGP, OSPF, MPLS, VPLS
    - STP, VLANs, VRF
    - Cisco IOS, Brocade IOS
    """)

with skill_col2:
    st.markdown("""
    ##### Automation & Programming
    - Python, Ansible, REST APIs
    - Git & Version Control
    - Cisco NSO (Conceptual)
    """)

with skill_col3:
    st.markdown("""
    ##### Security & Virtualization
    - Firewalls, VPNs, STIGs
    - NAC (802.1x), ISE, RADIUS
    - VMWare, Docker, GNS3
    """)


# df = pandas.read_csv("data.csv", sep=";")
# col3, col4 = st.columns([1.5, 1.5])
#
# with col3:
# 	for index, row in df[:10].iterrows():
# 		st.header(row['title'])
# 		st.write(row["description"])
# 		st.image("images/" + row["image"])
# 		st.write("[Source Code]({row['url']})")
#
# with col4:
# 	for index, row in df[10:].iterrows():
# 		st.header(row["title"])
# 		st.write(row["description"])
# 		st.image("images/" + row["image"])
# 		st.write("[Source Code]({row['url']})")

