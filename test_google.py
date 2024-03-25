# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_title():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )
    
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()



# # create venv # ctrl shift p -> create venv
# python3 -m venv venv
# # activate venv
# linux:
# . venv/bin/activate
# windows: 
# venv\Scripts\activate
# # pip install pytest
# # pip install selenium
# # pip install webdriver_manager