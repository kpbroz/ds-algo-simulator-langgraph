from dotenv import load_dotenv
import os

from langchain import hub
from langchain.agents import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai import AzureChatOpenAI

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
OPENAI_AZURE_ENDPOINT = os.getenv("OPENAI_AZURE_ENDPOINT")

react_prompt: PromptTemplate = hub.pull("hwchase17/react")


@tool
def palindrome(text: str) -> bool:
    """
    :param text: a string that need to be checked whether it is palidrome or not
    :return: True is text is palindrome else return False"""
    
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


tools = [palindrome]

llm = AzureChatOpenAI(temperature=0, stop=["\nObservation"], model=OPENAI_MODEL, api_key=AZURE_OPENAI_API_KEY, api_version=OPENAI_API_VERSION, azure_endpoint=OPENAI_AZURE_ENDPOINT)

react_agent_runnable = create_react_agent(llm, tools, react_prompt)

if __name__ == '__main__':
    # Wrap the input string in a dictionary
    res = react_agent_runnable.invoke({"input": "check malayalam is a palindrome"})
    print(res)
