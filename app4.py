#take message from text file
import pywhatkit as kit
import pyautogui
import time
import webbrowser


# Open the default web browser
webbrowser.open_new('')


# Open the file containing the message
with open("message.txt", "r") as message_file:
    message = message_file.read().strip()  # Read and strip whitespace from the message

# Open the file containing phone numbers
with open("numbers.txt", "r") as file:
    phone_numbers = file.readlines()  # Read all phone numbers

# Loop through the list of phone numbers and send a message to each
for phone_number in phone_numbers:
    phone_number = phone_number.strip()  # Remove any leading/trailing whitespace
    print(f"Sending message to {phone_number}...")

    # Send the message
    kit.sendwhatmsg_instantly(phone_number, message)

    # Wait for a short duration to ensure the message is sent before closing
    time.sleep(3)  # Adjust the sleep time if needed

    # Close the tab (Ctrl + W)
    pyautogui.hotkey('ctrl', 'w')
    print(f"Message sent to {phone_number} and tab closed.")
