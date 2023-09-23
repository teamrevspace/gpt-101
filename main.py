import os

import openai

# learn more: https://platform.openai.com/docs/api-reference/chat

openai.api_key = os.environ["OPENAI_API_KEY"]

# you can fine-tune the system prompt and create instructions for the ai chatbot to follow
system_prompt = 'you are a useful assistant. keep the answers under 3 sentences.'

messages = [{
    "role": "system",
    "content": system_prompt
}, {
    "role": "user",
    "content": input("ask me anything: ")
}]

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        temperature=0.8)

print(response.choices[0].message['content'])
