from typing import Dict, TypedDict

from langgraph.graph import END, StateGraph

from .change_directory import change_directory
from .forge_prompt import forge_prompt
from .generate import generate
from .smart_route import smart_route
from .tool_schemas import tool_schemas
from .use_tool import use_tool


class AgentState(TypedDict):
    user_prompt: str
    llm_response: str
    message_history: list
    action: str
    arguments: list
    cwd: str


def prompt_node(state):
    state["user_prompt"] = input(">> ")
    print()
    return state


def generate_node(state):
    SYSTEM_PROMPT = "You are system, a helpful chatbot"
    SYSTEM_PROMPT += f"\nTools you have access to: \n{tool_schemas()}"
    SYSTEM_PROMPT += "\nYou do not possess native tool calling capability"
    SYSTEM_PROMPT += "\nIn order to use a tool, simply respond with the tool name and arguments you wish to enter and the system will handle the rest"
    state["llm_response"] = generate(
        user_prompt=forge_prompt(state["message_history"], state["user_prompt"]),
        system_prompt=SYSTEM_PROMPT,
        temperature=0.5,
    )
    print(state["llm_response"])
    print()
    state["message_history"].append(f"user: {state['user_prompt']}")
    state["message_history"].append(f"system: {state['llm_response']}")
    return state


def smart_node(state):
    result = smart_route(state["llm_response"])
    if result["tool_name"] == "exit":
        state["action"] = "exit"
    elif result["tool_name"] is not None:
        print(
            f"Tool Called: {result['tool_name']} with Arguments {result['arguments']}"
        )
        print()
        state["message_history"].append(
            f"Tool Called: {result['tool_name']} with Arguments {result['arguments']}"
        )
        tool_result = use_tool(result["tool_name"], result["arguments"], state)

        if result["tool_name"] == "change_directory":
            if tool_result:
                try:
                    state["cwd"] = change_directory(
                        state["cwd"], result["arguments"][0]
                    )
                except IndexError:
                    state["cwd"] = change_directory(state["cwd"], None)
                tool_result = "Success"
            else:
                tool_result = "Failure"

        state["user_prompt"] = (
            f"{result['tool_name']} has given the response {tool_result}"
        )
        state["action"] = "llm"
    else:
        state["action"] = "prompt"
    return state


def router(state):
    return state["action"]


graph = StateGraph(AgentState)

graph.add_node("prompt", prompt_node)
graph.add_node("llm", generate_node)
graph.add_node("smart_node", smart_node)

graph.set_entry_point("prompt")
graph.add_edge("prompt", "llm")
graph.add_edge("llm", "smart_node")
graph.add_conditional_edges(
    "smart_node",
    router,
    {
        "exit": END,
        "llm": "llm",
        "prompt": "prompt",
    },
)

app = graph.compile()


def chat(initial_directory):
    app.invoke(
        {
            "user_prompt": "",
            "llm_response": "",
            "message_history": [],
            "action": "",
            "arguments": [],
            "cwd": initial_directory,
        }
    )
