import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content (
        model = "gemini-2.0-flash-001",
        contents = """What is your context size, explain"""
    )
    print(response.text)

    if response is None or response.usage_metadata is None:
        print("Response is malformed")
    print(f"Prompt token count:{response.usage_metadata.prompt_token_count}")
    print(f"Response token count: {response.usage_metadata.candidates_token_count}")

if __name__=="__main__":
    main()