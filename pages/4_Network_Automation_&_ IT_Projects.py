import streamlit as st
import pandas
from pathlib import Path

from streamlit.runtime.media_file_storage import MediaFileStorageError

st.set_page_config(
	page_title="Network/Automation Projects",
	page_icon='🐍',
	layout='wide'
)

csv_path = Path(__file__).parent.parent / 'network_automation_projects_data.csv'

st.title("Network Automation & IT Projects")

# st.info("This page is currently a work in progress as I gather the necessary information.")

net_df = pandas.read_csv(csv_path, sep=";")
columns = st.columns(3)

for index, row in net_df.iterrows():
	with columns[index % 3]:
		with st.container(border=True):
			st.subheader(row['title'])
			st.write(row["description"])
			try:
				st.video("net_videos/" + row["video"])
			except MediaFileStorageError:
				st.image("net_images/" + row["image"], use_container_width=True)
			except TypeError:
				st.image("net_images/" + row["image"], use_container_width=True)
			st.write(row['goal'])
			st.write(f"[More Details]({row['url']})")
