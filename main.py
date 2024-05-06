from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

os.system('clear')
llm = Ollama(model='phi3:mini')

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. You will only respond with information pertinent to the question asked."),
    ("user", "{userInput}")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "you will summarize what I say into less than 100 words."),
    ("user", "{userInput}")
])

outputParser = StrOutputParser()

chain = prompt | llm | outputParser | prompt2 | llm | outputParser

funnyResponse = chain.invoke('Tell me about platypus?')

print(funnyResponse)