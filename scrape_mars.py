# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
###   NASA Mars News   ###

def init_browser():
    # Setting the chromedriver path
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():

    mars_dict = {}
    ### getting the NASA Mars News ###
    
    # Setting the chromedriver path
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # setting and visiting the url
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)

    # soupifying
    html = browser.html
    soup = bs(html, 'html.parser')

    item_list = soup.select_one('ul.item_list  li.slide')
    mars_dict['news_title'] = item_list.find('div', class_='content_title').text()
    mars_dict['news_p'] = item_list.find('div', class_='article_teaser_body').text()

    
    print(news_title)
    print(news_p)

    return mars_dict



