import streamlit as st
import pandas
from pathlib import Path
# from streamlit_pdf_viewer import pdf_viewer
import fitz

st.set_page_config(
    page_title="Credentials",
    page_icon='📜',
    layout='wide'
)

st.title("Education")
st.write("---")

edu_pdf_dir = Path(__file__).parent.parent / 'images'
bs_file_name = 'BSNES-Cisco.pdf'
aa_file_name = 'Academics.pdf'

dip_col1, dip_col2 = st.columns([1, 2])

with dip_col1:
    with st.container(border=False):
        st.markdown(f"###### Bachelor of Science, Network Engineering and Security - Cisco Track")
        pdf_path = edu_pdf_dir / bs_file_name
        if pdf_path.is_file():
            try:
                # Open the PDF file
                bs_doc = fitz.open(pdf_path)
                bs_page = bs_doc.load_page(0)

                # Render page to a PNG image bytes
                bs_pix = bs_page.get_pixmap()
                bs_img_bytes = bs_pix.tobytes("png")

                # Display the image in Streamlit
                st.image(bs_img_bytes, use_container_width=True)
                bs_doc.close()

            except Exception as e:
                st.error(f"Could not render PDF content for {bs_file_name} as image: {e}")
                st.button(f"PDF Render Error", disabled=True, key=f"pdf_render_error_{bs_file_name}")
            st.markdown("**Acquired:** August 2025")

with dip_col2:
    with st.container(height=400, border=False):
        pdf2_path = edu_pdf_dir / aa_file_name


# st.write("---")

st.title("Certifications")
st.write("---")

csv_path = Path(__file__).parent.parent / 'certifications.csv'
pdf_image_dir = Path(__file__).parent.parent / 'cert_images'

try:
    cert_df = pandas.read_csv(csv_path, sep=";")
except FileNotFoundError:
    st.error(f"Error: The CSV file '{csv_path.name}' was not found. Please ensure it exists at '{csv_path}'.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the CSV file: {e}")
    st.stop()

num_columns = 3
main_cols = st.columns(num_columns)

for index, row in cert_df.iterrows():
    with main_cols[index % num_columns]:
        with st.container(border=False):
            st.markdown(f"###### {row['name']}")
            pdf_file_name = row['pdf']
            pdf_file_path = pdf_image_dir / pdf_file_name  # Construct full path to the PDF

            if pdf_file_path.is_file():
                try:
                    # Open the PDF file
                    doc = fitz.open(pdf_file_path)
                    page = doc.load_page(0)  # Load the first page (index 0)

                    # Render page to a PNG image bytes
                    pix = page.get_pixmap()
                    img_bytes = pix.tobytes("png")

                    # Display the image in Streamlit
                    st.image(img_bytes, use_container_width=True)
                    doc.close()  # Close the PDF document

                except Exception as e:
                    st.error(f"Could not render PDF content for {row['name']} as image: {e}")
                    st.button(f"PDF Render Error", disabled=True, key=f"pdf_render_error_{index}")

                # Display Acquired and Expires dates directly underneath the image
                st.markdown(f"**Acquired:** {row['acquired']}")
                if pandas.notna(row['expires']):
                    st.markdown(f"**Expires:** {row['expires']}")
                else:
                    st.markdown(f"**Expires:** N/A")
                st.markdown(f"**Verify:** {row['verification']}")
            else:
                st.warning(f"PDF file '{pdf_file_name}' not found for {row['name']} at '{pdf_file_path}'.")
                # Display placeholders for dates even if PDF is missing
                st.markdown(f"**Acquired:** {row['acquired']}")
                if pandas.notna(row['expires']):
                    st.markdown(f"**Expires:** {row['expires']}")
                else:
                    st.markdown(f"**Expires:** N/A")
                st.button(f"PDF Missing", disabled=True, key=f"pdf_missing_{index}")

        st.write("---")
             # Add a separator between certification cards for visual clarity
