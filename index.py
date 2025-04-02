from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure to have the appropriate driver installed)
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
input("Press Enter after scanning the QR code...")

# Example: Send a message to a contact
def send_message(to, message):
    # Find the search box and enter the contact name
    search_box = driver.find_element_by_xpath('//input[@title="Search"]')
    search_box.click()
    search_box.send_keys(to)
    search_box.send_keys(Keys.RETURN)

    # Wait for the chat to load
    time.sleep(2)

    # Find the message box and enter the message
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.RETURN)

# Example usage
send_message('Ceasar', 'Hello, this is a test message!')

# Close the WebDriver
driver.quit()