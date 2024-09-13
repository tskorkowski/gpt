import requests

def download_tiny_shakespeare():
    url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open("tiny_shakespeare.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Tiny Shakespeare dataset downloaded successfully.")
    else:
        print(f"Failed to download. Status code: {response.status_code}")

if __name__ == "__main__":
    download_tiny_shakespeare()
else:
    pass