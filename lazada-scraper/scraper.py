from bs4 import BeautifulSoup
from time import sleep
from random import randint
from selenium import webdriver
import xlsxwriter

# Selenium browser webdriver path
browserpath = ""

# Path for output spreadsheet
outputpath = ""

outfile = xlsxwriter.Workbook(outputpath+"/LazadaScrapedResults.xlsx")
outsheet = outfile.add_worksheet()

def writeTo(row, index, name, price, ogprice, discount, stars, review, loc):
    # Writes the information of each article to the excel file

    outsheet.write(row, 0, index)
    outsheet.write(row, 1, name)
    outsheet.write(row, 2, price)
    outsheet.write(row, 3, ogprice)
    outsheet.write(row, 4, discount)
    outsheet.write(row, 5, stars)
    outsheet.write(row, 6, review)
    outsheet.write(row, 7, loc)

writeTo(0, "Index", "Product Name", "Selling Price", "Original Price", "Discount Value", "Rating", "Number of Reviews", "Location")

def NoneCheck(value):
    if type(value) == type(None):
        return ""
    return value.string

def Search(skw):
    browser.get("https://www.lazada.com.my/#")
    sleep(randint(1,3))

    searchBar = browser.find_element_by_id("q")
    submit = browser.find_element_by_class_name("search-box__button--1oH7")

    sleep(randint(2,4))

    searchBar.send_keys(skw)
    submit.click()

def Scrape(skw):
    # Scrapes the website for items related to the search keyword
    Search(skw)

    for j in range(1,2):
        sleep(randint(5,10))
        content = browser.page_source
        soup = BeautifulSoup(content, "html.parser")

        result_item = soup.find_all("div",{"class":"c3KeDq"})

        for i in result_item:
            result_name = NoneCheck(i.find("div",{"class":"c16H9d"}))
            result_price = NoneCheck(i.find("span",{"class":"c13VH6"}))
            result_ogprice = NoneCheck(i.find("del",{"class":"c13VH6"}))
            result_discount = NoneCheck(i.find("span",{"class":"c1hkC1"}))
            result_stars = i.find_all("i",{"class":"c3dn4k"})
            result_review = NoneCheck(i.find("span",{"class":"c3XbGJ"}))
            result_loc = NoneCheck(i.find("span",{"class":"c2i43-"}))

            stars = str.count(str(result_stars),"c3EEAg")
            star_none = str.count(str(result_stars),"c1dtTC")

            if stars+star_none != 5 and star_none != 0 and stars != 0:
                stars += 0.5

            writeTo((result_item.index(i)*j)+1, (result_item.index(i)*j)+1, result_name, result_price, result_ogprice, result_discount, stars, result_review, result_loc)

searchKW = input("Please input your search term\n   > ")

browser = webdriver.Chrome(browserpath)
Scrape(searchKW)

outfile.close()
browser.quit()
