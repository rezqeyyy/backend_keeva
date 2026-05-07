import requests

def call_ollama(prompt: str, system: str):
    NGROK_URL = "https://3a87-2402-8780-1065-8907-785e-907-21e-7554.ngrok-free.app" 
    
    response = requests.post(f"{NGROK_URL}/api/chat", json={
        "model": "gemma3:4b",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    })
    return response.json()["message"]["content"]