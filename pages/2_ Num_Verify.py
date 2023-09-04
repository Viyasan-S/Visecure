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
}
.streamlit-expanderHeader:hover{
    color: rgb(96, 180, 255);
}
.css-1fcdlhc .streamlit-expanderHeader:hover svg{
    fill:rgb(96, 180, 255);
}
.st-ck:hover,.st-ck:focus{
    border: rgb(96, 180, 255);
}
<style>
"""

sl.markdown(f"{style}",unsafe_allow_html=True)


title = 'Visecure'

sl.markdown(f"<h1 style='text-align: center;color:rgb(50,121,123);'>{title}</h1>", unsafe_allow_html=True)

# def is_genuine_number(number):
#     if number.startswith('9') or number.startswith('8') or number.startswith('7') or number.startswith('6') and len(number) == 10:  # Including the '91' prefix
#         return True
#     elif number.startswith('144') and (len(number) != 10):
#         return False
#     else:
#         return False

# def has_unusual_area_code(number):
#     area_codes = ['001', '002', '123', '456', '999']  # Example of unusual area codes
#     prefix = number[:3]
#     return prefix in area_codes

# def has_repeating_digits(number):
#     for i in range(len(number) - 2):
#         if number[i] == number[i+1] == number[i+2]:
#             return True
#     return False

# def has_random_digit_sequence(number):
#     consecutive_count = 0
#     for i in range(1, len(number)):
#         if abs(int(number[i]) - int(number[i-1])) <= 1:
#             consecutive_count += 1
#         else:
#             consecutive_count = 0
#         if consecutive_count >= 3:
#             return True
#     return False


import requests
def is_genuine_number(number):
    url = f"https://truecaller-data1.p.rapidapi.com/rapid_api/truecaller/{number}"

    headers = {
        "X-RapidAPI-Key": "fcdf6023f9mshc7cf048dfe8bfe4p1432adjsn1633aeb1bf4e", #fcdf6023f9mshc7cf048dfe8bfe4p1432adjsn1633aeb1bf4e
        "X-RapidAPI-Host": "truecaller-data1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    # response = {
    #     "success": True,
    #     "data": [
    #         {
    #         "id": "jWAp5q77Jk/eN5OIwkiZ7g==",
    #         "name": "Dedi Suwandi Yagami",
    #         "imId": "1i9tibozg36kg",
    #         "gender": "UNKNOWN",
    #         "about": "",
    #         "jobTitle": "",
    #         "score": 0.9,
    #         "access": "PUBLIC",
    #         "enhanced": True,
    #         "companyName": "",
    #         "phones": [
    #             {
    #             "e164Format": "+6281223222224",
    #             "numberType": "MOBILE",
    #             "nationalFormat": "0812-2322-2224",
    #             "dialingCode": 62,
    #             "countryCode": "ID",
    #             "carrier": "Telkomsel",
    #             "type": "openPhone"
    #             }
    #         ],
    #         "addresses": [
    #             {
    #             "address": "ID",
    #             "street": "",
    #             "zipCode": "",
    #             "countryCode": "ID",
    #             "timeZone": "+07:00",
    #             "type": "address"
    #             }
    #         ],
    #         "internetAddresses": [],
    #         "badges": [
    #             "premium",
    #             "user"
    #         ],
    #         "tags": [],
    #         "cacheTtl": 1296000000,
    #         "sources": [],
    #         "searchWarnings": [],
    #         "surveys": [
    #             {
    #             "id": "0905a705-3c8c-48ab-a4a6-001ce0b20566",
    #             "frequency": 86400,
    #             "passthroughData": "eyAiMyI6ICI2MjgxMjIzMjIyMjI0IiwgIjIiOiAiRGVkaSBTdXdhbmRpIFlhZ2FtaSIsICI0IjogInBmIiB9",
    #             "perNumberCooldown": 31536000
    #             },
    #             {
    #             "id": "4eb9afcf-f36e-430d-86f9-4f72ca091f91",
    #             "frequency": 86400,
    #             "passthroughData": "eyAiMyI6ICI2MjgxMjIzMjIyMjI0IiwgIjIiOiAiRGVkaSBTdXdhbmRpIFlhZ2FtaSIsICI0IjogInBmIiB9",
    #             "perNumberCooldown": 31536000
    #             }
    #         ],
    #         "commentsStats": {
    #             "showComments": False
    #         },
    #         "ns": 0
    #         }
    #     ]
    # }
    # if response['success']:
    #     #sl.write(response['data'])
    return response

def main():
    sl.title("Spam Call Verification")
    number = sl.text_input("Enter your 10 digit number")  # Input number here
    


    def display(response):
        sl.markdown(f"""
            ## Details
            <div style="color:#ffffff;padding:20px;border: 1px solid; border-radius:15px;margin:15px;">
                <strong>Name :</strong> {response['data'][0]['name']}<br>
                <strong>Phone Number :</strong> {response['data'][0]['phones'][0]['e164Format']}<br>
                <strong>Carrier :</strong> {response['data'][0]['phones'][0]['carrier']}<br>
                <strong>Country :</strong> {response['data'][0]['phones'][0]['countryCode']}<br>
                <strong>Time Zone :</strong> {response['data'][0]['addresses'][0]['timeZone']}<br>
                <strong>Score :</strong> {response['data'][0]['score']}<br>
                <strong>Badges :</strong> {response['data'][0]['badges']}<br>
                <strong>Tags :</strong> {response['data'][0]['tags']}<br>
                <strong>Cache Ttl :</strong> {response['data'][0]['cacheTtl']}<br>
                <strong>Sources :</strong> {response['data'][0]['sources']}<br>
                <strong>Search Warnings :</strong> {response['data'][0]['searchWarnings']}<br>
                <strong>Surveys :</strong><br>
                <ul>
                    <li> <strong>id :</strong> {response['data'][0]['surveys'][0]['id']}<br> </li>
                    <li> <strong>frequency :</strong> {response['data'][0]['surveys'][0]['frequency']}<br> </li>
                    <li> <strong>passthroughData :</strong> {response['data'][0]['surveys'][0]['passthroughData']}<br> </li>
                    <li> <strong>perNumberCooldown :</strong> {response['data'][0]['surveys'][0]['perNumberCooldown']}<br> </li>
                    <li> <strong>id :</strong> {response['data'][0]['surveys'][1]['id']}<br> </li>
                    <li> <strong>frequency :</strong> {response['data'][0]['surveys'][1]['frequency']}<br> </li>
                    <li> <strong>passthroughData :</strong> {response['data'][0]['surveys'][1]['passthroughData']}<br> </li>
                </ul>
                <strong>Comments Stats :</strong> {response['data'][0]['commentsStats']}<br>
                <strong>Ns :</strong> {response['data'][0]['ns']}<br>
            </div>
            """,
            unsafe_allow_html=True
        )

    if sl.button('Verify'):
        if len(number) == 10:
            response = is_genuine_number("+91"+number)
            if response['success']:
                if response['success']:
                    sl.success("Verified Number")
                    display(response)
                    
                else:
                    sl.error("Unverified Number")
                    display(response)
            else:
                sl.error("Server Down")
        else:
            sl.error("Invalid Number")
if __name__ == "__main__":
    main()

with sl.expander("About"):
    sl.header(":blue[Description :]")
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
    

