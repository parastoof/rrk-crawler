import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    driver = webdriver.Chrome() #or webdriver.Firefox()
    driver.get("https://rrk.ir")
    
    wait = WebDriverWait(driver, 10)
    search = wait.until(
        EC.element_to_be_clickable((By.ID, "P0_SEARCH_ITEM_CONTAINER")))
    search.click()

    driver.quit()


if __name__ == "__main__":
    main()
