import base64

hidden_creds = "QUtJQTRTRE5WVDdaSzc2TDIyV0cKUGNYQXArRkRTOTlWdnJybEErZEdZKzl2bkEzbVIvZFU1NFloM2l2eg=="

def find_hidden_creds():
    print("Searching for hidden credentials...")
    return base64.b64decode(hidden_creds).decode('utf-8')

def main():
    creds = find_hidden_creds()
    print(f"Found credentials: {creds}")

if __name__ == "__main__":
    main()
