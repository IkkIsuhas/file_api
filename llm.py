import httpx
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("model")
url = "https://openrouter.ai/api/v1/chat/completions"

async def generate_notes(prompt:str)->str:
    header = {
        "Authorization" : f"Bearer {api}",
        "Content-Type" : "application/json"
    }
    payload = {
        "model" : model,
        "messages"  :[
            {
                "role": "system",
                "content": "You are an assistant that creates clear, structured notes."
            },
            {
                "role" : "user",
                "content":prompt
            }
        ]
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url,headers=header,json=payload)
        data = response.json()
        # return data["choices"][0]["message"]["content"]
        return data["choices"][0]["message"]["content"]