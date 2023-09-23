import os

# documents
from langchain.document_loaders import DirectoryLoader
# from langchain.document_loaders import TextLoader
from langchain.document_loaders.csv_loader import CSVLoader

from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.agents.agent_toolkits import create_retriever_tool

# Creating the Agent
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI

# Create memory 
from langchain.memory import ConversationBufferMemory

# Create the chain
from langchain.chains import (
    StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
)
from langchain.prompts import PromptTemplate

# UPDATE THESE PARAMETERS AS NEEDED
directory='../data/' # This is the directory containing the CSV/text files.

# Initialize Empty Dictionaries
tool_dict = dict()
embeddings_dict = dict()
db_dict = dict()
retriever_dict = dict()
vector_dict = dict()
description_dict = dict()
answer_dict=dict()
conversation_dict = dict()
doc_dict = dict()

def create_documents(directory='../data/', glob='**/[!.]*', show_progress=True, loader_cls=CSVLoader):
    loader = DirectoryLoader(
        directory, glob=glob, show_progress=show_progress,
        loader_cls=loader_cls)

    documents = loader.load()
    print(f'Number of files: {len(documents)}')
    return documents

def create_retriever(documents, site_key, vector_dict=vector_dict, text_splitter=None):
    """
    Parameters:
        - text_splitter (optional): a text splitter object. If None, the documents are not split. 
    """
    embeddings_dict[site_key] = OpenAIEmbeddings()
    if text_splitter is None: # object type is the same (class 'langchain.schema.document.Document') whether or not the documents are split
        texts = documents
    else:
        texts = text_splitter.split_documents(documents)

    vector_dict[site_key] = FAISS.from_documents(texts, embeddings_dict[site_key])
    retriever_dict[site_key] = vector_dict[site_key].as_retriever()
    return retriever_dict

def create_tools_list(retriever_dict, description_dict):
    """
    https://api.python.langchain.com/en/latest/agents/langchain.agents.agent_toolkits.conversational_retrieval.tool.create_retriever_tool.html?highlight=create_retriever_tool#langchain.agents.agent_toolkits.conversational_retrieval.tool.create_retriever_tool
    """
    tools_list = []
    for site_key, retriever in retriever_dict.items():
        tool_name = f'search_{site_key}'
        tool = create_retriever_tool(retriever_dict[site_key], tool_name, description_dict[site_key])
        tools_list.append(tool)
    return tools_list

def create_chatbot(tools_list=tools_list, vector_store=vector_dict['CoV'], verbose=True):

    llm = ChatOpenAI(
        temperature = 0,
        openai_organization=os.environ['openai_organization'],
        openai_api_key=os.environ['openai_api_key'],
        )

    agent_executor = create_conversational_retrieval_agent(llm, tools_list, verbose)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    template = """You are a helpful assistant who provides concise answers to residents in Metro Vancouver, Canada.
    To make your answer more concise, you ask follow up questions if needed so you can provide the most relevant answer.
    Where relevant, you retrieve the relevant information from your documents to answer the resident's question.
    Here is your chat history with the resident: \n\n{chat_history}\n\n
    Respond to the resident's query, which are delimited by triple backticks: ```{question}```
    """
    prompt = PromptTemplate(
        input_variables=['chat_history', 'question'], 
        output_parser=None, partial_variables={}, 
        template=template, template_format='f-string', validate_template=True)
    chat = ConversationalRetrievalChain.from_llm(
        llm, vector_store.as_retriever(), memory=memory,
        condense_question_prompt=prompt
        )

    return chat

def chat_with_chatbot(user_input, chat, verbose=True):
    result = chat({"question": user_input})
    
    return result

# Prepare the documents
doc_id = 1
doc_dict[doc_id] = create_documents(directory=directory, glob='**/*.csv')
retriever_dict = create_retriever(doc_dict[doc_id], 'recycle')
description_dict['recycle'] = """
From the Recycle BC website, this document provides the most specific information 
about whether or not an item is accepted for recycling and where to recycle it.
This should be the main resource for recycling information for residents of British Columbia.
"""

conversation_id = 1
tools_list_dict[conversation_id] = create_tools_list(retriever_dict, description_dict)


input_id = 1
query = "Where do I recycle coffee cups in Vancouver?"
conversation_dict[conversation_id] = create_chatbot(vector_store=vector_dict['recycle'])
answer_dict[input_id] = chat_with_chatbot(query, conversation_dict[conversation_id])
print(answer_dict[input_id])