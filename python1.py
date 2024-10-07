import base64

hidden_creds = "bmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA="

def find_hidden_creds():
    print("Searching for hidden credentials....")
    return base64.b64decode(hidden_creds).decode('utf-8')

def main():
    creds = find_hidden_creds()
    print(f"Found credentials: {creds}")

if __name__ == "__main__":
    main()
