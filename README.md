# automatic whatsapp message sender - AWMS

A Python script that allows you to send WhatsApp messages programmatically using WhatsApp Web automation.

## Features

- Send scheduled WhatsApp messages (recommended)
- Send instant WhatsApp messages
- Easy-to-use command-line interface
- Supports international phone numbers
- Error handling and user-friendly feedback

## Prerequisites

1. **Python 3.7+** installed on your system
2. **Google Chrome** or **Firefox** browser
3. **WhatsApp Web** access (you need to be able to log into web.whatsapp.com)

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Run the interactive script
```bash
python whatsapp_sender.py
```

### Method 2: Use the functions directly in your code
```python
from whatsapp_sender import send_whatsapp_message, send_instant_message

# Schedule a message (recommended)
send_whatsapp_message("+1234567890", "Hello from Python!", delay_minutes=2)

# Send instantly
send_instant_message("+1234567890", "Hello instantly!", wait_time=15)
```

## Phone Number Format

Always include the country code with a '+' prefix:
- ✅ Correct: `+1234567890` (US number)
- ✅ Correct: `+972501234567` (Israeli number)
- ❌ Wrong: `1234567890`
- ❌ Wrong: `0501234567`

## How It Works

1. **Scheduled Messages**: The script schedules a message to be sent at a specific time (default: 2 minutes from now)
2. **Instant Messages**: Opens WhatsApp Web immediately and sends the message
3. **Automation**: Uses browser automation to interact with WhatsApp Web
4. **Browser Control**: Automatically opens a browser tab, navigates to WhatsApp Web, and sends your message

## Important Notes

⚠️ **Before using:**
- Make sure you're logged into WhatsApp Web (web.whatsapp.com)
- Keep your computer active during the sending process
- Don't close the browser tab that opens automatically
- The script needs an active internet connection

⚠️ **Limitations:**
- Requires WhatsApp Web to be accessible
- May not work if WhatsApp Web layout changes
- Requires browser automation permissions
- Works best with stable internet connection

## Troubleshooting

**"WhatsApp Web not accessible"**
- Make sure you can manually access web.whatsapp.com
- Check your internet connection
- Try logging out and back into WhatsApp Web

**"Message not sent"**
- Verify the phone number format includes country code
- Ensure the recipient has WhatsApp
- Check if WhatsApp Web is working in your browser

**Browser issues**
- Make sure Chrome or Firefox is installed
- Grant necessary permissions when prompted
- Close other WhatsApp Web tabs before running

## Security & Privacy

- This script uses WhatsApp Web, so all WhatsApp's security measures apply
- No messages are stored or logged by this script
- The script only automates what you can do manually on WhatsApp Web
- Your WhatsApp account credentials are never accessed by this script

## Example Usage

```python
# Example 1: Simple scheduled message
send_whatsapp_message("+972501234567", "Hello! This is an automated message.")

# Example 2: Custom delay
send_whatsapp_message("+1234567890", "Meeting reminder!", delay_minutes=5)

# Example 3: Instant message
send_instant_message("+972501234567", "Urgent message!", wait_time=20)
```

## License

This project is for educational and personal use. Please respect WhatsApp's Terms of Service and use responsibly.
