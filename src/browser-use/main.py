import asyncio
from pathlib import Path
from dotenv import load_dotenv
from browser_use import Agent, Browser

# Load .env from root
load_dotenv(Path(__file__).parent.parent.parent / ".env")

async def main():
    agent = Agent(
        task="Go to https://news.ycombinator.com and find the top post title",
        browser=Browser(headless=False),
    )
    result = await agent.run()
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
