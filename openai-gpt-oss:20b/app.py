import requests

def ask_ollama(prompt):
    print("Sending prompt to Ollama.")

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "gpt-oss:20b",
        "prompt": f"Think step by step. {prompt}",
        "stream": False,
        "temperature": 0.2
    })

    print("Got response!")
    print(response.status_code, response.text)

    data = response.json()
    return data.get("response", "No response")

if __name__ == "__main__":
    prompt = "I had 3 apples, 2 bananas, and 1 orange. I ate 1 banana and picked 2 more apples. How many fruits do I have now?"
    result = ask_ollama(prompt)
    print("\nGPT-OSS Response:\n", result)
