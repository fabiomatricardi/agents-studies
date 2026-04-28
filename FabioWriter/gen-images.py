import argparse
import requests
import os
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def decrypt_subscription_key(password):
    """Decrypts the Pixazo API key using the provided password."""
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
            encrypted_data = f_file.read()
            return f.decrypt(encrypted_data).decode()
    except Exception:
        print("Error: Decryption failed. Check password or ensure 'pass' file exists.")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Flux-1-Schnell CLI Image Generator")
    parser.add_argument("prompt", type=str, help="The image description")
    parser.add_argument("output", type=str, help="The output filename (e.g., result.png)")
    parser.add_argument("--password", "-p", required=True, help="Password for the 'pass' file")
    
    args = parser.parse_args()

    # 1. Get the Key
    sub_key = decrypt_subscription_key(args.password)
    
    # 2. Prepare the Pixazo Request
    url = "https://gateway.pixazo.ai/flux-1-schnell/v1/getData"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Ocp-Apim-Subscription-Key": sub_key
    }
    
    payload = {
        "prompt": args.prompt,
        "num_steps": 4, # Schnell is optimized for low steps
        "seed": 42,     # You could make this an argument too
        "height": 640,
        "width": 1024
    }

    print(f"Sending prompt to Pixazo: {args.prompt}...")

    try:
        # 3. Call Pixazo API
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result_data = response.json()
        
        image_url = result_data.get("output")
        
        if image_url:
            print(f"Image generated! Downloading from: {image_url}")
            
            # 4. Download the actual image file
            img_data = requests.get(image_url).content
            with open(args.output, 'wb') as handler:
                handler.write(img_data)
            
            print(f"✨ Success! Saved to {args.output}")
        else:
            print("Error: API response did not contain an image URL.")
            print(result_data)

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    main()