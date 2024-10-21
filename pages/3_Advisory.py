
import streamlit as st
from logics import crew_elig


from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("Advisory")
st.subheader("Understanding HDB flat eligibility and housing loan options")

# topic = st.text_input("Please enter a detailed query about HDB flat eligibility and housing loan options. The more information you provide, the more accurate and helpful our response will be.")

topic = st.text_area("Please enter a detailed query about HDB flat eligibility and housing loan options. The more information you provide, the more accurate and helpful our response will be.",
value = "I am 38 years old, single, and a Singaporean. I plan to get an HDB flat. What is the maximum amount of subsidy and grants I can possibly receive from the government?" ) 

@st.cache_resource
def load_crew():
    return crew_elig.gen_crew()

if "crew" not in st.session_state.keys():  
    st.session_state.crew = load_crew()


if st.button("Run"):
    with st.spinner('Loading...'):
        result = st.session_state.crew.kickoff(inputs={"topic": topic})
        st.markdown(result.raw)
        st.write(result)
