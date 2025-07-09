import streamlit as st

st.set_page_config(
    page_title="Omar Sanchez | Network & Automation Engineer",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="auto"
)

col1, col_empty, col2 = st.columns([0.8, 0.2,0.4], gap='Large')

with col1:
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

with col2:
    with st.container():
        profile_pic = "images/photo.jpg"
        st.image(profile_pic, width=250, caption='Omar Sanchez')

with col_empty:
    st.write()

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

st.write("---")
st.subheader("Featured Projects")
st.write(
    "A selection of projects that showcase my skills in automation and application development. *(More projects available on the 'Projects' page)*")
st.write("")

proj_col1, proj_col2, proj_col3 = st.columns(3)

# Project Card 1
with proj_col1:
    with st.container(border=True):
        st.subheader("Network API Automation")
        st.write(
            "Python scripts utilizing REST APIs to automate monitoring and configuration tasks for Cisco Meraki and DevNet sandboxes.")
        # When you create your projects page, you'll link to it here
        st.link_button("View Project Details", "#")  # Placeholder link

# Project Card 2
with proj_col2:
    with st.container(border=True):
        st.subheader("PDF Invoice Generator")
        st.write(
            "Practical automation script that parses Excel data to programmatically generate PDF invoices, saving significant manual effort.")
        st.link_button("View Project Details", "#")  # Placeholder link

# Project Card 3
with proj_col3:
    with st.container(border=True):
        st.subheader("Password Manager GUI")
        st.write(
            "A secure, user-friendly desktop application built with Python, TKinter, and the MVC design pattern for local password management.")
        st.link_button("View Project Details", "#")  # Placeholder link
