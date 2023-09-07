import streamlit as st 
from streamlit_option_menu import option_menu as opt  
st.set_page_config(page_title="About",page_icon="icon/mainmenu.png",layout='wide')

sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:center;
                }
            </style>
        """
st.markdown(f"{sty}",unsafe_allow_html=True)

with st.sidebar:
    selected = opt(
        menu_title='About',
        menu_icon='body-text',
        options=['Project','Team']
    )

if selected == 'Project':
    st.write("""
## Product Perspective:
 Visecure is a comprehensive mobile application designed to empower users with cutting-edge security and privacy features, ensuring their digital well-being in an increasingly connected world. 
 It combines state-of-the-art technologies and a user-friendly interface to provide a one-stop solution for all their security needs.
## Product Features:

 * Malware Analysis: Scans both files and file-less malware to protect your device.\n
 * AI-Enabled Phishing Detection: Uses advanced AI algorithms to detect phishing attempts.\n
 * Spam Alert System: Crowd-sources inputs to verify the source of incoming calls, SMS, and emails.\n
 * Obscenity Blocker: Filters out inappropriate content from messages and websites.\n
 * Blockchain-Based Password Manager: Safely stores and manages passwords.\n
 * Real-time Fraud Indicator Flagging: Identifies and verifies calls, SMS, UPI IDs, and URLs in real-time.\n
 * Cybercrime Reporting: Allows users to report cybercrimes easily.\n

## User Classes and Characteristics:

 * General Users: Individuals concerned about their online security and privacy.\n
 * Business Users: Professionals and companies looking to secure their digital assets.\n
 * Parents: Concerned about their children's online safety.\n
 * Law Enforcement: Access to cybercrime reports and partnerships with local police.\n 
 * Cryptocurrency Enthusiasts: Use blockchain-based features for secure transactions.\n 
 * Frequent Travelers: Require VPN and secure communication abroad.\n 

## Special Features:
 * Blockchain Integration: Utilizes blockchain for added security and trust.
 * Crowdsourcing for Threat Detection: Harnesses the power of the community to identify threats.
 * Cybercrime Reporting & Emergency SOS Button: Provides a lifeline during critical situations & Allows users to report crimes easily..
 * Partnerships: Collaborates with government agencies and law enforcement.
 
""")

if selected == 'Team':
    sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:left;
                }
            </style>
        """
    st.markdown(f"{sty}",unsafe_allow_html=True)
    st.title("Team Details")
    st.header("Team Description :")
    st.write("""
         * Welcome to Cipher! We are a dynamic team of visionary professionals determined to address the challenge of predicting student grades accurately. 
         * Our mission is straightforward to develop a system that provides students with reliable grade predictions to make informed decisions about their future career options.
         * Our team comprises experts from diverse fields, who will utilize data analysis techniques and creative approaches to devise innovative solutions. 
         * We value collaboration and encourage brainstorming of ideas from all team members, regardless of size or scope. 
         * Together, we can create something truly extraordinary! Let us work harmoniously towards achieving tangible results. It's time for Cipher to shine!
""")

    st.subheader("Team members : ")
    st.write("""
         * [Viyasan S - ( Team Leader )](https://www.linkedin.com/in/viyasan-sivaraj-12b14b1a4/)
         * [Shabari K S](https://www.linkedin.com/in/shabari-k-s-56421822a) 
         * [Sathyaram R](https://www.linkedin.com/in/sathyaram-r-592b66227)
    """)
