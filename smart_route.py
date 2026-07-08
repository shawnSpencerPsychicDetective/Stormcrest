from json import loads

from .generate import generate
from .tool_schemas import tool_schemas

SYSTEM_PROMPT = f"""You are a tool router in a multi-agent system.

Your job is to read an LLM's plain-text message and output EXACTLY one JSON object.

Output format (no extra text):
{{"tool_name": "string or null", "arguments": [list]}}

Rules:
1. Choose the best tool from the catalog below based on intent, not keyword matching.
2. If the message is just a tool name with no explanation, treat it as a request for that tool with arguments = [].
3. Extract arguments as a list of strings in the order the tool expects. If unclear, use [].
4. If no tool matches, or the message is discussing a previous tool output rather than requesting a new call, set "tool_name" to null and put the original message unchanged as the single item in "arguments".
5. Never add commentary, markdown, or explanations. JSON only.

Tool catalog:
{tool_schemas()}
"""


def smart_route(request):
    prompt = f"""Convert the following LLM message:

    \"\"\"{request}\"\"\"

    Return only the JSON object."""
    return loads(
        generate(user_prompt=prompt, system_prompt=SYSTEM_PROMPT, temperature=0)
    )
