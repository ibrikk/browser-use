import asyncio
import json
from pydantic import SecretStr
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Replace with your actual working OpenAI key
api_key = SecretStr("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")

# Load task
with open("data/tasks/my-task.json", "r") as f:
    task_data = json.load(f)[0]

instruction = task_data["instructions"]

llm = ChatOpenAI(
    model="gpt-4o-mini",  # or gpt-3.5-turbo
    temperature=0.0,
    api_key=api_key
)

agent = Agent(task=instruction, llm=llm)

async def main():
    print("🧠 Prompt:", instruction)
    await agent.run()
    print("✅ Agent finished.")

if __name__ == "__main__":
    asyncio.run(main())
