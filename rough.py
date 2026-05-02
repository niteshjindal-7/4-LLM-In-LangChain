import os
import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# Load config

with open("config.json", "r") as f:
    config = json.load(f)
provider = config["provider"]

# Initialize the LLM

if provider=="openai":
    llm = ChatOpenAI(
        model = config["openai"]["model"],
        temperature = config["openai"]["temperature"],
        max_tokens = config["openai"]["max_token"],
        api_key=os.getenv("OPENAI_API_KEY")
    )
elif provider=="gemini":
    llm = ChatGoogleGenerativeAI(
        model = config["gemini"]["model"],
        temperature = config["gemini"]["temperature"],
        max_tokens = config["gemini"]["max_token"],
        api_key=os.getenv("GOOGLE_API_KEY")
    )
else:
    raise ValueError("Invalid provider in config.json [It must be openai or gemini only]")


# App Demo

prompt = "What is the capital of Japan?"

print(f"\nUsing Provider: {provider.capitalize()} ({type(llm).__name__})")
print(f"\n\nPrompt: {prompt}")

response = llm.invoke(prompt)

print(f"Bot's Response: {response}")