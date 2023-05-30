import os
import sys
import time

import openai

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

systemPrompt = { "role": "system", "content": "You are a helpful assistant." }
data = []

def get_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        return "clear chat"
    else:  
        data.append({"role": "assistant", "content": incoming_msg})

    messages = [ systemPrompt ]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""


