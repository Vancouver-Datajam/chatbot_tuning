from chat_functions import *
import streamlit as st
from langchain.schema.messages import HumanMessage, AIMessage
from datetime import datetime

recylebc = """
This document provides information from the Recycle BC website or BC government 
website. It has the most specific information 
about whether or not an item is accepted for recycling and where to recycle it.
This should be the main resource for recycling information for residents of British Columbia.
"""

CoV_mattress = """
Information from the City of Vancouver website about how to recycle mattresses.
"""

params_dict = {
    1: {
        'site_key': 'recycle',
        'doc_description': recylebc,
        'text_splitter': None
    },
    2: {
        'site_key': 'mattress',
        'doc_description': CoV_mattress,
        'text_splitter': None
    }
}
# Initialization
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'langchain_messages'
    
    # Prepare the documents
try: # on Streamlit
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if 'streamlit' not in st.session_state:
        st.session_state.streamlit = ''
    if 'embeddings_filepath' not in st.session_state:
        st.session_state.embeddings_filepath = ''
        if 'chat_initiation' not in st.session_state:
            st.session_state.chat_initiation = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        doc_id = 1
        directory = 'data'
        doc_dict[doc_id] = create_documents(directory=directory, glob='*.csv')

        doc_id = 2
        doc_dict[doc_id] = create_documents(directory=directory, glob='*.txt', loader_cls=TextLoader)
        st.session_state.embeddings_filepath = 'embeddings/'
        st.session_state.streamlit = True
        print('Executing on Streamlit')
    except: # on local machine
        doc_id = 1
        doc_dict[doc_id] = create_documents_from_csv()
        print('Done creating doc from CSV')

        doc_id = 2
        directory = '../data'
        doc_dict[doc_id] = create_documents(directory=directory, glob='*.txt', loader_cls=TextLoader)
        st.session_state.embeddings_filepath = '../embeddings/'
        st.session_state.streamlit = False
        print('Executing on local machine')


retriever_dict, description_dict = create_retriever_and_description_dicts(params_dict, st.session_state.embeddings_filepath)

# Create tools
tool_id = 1
tool_dict[tool_id] = create_tools_list(retriever_dict, description_dict)


conversation_id = 1
input_id = 1

conversation_dict[conversation_id] = create_chatbot(tool_dict[tool_id], streamlit=st.session_state.streamlit)

# Start the conversation
"""
# RecyclePro Bot

"""
st.write(f'Chat session initiated at {st.session_state.chat_initiation}')
# Initialize chat history
print(f'\nsession state messages: {st.session_state.messages}')
for message in st.session_state.messages:
    if message['role'] == "user":
        with st.chat_message("user"):
            st.write(f'{message["content"]}')
    elif message['role'] == "assistant":
        print(f'Assistant message: {message["content"]}')
        with st.chat_message("assistant"):
            st.write(f'{message["content"]}')

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-16k"


# prompt =  st.chat_input('Say something') 
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    answer_dict[conversation_id] = chat_with_chatbot(
        prompt, conversation_dict[conversation_id], streamlit=st.session_state.streamlit
        ) 
    chatbot_response = answer_dict[conversation_id]['output'] 
    st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(chatbot_response)