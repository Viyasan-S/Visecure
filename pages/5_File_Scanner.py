# import virustotal_python

# with virustotal_python.Virustotal("aa7529d5e8ec55dd973a5a9fd1e9a35cb9b16a4ee10d702ad4220c5cb8018896") as vtotal:

import vt
import streamlit as st 
from streamlit_option_menu import option_menu
import time
cl = vt.Client("aa7529d5e8ec55dd973a5a9fd1e9a35cb9b16a4ee10d702ad4220c5cb8018896")

st.title(":blue[File] Scanner")

uploaded_file = st.file_uploader("Upload a file")

if st.button("Scan File"):
    if uploaded_file is not None:
        # Upload the file and get the file ID
        fileid = cl.scan_file(uploaded_file)

        st.write("Scanning file...")
        while True:
            # Get the analysis status
            analysis = cl.get_object("/analyses/{}", fileid.id)
            st.write(f"Status: {analysis.status}")
            if analysis.status == "completed":
                break
            time.sleep(5)

        try:
            # Fetch the scan report
            report = cl.get_object("/files/{}".format(fileid.id))
        
            # Display the report
            st.write("Scan Report:")
            st.markdown(
                f'''
                <style>
                    .container {{
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        padding: 10px;
                        margin: 10px;

                    }}
                </style>
                <div class="container">
                    <b>File Name:</b> {uploaded_file.name}<br>
                    <b>File Size:</b> {report.size}<br>
                    <b>File MD5:</b> {report.md5}<br>
                </div>
                ''',
                unsafe_allow_html=True
            )
            if report.last_analysis_stats['malicious'] > 0:
                st.warning("This file is malicious!")
            else:
                st.success("This file is not malicious.")
                
        except vt.APIError as e:
            st.error(f"Error retrieving report: {e}")
        
        # Close the VirusTotal Client
        cl.close()