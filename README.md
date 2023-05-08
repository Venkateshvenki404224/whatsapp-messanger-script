# Automated WhatsApp Message Sender using Python and Selenium WebDriver
This Python script demonstrates how to use the Selenium WebDriver library to automate sending messages to multiple contacts on WhatsApp web. The script uses XPath expressions to locate elements on the web page, and various methods provided by the WebDriver library to interact with those elements.

## Prerequisites
- Python 3.x
- Selenium WebDriver for Python
- Chrome browser
- ChromeDriver executable

## Installation

1. Clone or download the repository to your local machine.

```
git clone https://github.com/Venkateshvenki404224/whatapp-messager-script.git
```
```
cd whatapp-messager-script
```
2. Install the necessary dependencies by running the following command in your terminal or command prompt.

```
pip install -r requirements.txt
```
3. Download the appropriate ChromeDriver executable for your operating system from [here](https://chromedriver.chromium.org/downloads) and save it to the same directory as the script.

## Usage 
1. Modify the following code to work on your machine.

   - Provide the list of numbers that you want to send messages to in list format.
   - Enter your WhatsApp contact number.
   - Change the 'search_text' value in the find_element_by_xpath method to match the name you have given for your WhatsApp web page.

![image](https://user-images.githubusercontent.com/75518037/236820332-3b619eab-9196-4708-a01a-eb12d02179bd.png)

![image](https://user-images.githubusercontent.com/75518037/236818407-775361ec-4398-4a15-9a94-2b5195369fec.png)

![image](https://user-images.githubusercontent.com/75518037/236818159-05a457e5-e2ef-4d8a-9012-debb7ba2b5bc.png)

2. Run the program using the following command.
```
python3 script.py
```
 ## Disclaimer
 This script is for educational purposes only. Use it at your own risk and responsibility. The authors are not responsible for any misuse or damage caused by this script.
