import streamlit as st

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

md = """
**project scope**

    To investigate strategies for enhancing and integrating artificial intelligence into the agency's public website

**objectives**

    To enhance citizen engagement efficiency through the implementation of AI solutions.

**data sources**
    
    Web pages from HDB public website 

**features**

    AI-generated quizzes for assessing the knowledge of agency processes and policies among both citizens and staff
    Chatbot to address citizen inquiries regarding specific policies
    AI bot to advise on eligibility and housing loan options.

"""
st.set_page_config(
        page_title="About Us",  
    )

st.markdown(md)