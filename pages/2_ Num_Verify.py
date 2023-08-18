import streamlit as sl
import pickle
import requests
import tldextract
from bs4 import BeautifulSoup
import tldextract
import socket
import whois
from datetime import datetime
from googlesearch import search
import pandas as pd
import bz2file as bz2

sl.set_page_config(page_title='Mobile Spam Detection', page_icon = "hacker.png")

data = bz2.BZ2File('model2.pbz2', 'rb')
pipe = pickle.load(data)

style = """
<style>
.stButton > button{
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 17px 0 17px 0;
    transition: 0.5s ease-in-out;
    color: #a0a0a0;
}

.stButton > button:hover{
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 0px 17px 0px 17px;
    transition: 0.5s ease-in-out;
}
.stButton > button:focus:not(:active){
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 10px 10px 10px 10px;
    transition: 0.5s ease-in-out;
}
.stButton > button:focus{
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 10px 10px 10px 10px;
    transition: 0.5s ease-in-out;
</style>
"""

sl.markdown(f"{style}",unsafe_allow_html=True)


title = '(Visecure)'

sl.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)

def is_genuine_number(number):
    if number.startswith('9') or number.startswith('8') or number.startswith('7') or number.startswith('6') and len(number) == 10:  # Including the '91' prefix
        return True
    elif number.startswith('144') and (len(number) != 10):
        return False
    else:
        return False

def has_unusual_area_code(number):
    area_codes = ['001', '002', '123', '456', '999']  # Example of unusual area codes
    prefix = number[:3]
    return prefix in area_codes

def has_repeating_digits(number):
    for i in range(len(number) - 2):
        if number[i] == number[i+1] == number[i+2]:
            return True
    return False

def has_random_digit_sequence(number):
    consecutive_count = 0
    for i in range(1, len(number)):
        if abs(int(number[i]) - int(number[i-1])) <= 1:
            consecutive_count += 1
        else:
            consecutive_count = 0
        if consecutive_count >= 3:
            return True
    return False

def is_valid_mobile_number(number):
    if len(number) == 10:
        return True
    else:
        return False

def main():
    sl.title("Spam Call Verification")
    number = sl.text_input("Enter your 10 digit number")  # Input number here

    if sl.button('Verify'):
        if number:
            if is_genuine_number(number) and not has_unusual_area_code(number) and not has_repeating_digits(number) and not is_valid_mobile_number and not has_random_digit_sequence(number):
                sl.success("The Mobile Number is Genuine ✅")
            else:
                sl.error("The Mobile Number is Spam 🚨")

if __name__ == "__main__":
    main()

with sl.expander("About"):
    sl.header("Description :")
    sl.write("""
  Team Name - Startup Pro - [ Team Head - Viyasan S ( CEO ) ]
1. S. Viyasan - Project Manager and Lead Developer: responsible for leading the project and managing the team's workflow, setting timelines and goals, and overseeing the development of the phishing page detection system.\n
2. V. Swathi - Data Scientist and Machine Learning Expert: responsible for designing and implementing the machine learning algorithms that will be used to detect phishing pages, as well as analyzing data and making recommendations for improving the system.\n
3. O. Vishnubalan - Front-end Developer and UI/UX Designer: responsible for designing and implementing the user interface for the phishing page detection system, making it intuitive and user-friendly.\n
4. R. Abilash Kumar - Back-end Developer and Database Expert: responsible for designing and implementing the back-end infrastructure for the system, including the database and server-side functionality.\n
5. S. Vivek - Quality Assurance and Testing Specialist: responsible for testing the system thoroughly to ensure it is functioning properly and meets the requirements, identifying and reporting any issues, and providing feedback for improvements.\n
    """)
    sl.write("###")
    sl.write("###")
    

