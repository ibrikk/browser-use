import asyncio
import json
import os
from pydantic import SecretStr
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
from browser_use import Agent


load_dotenv()

# Replace with your actual working OpenAI key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in environment variables.")

# Load task
with open("data/tasks/my-task.json", "r") as f:
    task_data = json.load(f)[0]

instruction = task_data["instructions"]

llm = ChatOpenAI(
    model="gpt-4o-mini",  # or gpt-3.5-turbo
    temperature=0.0,
    api_key=SecretStr(api_key)
)

agent = Agent(task=instruction, llm=llm)

async def main():
    print("🧠 Prompt:", instruction)
    await agent.run()
    print("✅ Agent finished.")

if __name__ == "__main__":
    asyncio.run(main())
