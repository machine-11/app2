import streamlit as st

md = """
--project scope

--objectives
    POC to showcase LLM 

--data sources
    Web pages from HDB public website 

--features
    this and that

"""
st.set_page_config(
        page_title="About Us",  
    )

st.markdown(md)