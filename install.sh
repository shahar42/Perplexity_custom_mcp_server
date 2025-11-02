#!/bin/bash
# Perplexity MCP Server - Quick Installation Script
# For Linux/macOS users

set -e

echo "================================================"
echo "Perplexity MCP Server Installation"
echo "================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    echo "❌ curl is required but not installed."
    echo "Please install curl and try again."
    exit 1
fi

echo "✓ curl found"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

echo "✓ Dependencies installed"
echo ""

# Setup .env file
if [ ! -f .env ]; then
    echo "🔑 Setting up API key configuration..."
    cp .env.example .env

    echo ""
    echo "Please enter your Perplexity API key:"
    echo "(Get one from https://www.perplexity.ai/)"
    read -p "API Key: " api_key

    if [ -z "$api_key" ]; then
        echo "❌ API key cannot be empty."
        exit 1
    fi

    # Update .env with the provided key
    sed -i "s|your_api_key_here|$api_key|g" .env
    echo "✓ API key configured"
else
    echo "✓ .env file already exists"
fi

echo ""
echo "================================================"
echo "✅ Installation Complete!"
echo "================================================"
echo ""
echo "To start the server, run:"
echo "  source venv/bin/activate"
echo "  python server.py"
echo ""
echo "To integrate with Claude:"
echo "  Copy the path shown above and add to your Claude settings"
echo ""
