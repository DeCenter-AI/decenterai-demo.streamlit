import logging
import os
import base64
import streamlit as st
from streamlit.commands.page_config import (
    REPORT_A_BUG_KEY,
    ABOUT_KEY,
    GET_HELP_KEY,
)

import public
from config.constants import GITHUB_REPORT_BUG, APP_ABOUT, GITHUB_DISCUSSION_QA


def head():
    with open("static/_style.css") as f:
        logging.info("reading _style.css")
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    col2.image("static/logo.png", width=300)

    st.toast("Welcome to Decenter", icon="🙏")

    # st.image("static/stand.png")
    st.title("AI Infrastructure for Model training")

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def head_v3():
    st.set_page_config(
        page_title="Decenter AI",
        page_icon="static/favicon.ico",
        layout="centered",
        menu_items={
            REPORT_A_BUG_KEY: GITHUB_REPORT_BUG,
            ABOUT_KEY: APP_ABOUT,
            GET_HELP_KEY: GITHUB_DISCUSSION_QA,
            
        },
        initial_sidebar_state="collapsed",
    ) 
    st.markdown(public.button_styles_css, unsafe_allow_html=True)

    st.sidebar.write(
        public.report_request_buttons_html,
        unsafe_allow_html=True,
    )

    st.write(public.index_css, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image(
            "static/cute_robo_avatar.png",
            caption="AI Infrastructure for Model training",
        )
        #st.toast("Welcome to # In the given code, `D` is not doing anything. It is just a placeholder
        # variable name. It is not used or referenced anywhere in the code.
        st.toast("Welcome to DeCenter AI", icon="🙏")

    col2.image(public.logo, width=400)

    #st.sidebar.success("Load complete")
    st.sidebar.title("Demo App V3")
    st.sidebar.text("Download the Samples here!!")
    def create_download_link(file_path, file_name):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        b64 = base64.b64encode(file_data).decode() 
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}.zip">{file_name}</a>'
        return href

    file_options = {
    "Sample1": "samples/demos/simple-linear-regression.zip",
    "Sample2": "samples/demos/multiple-linear-regression.zip",
    "Sample3": "samples/demos/boston-housing-price-prediction.zip",
    "Sample4": "samples/demos/headbrain.zip"
    }

    for project, file_path in file_options.items():
        if os.path.exists(file_path):
            st.sidebar.markdown(create_download_link(file_path, project), unsafe_allow_html=True)

def head_v4():
    # to be tested
    st.markdown(
        """
        <link rel="stylesheet" type="text/css" href="app/static/index.css">
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image(
            "static/cute_robo_avatar.png",
            caption="AI Infrastructure for Model training",
        )
        st.toast("Welcome to Decenter", icon="🙏")

    col2.image(public.logo, width=400)

    #st.sidebar.success("Load complete")
