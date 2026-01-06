import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from skyvern import Skyvern

# Load .env from local dir first, then root
load_dotenv(Path(__file__).parent / ".env")
load_dotenv(Path(__file__).parent.parent.parent / ".env")

async def main():
    api_key = os.getenv("SKYVERN_API_KEY")

    if not api_key:
        print("SKYVERN_API_KEY not found in .env")
        print("Get one from: https://app.skyvern.com/settings")
        return

    print(f"Using Skyvern Cloud API")
    skyvern = Skyvern(api_key=api_key)

    print("Starting task...")
    result = await skyvern.run_task(
        prompt="Go to https://news.ycombinator.com and find the top post title"
    )
    print(f"Result: {result}")
    print("\nView task history at: https://app.skyvern.com/tasks")

if __name__ == "__main__":
    asyncio.run(main())
