# Crime report and emergency button page

import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        "Select the Option",
        ["Emergency Button","Crime Reporting"]
    )


if selected == "Emergency Button":
    st.markdown("""
    <style>
    button {
       all: unset;
       border: none;
    }
    button:focus{
        outline: none;
    }

    .btn-frame{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 68vh;
    }
    .btn{
        all: unset;
        width: 220px;
        height: 220px;
        border-radius: 50%;
        border: 1px solid;
        background: red;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 30px;
    }
    .btn:focus{
        cursor: pointer;
        shadow: 0 0 10px red;
        transform : scale(1.1);
    }
    </style>
    <div class="btn-frame">
        <div  style='text-align: center;'>
        <button class="btn">Emergency SOS</button>
        </div>
    </div>
    """,unsafe_allow_html=True)

elif selected == "Crime Reporting":
    st.title("Crime Reporting")

    st.file_uploader("Upload a Image", type=("png", "jpg", "jpeg"))

    st.text_input("Enter the name")

    st.text_input("Enter the age")

    st.text_input("Enter Your Mail ID")

    st.text_input("Enter the location")

    st.text_area("Enter the description")

    if st.button("Submit"):
        st.success("Your report has been submitted successfully")
