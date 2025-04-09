import asyncio
import json
import os
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

# Load task
with open("data/tasks/my-task.json", "r") as f:
    task_data = json.load(f)[0]

instruction = task_data["instructions"]

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

agent = Agent(task=instruction, llm=llm)

async def main():
    print("🧠 Prompt:", instruction)
    await agent.run()
    print("✅ Agent finished.")

if __name__ == "__main__":
    asyncio.run(main())
