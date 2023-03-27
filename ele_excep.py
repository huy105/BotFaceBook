from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By

def handle_element(driver, xpath):
    try:
        e_text = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        print("Timeout error occurred while waiting for page to load")    
        return None
    return e_text.text