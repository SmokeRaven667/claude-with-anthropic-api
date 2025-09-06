import anthropic

client = anthropic.Anthropic()

model = "claude-sonnet-4-20250514"
max_tokens = 500
messages = []

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=messages
    )
    return message.content[0].text


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# get claude response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

answer = chat(messages)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

answer = chat(messages)

# Get the follow-up response with full context
final_answer = chat(messages)

print(final_answer)
