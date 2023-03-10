# Bing Search Bot using Selenium
This Python script automates Bing searches using Selenium. It uses a list of search queries and logs into Bing before performing the searches.

## Tools Required
To run this script, you will need to have the following tools installed:

1. Python 3
2. Selenium
3. ChromeDriver
## How to Install Required Tools

### Python 3
To download and install Python 3, go to the official Python website and download the latest version for your operating system. Follow the installation instructions provided.

### Selenium
You can install Selenium using pip, which is the package installer for Python. Open a command prompt or terminal window and run the following command:


```shell
pip install selenium # it will install selenium and all its dependencies

pip install python-dotenv # it will install python-dotenv and all its dependencies
```

### ChromeDriver
ChromeDriver is a standalone server that implements the W3C WebDriver standard. It allows you to automate web browser interactions, such as clicking buttons and filling out forms.

To download and install ChromeDriver, follow these steps:

+ Go to the ChromeDriver downloads page.
+ Download the appropriate version of ChromeDriver for your operating system and version of Google Chrome.
+ Extract the downloaded zip file to a folder of your choice.
+ Add the folder containing ChromeDriver to your system's PATH environment variable.
## How to Run the Script

1. Clone or download the script to your local machine.
2. Open a command prompt or terminal window and navigate to the directory containing the script.
3. Create a new file named *.env* in the same directory as the script.
4. Open the `.env file` and add your Bing email and password in the following format:


```bash
EMAIL=your_email_address
PASSWORD=your_password
```

5. Save the .env file.
6. Run the script using the following command:

```bash
python3 bing_search_bot.py
# or you can just double click the .py file
```
<mark>The script will log in to Bing using your email and password, perform the search queries, and then close the browser window. The results of the searches will be displayed in the browser window.<mark>