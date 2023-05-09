from selenium  import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException , NoSuchElementException 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.common.keys import Keys  
from datetime import datetime

print("""__      __.__            __                                           
/  \    /  \  |__ _____ _/  |_  ______          _____  ______ ______   
\   \/\/   /  |  \\__  \\   __\/  ___/   ______ \__  \ \____ \\____ \  
 \        /|   Y  \/ __ \|  |  \___ \   /_____/  / __ \|  |_> >  |_> > 
  \__/\  / |___|  (____  /__| /____  >          (____  /   __/|   __/  
       \/       \/     \/          \/                \/|__|   |__|     """)  

driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://web.whatsapp.com/")
time.sleep(3)  
print("Scan the QR code and then press Enter")
input()
print("Logged In")
time.sleep(4)
mentor_name = "M Venkatesh"
academy_name = "Selfmade Ninja Academy"
discount_percent = 10


# numbers = ['+91123456789', '+91123456789', '+91123456789']
start_time = time.time()
for number in numbers:
    try:
        search_box = driver.find_element(By.XPATH, value="//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp']") # search box
        search_box.send_keys("+91 123456789") # search for contact
        search_box.send_keys(Keys.ENTER) # press enter
        time.sleep(2)

        focus_message = driver.find_element(By.XPATH, value='//div[@class="tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd dnb887gk gjuq5ydh i2cterl7 p357zi0d kcgo1i74 sap93d0t gndfcl4n _1m68F"]')
        focus_message.click()

        delete_option = driver.find_element(By.XPATH, value='//span[@data-testid="down-context"]')
        delete_option.click()
        delete_message = driver.find_element(By.XPATH, value='//div[@class="iWqod _1MZM5 _2BNs3" and @aria-label="Delete message"]')
        delete_message.click()

        conform_delete = driver.find_element(By.XPATH, value='//button[@data-testid="popup-controls-delete"]')
        conform_delete.click()

        message_box = driver.find_element(By.XPATH, value="//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']") # message box
        message_box.send_keys(f"{number}") # number to send message 
        message_box.send_keys(Keys.ENTER)
        now = datetime.now()
        formatted_time = now.strftime("[%#I:%M %p, %d/%m/%Y]").lower()
        time.sleep(3)

            #searching the text in the chat
        search_text = driver.find_element(By.XPATH, value=f'//div[@data-pre-plain-text="{formatted_time} Selfmade Ninja Academy: "]') # This line may be differ based on the name that you would have given to your whats app account .
        search_text.click()
        time.sleep(2)

        chat_with = driver.find_element(By.XPATH, value='//li[@data-testid="mi-message-on-whatsapp"]')
        chat_with.click()
        time.sleep(2)
                
        new_chat_message = driver.find_element(By.XPATH, value="//div[@data-testid='conversation-compose-box-input']")
        new_chat_message.send_keys(f"Greetings! I'm thrilled to introduce myself as {mentor_name}, your mentor from {academy_name}. We are dedicated to helping individuals like you develop the skills and knowledge needed to excel in the modern business world. That's why we're excited to offer you an exclusive {discount_percent}% discount on one of our selected courses. Our courses are designed with you in mind, providing you with practical knowledge and real-world experience that will help you stand out from the crowd. Let's make you a self-made success story!")

        new_chat_message.send_keys(Keys.ENTER)
            # time.sleep(1)

        print("Message sent to " + number + " at " + formatted_time)
    except Exception:
        print("Message not sent to " + number + " at " + formatted_time)
        continue


time.sleep(2)
end_time = time.time()
time_taken = end_time - start_time
print("Time taken to send messages : ", time_taken)
driver.quit()
print("Message sending completed")
