"""Simple HTTP text client to test the local LLM backend.

Usage:
    python client/text_client.py

CEO e criador: David Adriano Ferrari dos Santos
"""
import requests
from client.config import BACKEND_URL


def send_chat(messages):
    url = f"{BACKEND_URL}/api/generate"
    payload = {"messages": messages}
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        return r.json()
    else:
        print("Error", r.status_code, r.text)
        return None


if __name__ == "__main__":
    print("Testing text client against", BACKEND_URL)
    # simple conversation example
    messages = [
        {"role": "system", "content": "Você é um assistente útil para os óculos inteligentes Vizo Glass."},
        {"role": "user", "content": "Qual é o status do sistema?"}
    ]
    resp = send_chat(messages)
    print("Response:", resp)
