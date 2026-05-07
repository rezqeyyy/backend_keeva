import requests

def call_ollama(prompt: str, system: str):
    # INGAT: URL ini bakal ganti tiap kali lu restart Ngrok di CMD!
    NGROK_URL = "https://3a87-2402-8780-1065-8907-785e-907-21e-7554.ngrok-free.app" 
    
    try:
        response = requests.post(
            f"{NGROK_URL}/api/chat", 
            json={
                "model": "gemma3:4b", 
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            headers={
                "ngrok-skip-browser-warning": "true" # Wajib ada kalau pake Ngrok gratis
            },
            timeout=30 
        )
        
        response.raise_for_status()
        return response.json()["message"]["content"]
        
    except Exception as e:
        print(f"Error Ngrok: {e}") 
        return "Maaf, AI asisten lagi kehilangan koneksi ke otak pusat (Ollama). Coba lagi ya!"