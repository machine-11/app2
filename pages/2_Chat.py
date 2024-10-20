
import streamlit as st
from logics import prepare_resale 

st.title("Chat")
st.subheader("Buying procedure for reslae flat")
if "messages" not in st.session_state.keys():  # Initialize the chat messages history
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": '''Ask me a question about "buying procedure for reslae flats"''',
        }
    ]

@st.cache_resource
def load_chat():
    return  prepare_resale.load_chat()

#load chat engine
if "chat_engine" not in st.session_state.keys():  
    st.session_state.chat_engine = load_chat()

# fake prompt
if prompt := st.chat_input("Ask a question about buying procedure for reslae flats"):  
    st.session_state.messages.append({"role": "user", "content": prompt})

# Write existing conversation
for message in st.session_state.messages:  # Write message history to UI
    with st.chat_message(message["role"]):
        st.write(message["content"])

#  generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response_stream = st.session_state.chat_engine.stream_chat(prompt)
        st.write_stream(response_stream.response_gen)
        message = {"role": "assistant", "content": response_stream.response}
        # Add response to message history
        st.session_state.messages.append(message)
