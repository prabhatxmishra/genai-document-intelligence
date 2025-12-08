import os
from dotenv import load_dotenv
import requests

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "mistralai/Mistral-7B-Instruct-v0.2")

if HF_API_TOKEN is None:
    raise ValueError("HF_API_TOKEN is not set in .env")

API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def call_hf_llm(prompt: str) -> str:
    """
    Call Hugging Face Inference API with a simple prompt.
    Returns the generated text as a string.
    """
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 256,
            "temperature": 0.3,
            "return_full_text": False
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

    if response.status_code != 200:
        raise RuntimeError(f"Hugging Face API error: {response.status_code}, {response.text}")

    data = response.json()

    # Response is usually: [{"generated_text": "..."}]
    if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
        return data[0]["generated_text"].strip()

    # Fallback
    return str(data)
