"""Entry point for Customer-Support-Agent."""

import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from .agent_runtime import run_agent


def main() -> None:
    print("Starting Customer-Support-Agent...")
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
