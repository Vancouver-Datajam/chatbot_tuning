import streamlit as st

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
# RecyclePro Bot

"""
# Initialize chat history
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'langchain_messages'
    
if "messages" not in st.session_state:
    st.session_state.messages = []
print(f'\nsession state: {st.session_state["langchain_messages"]}')
for index, message in enumerate(st.session_state['langchain_messages']):
    if (message.content == ''):
        pass
    elif index % 2 == 0:
        with st.chat_message("user"):
            st.write(f'{message.content}')
    else:
        with st.chat_message("assistant"):
            st.write(f'{message.content}')

print(st.session_state.messages)
# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-16k"


# prompt =  st.chat_input('Say something') 
if prompt := st.chat_input("What is up?"):
    answer_dict[conversation_id] = chat_with_chatbot(
        prompt, conversation_dict[conversation_id], streamlit=True
        ) 
    chatbot_response = answer_dict[conversation_id]['output'] 
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(chatbot_response)
    


# def show():
    
#     st.title('Chatbot Page')

#     # Create a text input box for the suer to enter questions.

#     user_input = st.text_input("Ask a question:")
    
#     # Your existing code for chatbot.py

#     # Model and Training and Stuff

#     # Chain
    
#     if st.button('Submit'):
#             # Process the user's question and generate a response
#             #response = generate_response(user_input)  # You need to implement the logic for generating responses
            
            
#         answer_dict[conversation_id] = chat_with_chatbot(user_input, conversation_dict[conversation_id]) 

#         chatbot_response = answer_dict[conversation_id]['response']           
#             #response = "Thank you for ask Question."


#             # Display the user's question and chatbot's response in an output box
#             # with st.expander("Chat Conversation"):
#             #     # st.text_area(f"User: {user_input}")
#             #     # st.text_area(f"Chatbot: {response}")
#             #     st.text_area(label ="",value=response, height =100)
            
#         # Get the background color of the text input box
#         input_box_style = st.get_option("theme.backgroundColor")
        
#         # Display the user's question and chatbot's response in a box with the same background color
#         #st.text(f"User: {user_input}")
#         response_html = f'<div style="background-color: #333333; color: white; padding: 10px;">Chatbot: {chatbot_response}</div>'
#         st.markdown(response_html, unsafe_allow_html=True)

#             # st.text("Answer")
#             # st.write(response)


#     if st.button('Go to Back'):
#             st.session_state.page = "Uber Pickups"

