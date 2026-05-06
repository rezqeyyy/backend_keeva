from chatbot.ollama_client import call_ollama
from chatbot.prompt_builder import build_system_prompt

chat_histories = {}  # simpan history per customer_id

def handle_chat(customer_id: str, message: str, churn_data: dict) -> str:
    system = build_system_prompt(churn_data)
    
    if customer_id not in chat_histories:
        chat_histories[customer_id] = []
    
    chat_histories[customer_id].append({"role": "user", "content": message})
    
    reply = call_ollama(message, system)
    
    chat_histories[customer_id].append({"role": "assistant", "content": reply})
    
    return reply