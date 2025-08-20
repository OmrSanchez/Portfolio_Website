import streamlit as st

BASE_URL = "https://odsnetworking.streamlit.app/"

st.set_page_config(
    page_title="Omar Sanchez | Network & Automation Engineer",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="auto"
)

col1, col_empty, col2 = st.columns([0.85, 0.1, 0.4], gap='Small')

with col1:
    with st.container(height=500, border=False):
        st.title("Omar D. Sanchez")
        st.subheader("Network & Automation Engineer")
        st.write("USMC Veteran | Secret Cleared")
        content = """
        I am a highly motivated and results-driven Network & Automation Engineer, bringing over nine years of dedicated experience from the demanding world of Department of Defense network infrastructures. My journey began in the U.S. Marine Corps, where I learned to build, secure, and maintain mission-critical communication systems under pressure. Today, I apply that same focus and a security-first mindset to the modern enterprise, specializing in designing resilient architectures, implementing robust security protocols, and, most importantly, automating complex operations with tools like Python and Ansible to create more intelligent and efficient networks.
        """
        st.info(content)

with col2:
    with st.container(height=450, border=False):
        profile_pic = "images/photo.jpg"
        st.image(profile_pic, caption='Omar Sanchez', width=375)
        st.write(
            "[📲 LinkedIn](https://linkedin.com/in/os-networks) | "
            "[💻 GitHub](https://github.com/OmrSanchez)")

with col_empty:
    st.write()

st.write("---")


st.markdown("## Technical Skills & Expertise")
st.write("---")

# Create a two-column layout
col1, col2 = st.columns(2, gap="medium")

# Populate the first column
with col1:
    # Container for Routing & Switching skills
    with st.container(border=True, height=250):
        st.markdown(
            """
            #### Routing & Switching
            * **Routing Protocols:** OSPF, BGP, HSRP, Static & Default Routing
            * **Switching Protocols:** STP (RPVST+), EtherChannel (LACP & PAgP), VTP, VLANs & 802.1Q Trunks
            * **IP Addressing:** IPv4, IPv6, Subnetting, VLSM
            * **Vendor Platforms:** Cisco IOS, Brocade IOS
            """
        )

    # Container for Network Security skills
    with st.container(border=True, height=260):
        st.markdown(
            """
            #### Network Security
            * **Access Control:** ACLs (Standard, Extended), Port Security, NAC (802.1x), RADIUS
            * **Threat Mitigation:** DHCP Snooping, Dynamic ARP Inspection (DAI)
            * **Infrastructure Security:** Firewalls, VPNs, NAT/PAT
            * **Compliance & Hardening:** STIGs
            """
        )

# Populate the second column
with col2:
    # Container for Automation & Programming skills
    with st.container(border=True, height=250):
        st.markdown(
            """
            #### Automation & Programming
            * **Languages & Tools:** Python, Ansible, Git & Version Control
            * **Frameworks & APIs:** NETCONF, RESTCONF, REST APIs, Cisco NSO
            """
        )

    # Container for Services & Virtualization skills
    with st.container(border=True, height=250):
        st.markdown(
            """
            #### Network Services & Virtualization
            * **Core Services:** DHCP Server & Relay, DNS, NTP, SNMP, Syslog
            * **Virtualization Platforms:** GNS3, VMware, Docker
            """
        )

# Add a final horizontal line to conclude the section
st.write("---")
st.subheader("Featured Projects")
st.write(
    "A selection of projects that showcase my skills in network design, automation, and application development. *(More projects available on the 'Projects' page)*")
st.write("")

proj_col1, proj_col2 = st.columns(2)

# Project Card 1
with proj_col1:
    with st.container(border=True, height=600):
        st.subheader("WGU Capstone - Network PT")
        st.write(
            "A comprehensive capstone project involving the design, implementation, and testing of a secure, multi-site enterprise network. The architecture features a collapsed-core design, a site-to-site IPsec VPN, and high availability with HSRP. The network utilizes a hybrid routing scheme with BGP for external connectivity and OSPF for internal routing, all supported by a full suite of centralized network services and a multi-layered security model including firewalls, ACLs, and 802.1x.")
        st.image('net_images/net_7.png', width=575)
        st.link_button("View Project Details", f"{BASE_URL}Network_Projects")

# Project Card 2
with proj_col2:
    with st.container(border=True, height=600):
        st.subheader("Dual Site 3-Tier Network Lab")
        st.write(
            "A comprehensive GNS3 simulation of a resilient, dual-site enterprise network using a three-tier architecture. Implements OSPF, HSRP, NAT, and advanced Layer 2 security.")
        st.image('net_images/net_8.png', width=550)
        st.link_button("View Project Details", f"{BASE_URL}Network_Design_Automation_&_IT_Projects")


proj_col3, proj_col4 = st.columns(2)

# Project Card 3
with proj_col3:
    with st.container(border=True, height=600):
        st.subheader("Tic-Tac-Toe")
        st.write(
            "A guizero-based Tic-Tac-Toe game. Uses colors instead of symbols to track player turns.")
        st.image('images/8.png', width=400)
        st.link_button("View Project Details", f"{BASE_URL}Python_Projects")

with proj_col4:
    with st.container(border=True, height=600):
        st.subheader("Network Performance Tracking and Sniffing")
        st.write(
            "Establish a foundation of utilizing performance monitor to collect network traffic and showcase familiarity with Wireshark for sniffing.")
        st.video('net_videos/Project - Basic Network Performance Monitoring and Sniffing.mp4', width=550)
        st.link_button("View Project Details", f"{BASE_URL}Network_Projects")
