from chat_functions import *
import streamlit as st

# Prepare the documents
doc_id = 1
try:
    directory = 'data'
    doc_dict[doc_id] = create_documents(directory=directory, glob='*.csv')
except:
    doc_dict[doc_id] = create_documents_from_csv()
    print('Done creating doc from CSV')
retriever_dict = create_retriever(doc_dict[doc_id], 'recycle')
description_dict['recycle'] = """
This document provides information from the Recycle BC website or BC government 
website. It has the most specific information 
about whether or not an item is accepted for recycling and where to recycle it.
This should be the main resource for recycling information for residents of British Columbia.
"""

doc_id = 2
try:
    directory = 'data'
    doc_dict[doc_id] = create_documents(directory=directory, glob='*.txt', loader_cls=TextLoader)
except:
    directory = '../data'
    doc_dict[doc_id] = create_documents(directory=directory, glob='*.txt', loader_cls=TextLoader)
retriever_dict = create_retriever(doc_dict[doc_id], 'mattress')
description_dict['mattress'] = """
Information from the City of Vancouver website about how to recycle mattresses.
"""
tool_id = 1
tool_dict[tool_id] = create_tools_list(retriever_dict, description_dict)


conversation_id = 1
input_id = 1

conversation_dict[conversation_id] = create_chatbot(tool_dict[tool_id], streamlit=True)

# Start the conversation
"""
# Chatbot

"""
query = st.text_input('Your question here') 
answer_dict[conversation_id] = chat_with_chatbot(
    query, conversation_dict[conversation_id], streamlit=True
    ) 

if st.button('Get results'):
    chatbot_response = answer_dict[conversation_id]['output'] 
    st.write(chatbot_response)
else:
    st.write('Click for results')