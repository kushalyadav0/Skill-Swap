import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def get_chat_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    return response['choices'][0]['message']['content']
