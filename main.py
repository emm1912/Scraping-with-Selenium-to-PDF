from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.tijd.be/dossiers/kaaiman/")

locator1 = (By.ID, "didomi-notice-learn-more-button")
cookie_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator=locator1))
cookie_btn.click()
locator2 = (By.CSS_SELECTOR, "button[class='didomi-components-button didomi-button didomi-button-standard standard-button']")
cookie_btn_NIES = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator=locator2))
cookie_btn_NIES.click()

# cookie_btn = driver.find_element(By.ID, "didomi-notice-learn-more-button")
# cookie_btn.click()
# cookie_btn_NIES  = driver.find_element(By.CSS_SELECTOR, "button[class='didomi-components-button didomi-button didomi-button-standard standard-button']")
# cookie_btn_NIES.click()

# page_urls = driver.find_elements(By.XPATH, "//a[@class='c-articleteaser__link']")
# By.C

locator3 = (By.XPATH, "//a[@class='c-articleteaser__link']")
pages_urls = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(locator=locator3))
list_urls = []
for i in pages_urls:
    list_urls.append(i.get_attribute("href"))
print(list_urls)

