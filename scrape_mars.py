# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time



def init_browser():
    # Setting the chromedriver path
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():

    # calling the init_browser function
    browser = init_browser()
    
    # defining the dictionary that will hold the results
    mars = {}
    
    ### NASA Mars News ###

    # setting and visiting the url
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)

    # soupifying
    html = browser.html
    soup = bs(html, 'html.parser')

    item_list = soup.select_one('ul.item_list  li.slide')
    mars['news_title'] = item_list.find('div', class_='content_title').text
    mars['news_p'] = item_list.find('div', class_='article_teaser_body').text

   
    ### JPL Mars Space Images - Featured Image ###
    
    # visitng url
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(1)

    # using Splinter to click on the feature image 'Full Image' button
    full_img = browser.find_by_id('full_image')
    full_img.click()
    

    # using Splinter to click on the 'More Info' button
    more_info = browser.find_by_text('more info     ')
    more_info.click()

    # designing xpath to click on the image a get the full resolution on the browser
    xpath = '//div//img[@class="main_image"]'
    results = browser.find_by_xpath(xpath)
    results[0].click()

    # scraping the browser into soup and using soup to get the full resolution image of mars
    html_img = browser.html
    soup_img = bs(html_img, 'html.parser')

    mars['featured_image_url'] = soup_img.body.img['src']

    ### Mars Facts ###
    table_url = 'https://space-facts.com/mars/'

    # reading tables in pandas
    tables = pd.read_html(table_url)
    # reading the first table listed
    mars_facts = tables[0]
    # renaming columns
    mars_facts = mars_facts.rename(columns={0:'Description', 1:'Mars'})
    # setting new index
    mars_facts.set_index('Description', inplace=True)
    # getting html table format
    mars['mars_facts'] = mars_facts.to_html()

    ### Mars Hemispheres ###

# visit the USGS Astrogeology url 
    url_h = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_h)

    # soupifying..
    html = browser.html
    soup = bs(html, 'html.parser')
    # retrieving the titles within the div, class=item, found in h3 element
    items = soup.select('div.item div.description h3')

    hemisphere_image_urls = []
    # looping throught items

    for item in items:
        
        list_dict = {}

        # finding and clicking on the element holding Hemisphere (Splinter)
        browser.find_by_text(item.text).click()
        # finding the image:
        image = browser.find_by_text('Sample').first
        
        # adding k, v to the list_dict
        list_dict['name'] = item.text
        list_dict['img_url'] = image['href']
        
        # appending results to the list
        hemisphere_image_urls.append(list_dict)
    
        # navigating back to previous url
        browser.back()

    mars['hemisphere_image_urls'] = hemisphere_image_urls
    

    return mars



