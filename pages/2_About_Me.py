import streamlit as st
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")

img_path = Path(__file__).parent.parent / 'images/about_photo.png'

# --- HERO SECTION ---
st.title("About Me")
st.write("---")

# --- MAIN CONTENT ---
st.subheader('My Journey: From the Battlefield to the Backbone of Technology')

st.write("""
    My passion for network engineering was forged in one of the most demanding environments imaginable: the United States Marine Corps. For
eight years, I wasn't just supporting communications; I was on the digital front lines, leading teams and engineering secure satellite
networks where 99.9% uptime wasn't a goal, it was the mission. That experience, where every signal matters, ignited an unwavering drive in 
me to build and protect the systems that connect our world.

    Transitioning from the military wasn't an end, but an acceleration. I dove headfirst into the technologies that form the digital nervous
system of modern enterprise, driven by a relentless curiosity to master everything from the physical layer to the application. This wasn't
just about earning certifications—it was about a structured, aggressive pursuit of deep, practical knowledge in networking, security, and
the future of automation.""")

st.subheader('An Accelerated Timeline of Key Milestones')


st.write("""
• January 2016: Began my journey of service and technical leadership with the U.S. Marine Corps.

• February 2024: Honorably concluded eight years of service as a Sergeant, immediately pivoting my focus to a full-time career in network engineering.

• June 2025: Achieved a trifecta of modern Cisco certifications, earning the CCNA, DevNet Associate, and Cybersecurity Associate to build a 
    comprehensive, multi-disciplinary skill set.

• August 2025: Successfully completed my university Capstone Project, where I designed, built, and tested a complex, multi-site enterprise 
    network from the ground up.

• August 2025: Officially earned my Bachelor of Science in Network Engineering and Security, completing a rigorous, hands-on degree program.
""")

st.subheader("My Philosophy: Build, Automate, and Secure")

st.write("""
I believe the best engineers are perpetual students, and I live that philosophy every day. Whether I'm in my home lab breaking and fixing BGP routing scenarios, building a new Python application in my portfolio, or studying emerging security threats, I am constantly pushing the boundaries of my skill set.

My goal is to be more than just an administrator who maintains systems; I am an engineer who actively improves them through intelligent design and automation. I'm not just looking for a job—I'm looking for a new mission. I am eager to bring my unique blend of military discipline, technical expertise, and a security-first mindset to a team where I can help solve complex challenges and contribute to building the resilient and impenetrable networks of the future.
    """
)
