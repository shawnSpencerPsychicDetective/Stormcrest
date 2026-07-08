from .compress import compress


def forge_history(message_history):
    history = ""
    for line in message_history:
        history += f"{line}\n"
    return history


def forge_prompt(message_history, prompt):
    if message_history == []:
        return prompt
    final_prompt = "Given the context"
    final_prompt += f"\n{compress(forge_history(message_history))}"
    final_prompt += f"Respond to the user's prompt: {prompt}"
    final_prompt += f"\nNote: You are system"
    return final_prompt
