#*******************************************************************************#
# Made by: Gerardo Bustos                                                       #
# Date: 30-05-2023                                                              #
# Title:  Scraping for articles with selenium and saving info to PDF's          #
#...............................................................................#

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import LETTER

#Creating a method to save data to a PDF
def pdf(title, body, url):
    # Instantiating and creating a "document" object
    document = SimpleDocTemplate("pdf/" + title, pagesize=LETTER, rightMargin=72, leftMargin=72, topMargin=18, bottomMargin=18)
    flowables = []
    formatted_time = time.ctime()
    styles = getSampleStyleSheet()
    # Adding nwe style's to use with our pdf's
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    # Adding the time, date at the top left of the document
    ptext = '<font size=12>%s</font>' % formatted_time
    flowables.append(Paragraph(ptext, styles["Right"]))
    # Adding a space between time, date and the title
    flowables.append(Spacer(1, 44))
    # Adding the title of the pdf
    ptext = '<b><font size=12>"%s"</font></b>' % title
    flowables.append(Paragraph(ptext, styles["Centered"]))
    flowables.append(Spacer(1, 12))
    # Adding the body (the article itself)
    ptext = '<font size=12>%s</font>' % body
    flowables.append(Paragraph(ptext, styles["Justify"]))
    flowables.append(Spacer(1, 12))
    # Adding the source url to the document
    ptext = '<a href="{}" color="blue">Source link</a>'.format(url)
    # ptext = '<font size=12>%s</font>' % url
    flowables.append(Paragraph(ptext, styles["Left"]))
    document.build(flowables)

# Creating the webdriver and getting the url
driver = webdriver.Firefox()
driver.get("https://www.tijd.be/dossiers/kaaiman/")

# This handles the cookie pop up
locator1 = (By.ID, "didomi-notice-learn-more-button")
cookie_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator=locator1))
cookie_btn.click()
locator2 = (By.CSS_SELECTOR, "button[class='didomi-components-button didomi-button didomi-button-standard standard-button']")
cookie_btn_NIES = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator=locator2))
cookie_btn_NIES.click()

# Searching the "MEHR LADEN" button to loop until we have all the elemnts (articles) and get the url's
locator3 = (By.CSS_SELECTOR, "button[class='btn btn-link-neutral-3b5']")
btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator3))

# Explicit wait looping the clicking of the "MEHR_LADEN" button until is not found (when end_page = True, the list is fully loaded with all the articles)
end_page = False
while end_page != True:
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
        time.sleep(1)
        btn.click()
    except:
        end_page = True

# Looping and searching for all the url's
locator4 = (By.XPATH, "//a[@class='c-articleteaser__link']")
pages_urls = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(locator=locator4))
list_urls = []
for i in pages_urls:
    list_urls.append(i.get_attribute("href"))

# Looping to get each url from "list_urls" and getting the title and the body of the article
for n, url in enumerate(list_urls, start=1):
    driver.get(url)
    locator5 = (By.CSS_SELECTOR, "h1[itemprop='headline']")
    try:
        title_webobjects = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator=locator5))
        title_text = title_webobjects.get_attribute("textContent")
        locator6 = (By.CSS_SELECTOR, "div[class='ac_paragraph ac_paragraph--first']")
        body_webobjects = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator=locator6))
        body_text = body_webobjects.get_attribute("textContent")
    except:
        title_text = "Not Found"
        body_text = "Not Found"

# Printing and saving the title's and the body's found
    print(str(n) + "-" + title_text, body_text)
    pdf(title=str(n) + "-" + title_text, body=body_text, url=url)

# Quitting the webdriver
driver.quit()





