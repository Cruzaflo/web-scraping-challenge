#!/usr/bin/env python
# coding: utf-8

# In[2]:


from  splinter import Browser
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

def scrape_all():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=True)

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(3)

    page = browser.html
    soup = bs(page, 'html.parser')


    #Title text and description
    results = soup.find('div', class_='image_and_description_container')

    title = results.find('div', class_='content_title')

    #Returns
    title_text = title.a.text
    description = results.find('div', class_='article_teaser_body').text

    #Image scraping

    #Setup 
    #Browser navigation
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(2)
    browser.click_link_by_id('full_image')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')

    #Large Image HTML
    page = browser.html
    soup = bs(page, 'html.parser')

    #Store large Image URL
    results = soup.find('img', class_='main_image')
    image_link = results['src']

    #return
    featured_image_url = ("https://www.jpl.nasa.gov" + image_link)


    #Table scraping
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_facts = tables[0]
    mars_facts.columns = ['Facts', 'Mars']
    mars_facts.set_index('Facts', inplace=True)

    #return
    fact_table = mars_facts.to_html(classes="table table-striped")

    #Mars Hemispheres
    #browser navigation
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(2)

    #page html
    page = browser.html
    soup = bs(page, 'html.parser')
    results = soup.find_all('a', class_='description')
    results = soup.find_all('div', class_='description')

    hemispheres = []

    for result in results:
        url = result.a['href']
        url_full = ("https://astrogeology.usgs.gov" + url)
        browser.visit(url_full)
        time.sleep(2)
        url_page = browser.html
        url_soup = bs(url_page, 'html.parser')
        url_results = url_soup.find('img', class_="wide-image")['src']
        img_url = ("https://astrogeology.usgs.gov" + url_results)
        title = url_soup.find('h2', class_='title').text
        hem_dic = {
            "title": title,
            "img_url": img_url
        }
        hemispheres.append(hem_dic)

    data = {
        "latest_title": title_text,
        "latest_description": description,
        "featured_image": featured_image_url,
        "mars_fact_table": fact_table,
        "hemispheres": hemispheres
    }

    browser.quit()
    return data 


# In[ ]:




