from dotenv import load_dotenv

load_dotenv()

from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph

from nodes import run_agent_reasoning_engine, execute_tools

from state import AgentState

AGENT_REASON = "agent_reason"
ACT = "act"


def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT


graph = StateGraph(AgentState)
graph.add_node(AGENT_REASON, run_agent_reasoning_engine)
graph.add_node(ACT, execute_tools)

graph.set_entry_point(AGENT_REASON)

graph.add_conditional_edges(AGENT_REASON, should_continue)

graph.add_edge(ACT, AGENT_REASON)

app = graph.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")


if __name__ == "__main__":
    print("Hello bvc!")
    
    # text = "can you find the longest duplicate of banana and also check whether hannah is palindrome"
    text = "can you find longest increasing subsequence of [10,9,2,5,3,7,101,18]"
    
    
    res = app.invoke(
        input= {
            "input": text
        }
    )
    print(res["agent_outcome"].return_values["output"])
    