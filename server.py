#!/usr/bin/env python3
"""
Perplexity MCP Server using curl
Simple wrapper around Perplexity API for Claude Code.
"""

import os
import sys
import asyncio
import subprocess
import json
import logging
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)]
)
logger = logging.getLogger("perplexity-mcp")

# Initialize FastMCP server
mcp = FastMCP("perplexity")

# Load environment variables from .env file in the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=env_path)

# Configuration
API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

if not API_KEY:
    logger.error("PERPLEXITY_API_KEY environment variable required")
    sys.exit(1)

logger.info(f"API key loaded: {API_KEY[:10]}...")

# Available models (as of 2025)
MODELS = {
    "sonar": "Lightweight, real-time search with citations (Llama 3.3 70B foundation)",
    "sonar-pro": "Enhanced search with richer context and deeper multi-step queries",
    "sonar-reasoning": "Real-time reasoning with live search and Chain-of-Thought inference",
    "sonar-reasoning-pro": "Advanced step-by-step reasoning (DeepSeek-R1 powered)",
    "sonar-deep-research": "Long-form research, synthesis, and reporting with async support"
}

async def run_curl(data: Dict) -> Dict:
    """Execute curl command to Perplexity API"""
    cmd = [
        "curl", "-s", "-w", "\nHTTP_CODE:%{http_code}",
        "-X", "POST",
        "-H", f"Authorization: Bearer {API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(data),
        API_URL
    ]

    try:
        logger.info(f"Making request to {API_URL} with model {data.get('model')}")

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            logger.error(f"Curl failed with code {process.returncode}")
            logger.error(f"Stderr: {stderr.decode()}")
            raise Exception(f"Curl failed: {stderr.decode()}")

        output = stdout.decode()
        logger.info(f"Received {len(output)} bytes")

        # Extract HTTP code
        if "HTTP_CODE:" in output:
            parts = output.rsplit("HTTP_CODE:", 1)
            body = parts[0].strip()
            http_code = parts[1].strip()
            logger.info(f"HTTP code: {http_code}")

            if http_code != "200":
                logger.error(f"Non-200 response: {http_code}")
                logger.error(f"Body: {body[:500]}")
                raise Exception(f"HTTP {http_code}: {body[:200]}")
        else:
            body = output.strip()

        if not body:
            raise Exception("Empty response from API")

        return json.loads(body)

    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        logger.error(f"Response body: {body[:500] if 'body' in locals() else output[:500]}")
        raise Exception(f"JSON decode error: {e}")
    except Exception as e:
        logger.error(f"Request failed: {e}")
        raise Exception(f"Request failed: {e}")


@mcp.tool()
async def perplexity_ask(
    question: str,
    model: str = "sonar",
    max_tokens: int = 1000,
    temperature: float = 0.7,
    top_p: float = 1.0,
    system_message: str = ""
) -> str:
    """
    Ask Perplexity AI a question.

    Args:
        question: Your question
        model: Model to use (sonar, sonar-pro, sonar-reasoning, sonar-reasoning-pro, sonar-deep-research)
        max_tokens: Max tokens in response (default: 1000)
        temperature: Creativity control 0.0-2.0 (default: 0.7, lower=focused, higher=creative)
        top_p: Nucleus sampling 0.0-1.0 (default: 1.0, lower=more focused)
        system_message: System prompt to guide AI behavior (optional)

    Returns:
        Answer with sources
    """
    try:
        if model not in MODELS:
            return f"ERROR: Invalid model. Choose from: {', '.join(MODELS.keys())}"

        # Build messages array with optional system message
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": question})

        data = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
        }

        response = await run_curl(data)

        # Extract answer
        answer = response.get("choices", [{}])[0].get("message", {}).get("content", "No response")
        citations = response.get("citations", [])

        # Format output
        result = [f"ANSWER ({model}):", "=" * 60, answer, ""]

        if citations:
            result.append(f"\nSOURCES ({len(citations)}):")
            result.append("-" * 60)
            for i, citation in enumerate(citations[:10], 1):
                result.append(f"[{i}] {citation}")

        return "\n".join(result)

    except Exception as e:
        return f"ERROR: {str(e)}"


@mcp.tool()
async def list_models() -> str:
    """List all available Perplexity models"""
    result = ["AVAILABLE MODELS:", "=" * 60]
    for model, desc in MODELS.items():
        result.append(f"\n{model}")
        result.append(f"  {desc}")
    return "\n".join(result)


async def test_connection():
    """Dummy function to test asyncio loop."""
    logger.info("Testing asyncio loop.")
    await asyncio.sleep(0.01)
    logger.info("Asyncio loop test successful.")
    return True

if __name__ == "__main__":
    logger.info("Initializing Perplexity MCP Server...")
    # Run a quick async test to ensure the loop is working
    asyncio.run(test_connection())
    
    logger.info("Starting Perplexity MCP Server...")
    mcp.run(transport='stdio')
