import requests

def call_ollama(prompt: str, system: str):
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "gemma3:4b",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    })
    return response.json()["message"]["content"]