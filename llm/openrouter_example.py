#!/usr/bin/env python3
"""Minimal example showing how to call ChatOpenRouter with a prompt.

Set your API key in the environment first:

export OPENROUTER_API_KEY="<your-key>"

Then run:

python openrouter_example.py
"""
import os
import sys
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()


def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Please set OPENROUTER_API_KEY in your environment and re-run.")
        sys.exit(1)

    # Choose model from env or use a sensible default
    model_name = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    try:
        model = ChatOpenRouter(model=model_name)
    except Exception as e:
        print("Failed to construct ChatOpenRouter:", e)
        sys.exit(1)

    prompt = "Write a friendly one-line greeting and today's date."
    print("Sending prompt:", prompt)

    # `invoke` accepts a simple input and returns an AIMessage-like object
    resp = model.invoke(prompt)

    # Try common attributes for content
    text = getattr(resp, "content", None) or getattr(resp, "text", None) or str(resp)
    print('\nResponse:\n', text)


if __name__ == "__main__":
    main()
