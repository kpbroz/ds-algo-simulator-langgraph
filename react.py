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


def find_duplicate(text: str, mid: int, n: int) -> str:
    st = set()
    slide = text[:mid]
    st.add(slide)
    
    for i in range(mid,n):
        slide = slide[1:mid] + text[i]
        
        if slide in st:
            return (mid, slide)
        else:
            st.add(slide)
            
    return (mid,"")
    


@tool
def palindrome(text: str) -> bool:
    """
    :param text: a string that need to be checked whether it is palidrome or not
    :return: True is text is palindrome else return False"""
    
    print("Inside palindrome()....")
    
    # print(text)
    # print(type(text))
    
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

@tool
def longest_duplicate_substring(text: str) -> str:
    """
    :param text: a string within which duplicate substring need to be found
    :return: return a longest duplicate substring if present. if not return empty string"""
    
    print("Inside longest_duplicate_substring()....")
    n = len(text)
    result_len = 0
    result_string = ""
    
    left, right = 0, n
    
    while left < right:
        mid = (left + right) // 2
        
        # print(left, right)
        
        intermediate_result_len, intermediate_result_str = find_duplicate(text, mid, n)
        
        if intermediate_result_str == "":
            right = mid
        else:
            if intermediate_result_len > result_len:
                result_len = intermediate_result_len
                result_string = intermediate_result_str
                
            left = mid + 1
            
    return result_string
            
            


tools = [palindrome, longest_duplicate_substring]

llm = AzureChatOpenAI(temperature=0, stop=["\nObservation"], model=OPENAI_MODEL, api_key=AZURE_OPENAI_API_KEY, api_version=OPENAI_API_VERSION, azure_endpoint=OPENAI_AZURE_ENDPOINT)

react_agent_runnable = create_react_agent(llm, tools, react_prompt)


if __name__ == "__main__":
    text = "banana"
    
    print(longest_duplicate_substring(text))
