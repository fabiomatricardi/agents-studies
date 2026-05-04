import argparse
import requests
import os
import time
import json  # Added for JSON support
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def decrypt_subscription_key(password):
    try:
        salt = b'static_salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key)
        with open("pass", "rb") as f_file:
            return f.decrypt(f_file.read()).decode()
    except Exception:
        print("Error: Decryption failed.")
        exit(1)

def generate_image(prompt, output_name, sub_key):
    url = "https://gateway.pixazo.ai/flux-1-schnell/v1/getData"
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": sub_key
    }
    payload = {
        "prompt": prompt,
        "num_steps": 4,
        "height": 640,
        "width": 1024
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        image_url = response.json().get("output")
        
        if image_url:
            img_data = requests.get(image_url).content
            with open(output_name, 'wb') as f:
                f.write(img_data)
            print(f"Successfully saved: {output_name}")
        else:
            print(f"API Error: {response.json()}")
    except Exception as e:
        print(f"Error during API call: {e}")

def main():
    parser = argparse.ArgumentParser(description="Flux-1-Schnell JSON Bulk Generator")
    parser.add_argument("output", type=str, help="Base name for output file(s)")
    parser.add_argument("--file", "-f", type=str, help="Path to prompts.json")
    parser.add_argument("--password", "-p", required=True, help="Decryption password")
    
    args = parser.parse_args()
    sub_key = decrypt_subscription_key(args.password)

    if not os.path.exists(args.file):
        print(f"Error: {args.file} not found.")
        return

    # Load prompts from JSON
    with open(args.file, 'r', encoding='utf-8') as f:
        tasks = json.load(f)

    total = len(tasks)
    print(f"Found {total} prompts. Starting generation...")

    for i, task in enumerate(tasks):
        # Accessing data by dictionary keys
        prompt_text = task.get("prompt")
        source_id = task.get("id", i) # Use 'id' if exists, else use index
        
        filename = f"source_{source_id}_{args.output}"
        
        print(f"Processing ({i+1}/{total}): ID {source_id}")
        generate_image(prompt_text, filename, sub_key)

        if i < total - 1:
            print("Waiting 30 seconds...")
            time.sleep(30)

    print("Batch processing complete.")

if __name__ == "__main__":
    main()