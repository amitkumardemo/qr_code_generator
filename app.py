import streamlit as st
import qrcode
from PIL import Image
import io
import base64

def generate_qr_code(data, size=150):  # Adjusted size
    """Generate a QR code from the provided data."""
    qr = qrcode.QRCode(
        version=1,  # Fixed version; increase if needed but within limits
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill='black', back_color='white').resize((size, size))

    # Convert PIL Image to BytesIO
    buf = io.BytesIO()
    qr_image.save(buf, format='PNG')
    buf.seek(0)
    return buf

def download_link(buffer, filename):
    """Generate a download link for the QR code image with a download icon."""
    buffer.seek(0)
    b64 = base64.b64encode(buffer.read()).decode()
    download_icon = '<i class="fa fa-download"></i>'  # FontAwesome download icon
    return f'<a href="data:file/png;base64,{b64}" download="{filename}" style="text-decoration: none; color: #007bff; font-size: 18px;">{download_icon} Download QR Code</a>'

# Set page configuration
st.set_page_config(page_title="QR Code Generator", layout="wide")

# Include FontAwesome for icons
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">', unsafe_allow_html=True)

# Logo
st.image("jb.png", width=250)  # Replace with your logo URL

# Navbar
st.markdown("""
<div class="navbar">
  <a href="#Home">Home</a>
  <a href="#About">About</a>
  <a href="https://techiehelpt.netlify.app/">Back To Website</a>
</div>
<style>
    .navbar {
        background-color: blue;
        overflow: hidden;
    }
    .navbar a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    .footer {
        background-color: blue;
        color: white;
        text-align: center;
        padding: 10px 0;
        position: fixed;
        width: 100%;
        bottom: 0;
    }
    .footer a {
        color: white;
        margin: 0 10px;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Add navigation to different sections
menu = ["Home", "About"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Home":
    # Home Page
    st.title("QR Code Generator")
    st.write("Generate QR codes from text and URLs. Enter your data below and download the QR code.")

    # Text input
    text_input = st.text_input("Enter text to generate QR Code:")
    if st.button("Generate QR Code for Text"):
        if text_input:
            try:
                qr_buffer = generate_qr_code(text_input)
                st.image(qr_buffer, caption='QR Code for Text', use_column_width=True)

                # Display download link with icon
                st.markdown(download_link(qr_buffer, 'text_qr_code.png'), unsafe_allow_html=True)
            except ValueError as e:
                st.error(e)
        else:
            st.warning("Please enter some text.")

    # URL input
    url_input = st.text_input("Enter URL to generate QR Code:")
    if st.button("Generate QR Code for URL"):
        if url_input:
            try:
                qr_buffer = generate_qr_code(url_input)
                st.image(qr_buffer, caption='QR Code for URL', use_column_width=True)

                # Display download link with icon
                st.markdown(download_link(qr_buffer, 'url_qr_code.png'), unsafe_allow_html=True)
            except ValueError as e:
                st.error(e)
        else:
            st.warning("Please enter a URL.")

elif choice == "About":
    # About Page
    st.title("About QR Code Generator")
    st.write("""
    This tool allows you to generate QR codes from text and URLs.

    **Features**:
    - Enter text or URL to generate a QR code.
    - Download the generated QR code.

    **Technology Stack**:
    - Streamlit (for building the web app)
    - qrcode (for generating QR codes)
    - PIL (for handling images)
    """)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2024 QR Code Generator | TechieHelp</p>
    <a href="https://www.linkedin.com/in/techiehelp">LinkedIn</a>
    <a href="https://www.twitter.com/techiehelp">Twitter</a>
    <a href="https://www.instagram.com/techiehelp2">Instagram</a>
</div>
""", unsafe_allow_html=True)
