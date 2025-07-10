import streamlit as st

BASE_URL = "https://odsnetworking.streamlit.app/"

st.set_page_config(
    page_title="Omar Sanchez | Network & Automation Engineer",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="auto"
)

col1, col_empty, col2 = st.columns([0.8, 0.1,0.4], gap='Large')

with col1:
    with st.container():
        st.title("Omar D. Sanchez")
        st.subheader("Network & Automation Engineer | USMC Veteran")
        content = """
        I am a highly motivated and results-driven Network & Automation Engineer, bringing over nine years of dedicated experience from the demanding world of Department of Defense network infrastructures. My journey began in the U.S. Marine Corps, where I learned to build, secure, and maintain mission-critical communication systems under pressure. Today, I apply that same focus and a security-first mindset to the modern enterprise, specializing in designing resilient architectures, implementing robust security protocols, and, most importantly, automating complex operations with tools like Python and Ansible to create more intelligent and efficient networks.
        """
        st.info(content)
        st.write(
            "[🔗 LinkedIn](https://linkedin.com/in/os-networks) | "
            "[🐙 GitHub](https://github.com/OmrSanchez)")

with col2:
    with st.container():
        profile_pic = "images/photo.jpg"
        st.image(profile_pic, caption='Omar Sanchez')

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
        st.subheader("Network Performance Tracking and Sniffing")
        st.write(
            "Establish a foundation of utilizing performance monitor to collect network traffic and showcase familiarity with Wireshark for sniffing.")
        st.video('net_videos/Project - Basic Network Performance Monitoring and Sniffing.mp4')
        st.link_button("View Project Details", f"{BASE_URL}Network_Automation_&_IT_Projects")

# Project Card 2
with proj_col2:
    with st.container(border=True):
        st.subheader("Tic-Tac-Toe")
        st.write(
            "A guizero-based Tic-Tac-Toe game. Uses colors instead of symbols to track player turns.")
        st.image('images/8.png')
        st.link_button("View Project Details", f"{BASE_URL}Python_Projects")

# Project Card 3
with proj_col3:
    with st.container(border=True):
        st.subheader("Password Manager GUI")
        st.write(
            "A password manager built in Python. Support password generation and login search and lookup. MVC and Tkinter.")
        st.image('images/4.png')
        st.link_button("View Project Details", f"{BASE_URL}Python_Projects")  # Placeholder link
