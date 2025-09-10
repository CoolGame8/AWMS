#!/bin/bash

# WhatsApp Sender Runner Script
# This script activates the virtual environment and runs the WhatsApp sender

echo "🚀 Starting WhatsApp Sender..."
echo "Activating virtual environment..."

# Activate virtual environment
source venv/bin/activate

# Check if activation was successful
if [ $? -eq 0 ]; then
    echo "✅ Virtual environment activated"
    echo ""
    
    # Run the main script
    python whatsapp_sender.py
else
    echo "❌ Failed to activate virtual environment"
    echo "Please make sure you have run: python3 -m venv venv"
    exit 1
fi
