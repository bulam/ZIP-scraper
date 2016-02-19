#! python3

# A python script that scrapes ZIP code demographics attributes from the map on the ESRI ZIP Tapestry website
# (http://www.esri.com/data/esri_data/ziptapestry) using the selenium module and writes the scraped results into
# an Excel spreadsheet. Because the script is written to be used with the Firefox browser,
# it is necessary to have Firefox installed to run the script.

import os, openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open excel file with the list of all zip codes, with write method
ZIPcodes = openpyxl.load_workbook('replace with directory')
ZIPsheet = ZIPcodes.get_sheet_by_name('replace with sheet')

browser = webdriver.Firefox()

#get URL
URL = ZIPsheet['E' + str(2)].value
print(URL)
#go to URL
browser.get(URL)
AgeValue = browser.find_element_css_selector('meta.itemprop')
print(AgeValue)
    # enter in the text field
    textInput = browser.find_element_by_id('zipCodeInput')
    textInput.send_keys(zip)
    textInput.send_keys(Keys.ENTER)

    # click on the income tab
    income = browser.find_element_by_link_text('Income')
    income.click()
    incomeValue = browser.find_element_by_class_name('chart-value')
    ZIPsheet['B' + str(i+1)].value = incomeValue.text

    #get age and write to a column
    age = browser.find_element_by_link_text('Age')
    age.click()
    AgeValue = browser.find_element_by_css_selector('#age div.chart-value')
    ZIPsheet['C' + str(i+1)].value = AgeValue.text

    #get pop density and write to a column
    density = browser.find_element_by_link_text('Population Density')
    density.click()
    densityValue = browser.find_element_by_css_selector('#population div.chart-value')
    ZIPsheet['D' + str(i+1)].value = densityValue.text

    #clear text field
    textInput.clear()

# save into new file
os.chdir('replace with directory')
ZIPcodes.save('scraped_data.xlsx')


