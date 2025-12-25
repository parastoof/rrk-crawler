# first version
import time
import jdatetime
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start = time.time()
today = date.today()
jalali_date_today = jdatetime.date.fromgregorian(date=today)
jalali_date_today = jalali_date_today.strftime("%Y/%m/%d")
print(f"today date is: {jalali_date_today}")

ten_days_ago = today - timedelta(days=10)
jalali_date_ten_days_ago = jdatetime.date.fromgregorian(date=ten_days_ago)
jalali_date_ten_days_ago = jalali_date_ten_days_ago.strftime("%Y/%m/%d")
print(f"date of 10 days ago is: {jalali_date_ten_days_ago}")

def main():
    driver = webdriver.Firefox()
    driver.get("https://rrk.ir")
    
    wait = WebDriverWait(driver, 10)
    
    menu = wait.until(
        EC.element_to_be_clickable((By.ID, "t_MenuNav_1")))
    menu.click()

    search = wait.until(
        EC.element_to_be_clickable((By.ID, "t_MenuNav_1_1i")))   
    search.click()

    setdate = wait.until(
        EC.element_to_be_clickable((By.ID, "P199_NEWSPAPERDATE_AZ"))) #P199_SABTNODATE_AZ
    setdate.click()
    setdate.send_keys(jalali_date_ten_days_ago)

    setdate_to = wait.until(
        EC.element_to_be_clickable((By.ID, "P199_NEWSPAPER_TA"))) #P199_SABTNODATE_TA
    setdate_to.click()
    setdate_to.send_keys(jalali_date_today)

    finalsearch = wait.until(
        EC.element_to_be_clickable((By.ID, "B912476867105247978")))
    finalsearch.click()
    
    count_text = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "a-GV-pageRange"))).text

    total = int(count_text.split()[-1])
    print(f"Number of advertisements (approximately): {total}")
    
    driver.quit()
    end = time.time()

    print(f"Total runtime of the program is {(end - start)/60} minutes")

if __name__ == "__main__":
    main()
