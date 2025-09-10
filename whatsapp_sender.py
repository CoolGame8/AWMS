import pywhatkit as pwk
import time
from datetime import datetime, timedelta

def send_whatsapp_message(phone_number, message, delay_minutes=1):
    """
    Send a WhatsApp message to a phone number, ( no need to add them to your contacts)
    
    Args:
        phone_number (str): Phone number with country code for exemple: +1234567890
        message (str): Message to send
        delay_minutes (int): Minutes to wait before sending
    
    Returns:
        bool: True if message was scheduled successfully, False otherwise
    """
    try:
        # Get current time and add delay
        now = datetime.now()
        send_time = now + timedelta(minutes=delay_minutes)
        hour = send_time.hour
        minute = send_time.minute
        
        print(f"Scheduling message to {phone_number}")
        print(f"Message: {message}")
        print(f"Scheduled time: {send_time.strftime('%H:%M')}")
        print(f"Please make sure WhatsApp Web is accessible in your browser...")
        
        # Send the message
        pwk.sendwhatmsg(phone_number, message, hour, minute)
        
        print("Message scheduled successfully!")
        print("Note: Keep your computer active and don't close the browser tab that opens.")
        return True
        
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return False

def send_instant_message(phone_number, message, wait_time=5):
    """
    Send a WhatsApp message instantly (opens WhatsApp Web immediately).
    
    Args:
        phone_number (str): Phone number with country code for exemple: +1234567890
        message (str): Message to send
        wait_time (int): Seconds to wait before closing the tab
    
    Returns:
        bool: True if message was sent successfully, False otherwise
    """
    try:
        import pyautogui
        print(f"Sending instant message to {phone_number}")
        print(f"Message: {message}")
        print("Opening WhatsApp Web...")
        
        # Send instant message - leave window open
        pwk.sendwhatmsg_instantly(phone_number, message, 10, False, 8)
        
        # Wait longer for the message to load properly, then press Enter to send
        time.sleep(3)
        pyautogui.press('enter')
        
        print("Message should be sent! Check the WhatsApp Web window.")
        print("Message sent successfully!")
        return True
        
    except Exception as e:
        print(f"Error sending instant message: {str(e)}")
        return False

def main():
    # Get user input
    phone_number = input("Enter phone number (e.g. +972501234567): ")
    
    # Format Israeli phone numbers: replace leading 0 with +972
    if phone_number.startswith('0'):
        phone_number = '+972' + phone_number[1:]
        print(f"Formatted to: {phone_number}")
    
    # Set message text
    message = "your message"
    
    # Send the message instantly
    success = send_instant_message(phone_number, message, wait_time=5)
    
    if success:
        print("Message scheduled successfully!")
    else:
        print("Failed to send message.")

if __name__ == "__main__":
    main()
